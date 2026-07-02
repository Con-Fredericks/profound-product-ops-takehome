"""
signal_analysis.py

Profound's product classifies unstructured signal from the open web (mentions,
citations, sentiment) into structured categories customers can act on. This
script applies the same move one level up: it takes 15 unstructured quotes
pulled from EM interviews and classifies each one into a structured record
- problem category, urgency, fixability - using the Anthropic API.

The point isn't the script. The point is that the method Profound sells is
the same method that diagnoses Profound's own operational gap. That should
be visible here, not just asserted in the writeup.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python3 signal_analysis.py

Input:  quotes_raw.txt   (15 numbered quotes, one per line)
Output: signal_output.json (structured classification, one record per quote)
"""

import json
import os
import re
import sys
from pathlib import Path

MODEL = "claude-sonnet-4-5-20250929"

INPUT_PATH = Path(__file__).parent / "quotes_raw.txt"
OUTPUT_PATH = Path(__file__).parent / "signal_output.json"

# Three categories, converged on before this script runs. The model is not
# asked to invent categories - it's asked to route each quote into one of
# them, the same way Profound's classifier routes a citation into a topic
# bucket rather than discovering topics from scratch each time.
CATEGORIES = {
    "knowledge_doesnt_travel": (
        "Internal knowledge doesn't travel: something shipped, changed, or "
        "was built by one person, and the people who need it (other EMs, "
        "the EM in front of a customer) don't have it."
    ),
    "no_standards": (
        "No standards, everything rebuilt from scratch: the same artifact "
        "(deck, doc, explanation, workflow) gets recreated repeatedly "
        "because no shared version exists or can be found."
    ),
    "no_activation_loop": (
        "No activation loop, customer success is accidental: onboarding and "
        "early usage have no designed path to a win, so outcomes depend on "
        "whatever the customer or EM improvises."
    ),
}

# Forces the model to answer in the shape we need instead of prose. This is
# the structured-output discipline Profound's own classification pipeline
# depends on - unstructured input in, typed record out, nothing left to
# parse out of a paragraph.
CLASSIFY_TOOL = {
    "name": "classify_quote",
    "description": "Classify one EM interview quote against a fixed operational taxonomy.",
    "input_schema": {
        "type": "object",
        "properties": {
            "category": {
                "type": "string",
                "enum": list(CATEGORIES.keys()),
                "description": "Which of the three converged problem categories this quote is primary evidence for.",
            },
            "urgency": {
                "type": "integer",
                "enum": [1, 2, 3],
                "description": (
                    "1 = discomfort or inefficiency, no customer-facing harm yet. "
                    "2 = recurring friction with a plausible link to churn or lost expansion. "
                    "3 = quote describes a customer-visible failure (fumbled explanation, "
                    "churn, unmanaged risk) that already happened or is actively happening."
                ),
            },
            "fixability": {
                "type": "integer",
                "enum": [1, 2, 3],
                "description": (
                    "1 = depends on something outside Profound's control (e.g. the "
                    "customer's own org). 2 = fixable but requires designing a new "
                    "workflow or process. 3 = fixable with a comms/distribution or "
                    "documentation change, no new process required."
                ),
            },
            "rationale": {
                "type": "string",
                "description": "One sentence: why this category, urgency, and fixability.",
            },
        },
        "required": ["category", "urgency", "fixability", "rationale"],
    },
}

SYSTEM_PROMPT = (
    "You are classifying internal interview quotes from Engagement Managers "
    "at an AI visibility analytics company. Route each quote into exactly "
    "one of three pre-defined operational problem categories, then score "
    "urgency and fixability. Do not invent new categories. Do not soften "
    "the score to be diplomatic - score what the quote actually describes."
)


def load_quotes(path: Path) -> list[str]:
    """Strip the leading 'N. ' index and surrounding quotes, keep the text."""
    quotes = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(r"^\d+\.\s*\"(.*)\"$", line)
        quotes.append(match.group(1) if match else line)
    return quotes


def classify(client, quote: str, model: str) -> dict:
    category_list = "\n".join(f"- {k}: {v}" for k, v in CATEGORIES.items())
    message = client.messages.create(
        model=model,
        max_tokens=500,
        system=SYSTEM_PROMPT,
        tools=[CLASSIFY_TOOL],
        tool_choice={"type": "tool", "name": "classify_quote"},
        messages=[
            {
                "role": "user",
                "content": (
                    f"Categories:\n{category_list}\n\n"
                    f'Quote: "{quote}"\n\n'
                    "Classify it."
                ),
            }
        ],
    )
    for block in message.content:
        if block.type == "tool_use":
            return block.input
    raise RuntimeError(f"No tool_use block returned for quote: {quote!r}")


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit(
            "ANTHROPIC_API_KEY is not set. Export it before running:\n"
            "  export ANTHROPIC_API_KEY=sk-ant-...\n"
            "This script makes live calls to the Anthropic API and does not "
            "run offline."
        )

    try:
        import anthropic
    except ImportError:
        sys.exit("Missing dependency. Run: pip install anthropic")

    client = anthropic.Anthropic()
    quotes = load_quotes(INPUT_PATH)

    results = []
    for i, quote in enumerate(quotes, start=1):
        classification = classify(client, quote, MODEL)
        results.append(
            {
                "id": i,
                "quote": quote,
                "category": classification["category"],
                "urgency": classification["urgency"],
                "fixability": classification["fixability"],
                "rationale": classification["rationale"],
            }
        )
        print(f"[{i}/{len(quotes)}] {classification['category']} "
              f"(urgency={classification['urgency']}, "
              f"fixability={classification['fixability']})")

    OUTPUT_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nWrote {len(results)} classified records to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
