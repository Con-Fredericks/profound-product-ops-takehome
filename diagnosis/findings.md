# Findings: EM Interview Signal Analysis

15 quotes from Engagement Manager interviews, classified by problem category, urgency, and fixability. The method mirrors Profound's own Intent classification in Prompt Volumes, where the taxonomy is fixed before classification rather than discovered from the data afterward. The scores separate noise from the operational problems that are fixable and urgent enough to act on.

## What's Broken

Profound ships fast. CEO James Cadwallader counted six new features in June alone, including agentic workflows, Slack and external MCP integrations, and Projects, and called the pace "insane" (Cadwallader, 2026). By account of the engagement managers interviewed, nothing ships alongside that pace to help the people who sell and support the product actually use what changed. That gap shows up three ways across these 15 quotes:

1) A feature ships, or one EM builds something worth reusing, and the rest of the team finds out too late to help a customer.
2) With no standard version of a deck, doc, or workflow, each EM rebuilds the same material from scratch.
3) Onboarding covers week one and then stops, so whether a customer reaches a first win comes down to luck.

The three gaps share one root cause, and it is structural. Profound ships faster than the field can absorb, and no function owns the work of turning a shipped feature into something an EM can sell and support: the explanation, the deck, the workflow, the week-two onboarding beat. At most companies a product marketing or launch PM owns that work. A product org lean enough to keep this ship pace has little left to also own it, so by account of these 15 quotes it sits with no one, and each EM improvises it per account or skips it. The hypothesis this diagnosis rests on is that the failure is a missing operational layer, with the EM behavior in these quotes as its symptom.

Call it the launch-to-field layer. Its absence surfaces first as the travel gap: what ships, and what one EM builds, never reaches the rest of the team. The other two follow. With no standard version produced at ship time, EMs rebuild decks and workflows from scratch, and with no current material to anchor it, onboarding has no reliable win moment. Stand up that layer and the other two lose the reason they keep happening.

Fix that one first. It is the largest of the three by volume (7 of 15 quotes), effectively ties the most urgent on urgency alone, and is by far the easiest to close. The table below numbers them 1 through 3 in priority order.

This gap gets more expensive from here. Profound passed 10 percent of the Fortune 500 at its February 2026 Series C (Profound, 2026) and is at 14 percent now, still shipping features weekly (Cadwallader, 2026). McKinsey's study of B2B SaaS companies that scaled past $100M in ARR found that once product-market fit is set, go-to-market becomes the deciding factor, and it named customer success the most underused lever, ignored until churn climbs (Beerthuis et al., 2024). Both findings point at the layer these quotes expose. Profound already builds the outward half of it, the Profound Ecosystem of University, certification, and an agency marketplace that trains customers and partners (Profound, 2026). The inward half, the pipeline from a shipped feature to what an EM says and does in front of a customer, is what these 15 quotes show missing. Build it, and fast shipping compounds into deeper Fortune 500 penetration instead of outrunning the field.

## Method

Quotes were classified by category, urgency, and fixability using `signal_analysis.py`, an LLM classifier run against a taxonomy fixed before classification starts. Profound classifies its own data the same way. For Intent in Prompt Volumes it rejected two approaches, public LLM APIs as too costly at its scale and traditional NLP classifiers as too rigid to generalize, and self-hosts its own language models instead (Babbs et al., 2025). Sentiment works the opposite way, with themes that are open-ended and emergent rather than fixed in advance (Lafferty, 2026). Profound validates its Intent classifier against a published external distribution, OpenAI's study of ChatGPT usage (OpenAI, 2025). This analysis doesn't have that check yet. It is a single pass with no second rater, and it already surfaced one inconsistency worth naming, covered below. Full model output and rationale: `signal_output.json`.

## The Categories

| # | Category | What breaks | Quotes | Count | Avg urgency | Avg fixability |
|---|---|---|---|---|---|---|
| 1 | Knowledge doesn't travel | A feature ships, an update lands, or useful work gets built somewhere in the org, and the people who need to know don't find out in time to use it or help a customer with it. | 1, 4, 5, 6, 7, 12, 15 | 7 | 2.3 | 2.9 |
| 2 | No standards | The same deck, doc, or workflow gets rebuilt from scratch because no shared version exists or can be found. | 2, 9, 11 | 3 | 1.7 | 3.0 |
| 3 | No activation loop | Onboarding has a script for week one and nothing after. Whether a customer succeeds depends on luck: did they arrive with a specific question, do they have an internal champion. | 3, 8, 10, 13, 14 | 5 | 2.4 | 2.0 |

Knowledge that doesn't travel is the biggest problem here, seven of the fifteen quotes. Two of them look like standards problems at first and aren't. One EM keeps a sentiment explainer in a personal Notion page that three others have asked him to send; another built a strong competitive-tracking workflow for a customer and has no idea whether anyone else knows it exists. Neither is being rebuilt. The material exists and never reached the people who needed it, which is a travel problem, not a standards one, and it is what makes this the largest group.

One of these seven does extra work. The team keeps saying it will run an internal training once things slow down, and things have not slowed down. That explains why the obvious fix already failed: a scheduled training loses to shipping velocity every time. Whatever fixes this has to ride along with the ship, not wait for a quiet week that never comes.

The activation gap, onboarding that stalls after week one, actually edges the travel gap on urgency, 2.4 to 2.3. Fixability is where they part. The travel quotes mostly close with better distribution and average 2.9; the activation quotes average 2.0, and every one scored a 2, meaning none of them closes with a document. One arguably scores lower still: the account that only thrives when the customer has an internal champion depends on the customer's own org, which the rubric defines as the least fixable case, a 1 rather than the 2 the model gave it. That is the exact caution the take-home flags, that not every quote points to a fixable operational problem. Correct it and the activation average drops to 1.8, widening the gap.

The standards gap is the smallest and cheapest, three quotes and the most fixable of the three at 3.0, and it gets cheaper once the travel fix gives EMs a current source of truth to standardize from. One seam is worth admitting: two quotes describe the same failure, an artifact nobody can find, and the classifier filed them under different problems anyway. That is what a single pass with no second rater produces. Fix the travel gap first, then standards, then activation.

## Why the Others Wait

Both wait for the same underlying reason: each needs what the launch-to-field layer produces, so neither closes until that layer exists.

The standards gap waits because it is a cost problem, not a churn problem. It is the smallest of the three, and cheaper to close once the layer gives EMs a current source of truth to standardize from.

The activation gap waits because closing it means building new onboarding infrastructure, not shipping a distribution fix, and that infrastructure needs current product knowledge to build around, which the layer supplies.

The fix for the travel gap is that layer, built next as its own artifact rather than recommended here, in the form the take-home asks for: a process doc, a template, a framework.

## Appendix: Per-Quote Scores

| # | Quote (excerpt) | Category | Urgency | Fixability |
|---|---|---|---|---|
| 1 | "I found out we launched a new citations feature because a customer asked..." | 1 | 3 | 3 |
| 2 | "Every time I onboard a new customer I basically rebuild my whole deck..." | 2 | 2 | 3 |
| 3 | "We had a customer churn last quarter... they just never really got started" | 3 | 3 | 2 |
| 4 | "I have a whole Notion page I built myself for explaining how sentiment works..." | 1 | 2 | 3 |
| 5 | "When something new ships I usually find out from the Slack announcement..." | 1 | 2 | 3 |
| 6 | "...asked me to walk them through the difference between citations and prompt volumes... fumbled it" | 1 | 3 | 3 |
| 7 | "We built this whole competitive tracking workflow for a customer in Q1..." | 1 | 2 | 3 |
| 8 | "My customers who are succeeding are the ones who came in with a specific question..." | 3 | 2 | 2 |
| 9 | "I asked two other EMs how they explain agents to new customers... three completely different answers" | 2 | 2 | 3 |
| 10 | "There's no moment in onboarding where the customer has a win..." | 3 | 2 | 2 |
| 11 | "I spent two hours last week recreating a workflow doc..." | 2 | 1 | 3 |
| 12 | "Product dropped a big update two weeks ago. I still haven't had time..." | 1 | 2 | 3 |
| 13 | "The customers who get the most value are the ones who have someone internally who owns it..." | 3 | 3 | 2 |
| 14 | "I don't have a good answer when a customer asks me what they should do in week two..." | 3 | 2 | 2 |
| 15 | "We keep saying we'll do an internal training when things slow down..." | 1 | 2 | 2 |

## References

Babbs, D., Vaghar, A., & Chandrappa, S. (2025, November 4). Data science at Profound: How people use answer engines. *Profound Engineering Blog*. https://www.tryprofound.com/engineering/data-science-at-profound-how-people-use-answer-engines

Beerthuis, T., Jules, C., Markovitch, S., & Seiler, C. (2024, April 29). From start-up to centaur: Leadership lessons on scaling. *McKinsey & Company*. https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/from-start-up-to-centaur-leadership-lessons-on-scaling

Cadwallader, J. (2026, June 30). Closing out June and the team continues to move at an insane speed [LinkedIn post]. LinkedIn. https://www.linkedin.com/in/jsca/

Lafferty, N. (2026, February 10). How to track brand sentiment in answer engines with Profound. *Profound Blog*. https://www.tryprofound.com/blog/how-to-track-brand-sentiment-in-answer-engines

OpenAI. (2025, September 15). How people are using ChatGPT. https://openai.com/index/how-people-are-using-chatgpt/

Profound. (2026, February 24). Profound raises Series C at $1B valuation to lead a new category of marketing [Press release]. *GlobeNewswire*. https://www.globenewswire.com/news-release/2026/02/24/3243475/0/en/Profound-Raises-Series-C-at-1B-Valuation-to-Lead-a-New-Category-of-Marketing.html
