# Findings: EM Interview Signal Analysis

15 quotes from Engagement Manager interviews, classified by problem category, urgency, and fixability using the same signal-extraction approach Profound applies to customer-facing data. The categories were fixed before classification. The scores below are what the quotes actually describe, not a diplomatic average.

## Categories

**Category 1 - Internal knowledge doesn't travel.** Something ships, changes, or gets built, and the people who need it next don't have it. An EM finds out about a launch from a customer. An update ships and nobody knows which accounts it touches. Two features exist separately in an EM's head but nobody has connected them into one explanation. Quotes: 1, 5, 6, 12, 15.

**Category 2 - No standards, everything rebuilt from scratch.** The same artifact gets recreated repeatedly because no shared version exists or can be found. Onboarding decks, workflow docs, competitive tracking, an explanation of how a feature works. Quotes: 2, 4, 7, 9, 11.

**Category 3 - No activation loop, customer success is accidental.** Onboarding has a script for week one and nothing after. There's no designed moment where a customer gets a win. Outcomes depend on whether the customer arrived with a specific question or an internal champion, both accidents of who signed up, not anything Profound built. Quotes: 3, 8, 10, 13, 14.

Five quotes each. Not engineered - that's just where the evidence lands.

Quote 15 ("we keep saying we'll do an internal training when things slow down") is Category 1, but it's doing different work than the other four. It's not describing a knowledge gap - it's describing why the obvious fix for a knowledge gap (schedule a training) doesn't survive contact with a team that ships constantly. That's the strongest argument in this dataset for what the Category 1 fix has to look like: not a training program competing for time against shipping, but something that rides along with the ship itself and costs nothing to skip.

## Root cause

Shipped work arrives without an operational layer. Product ships a feature; nobody ships the explanation, the positioning, or the "here's who this affects" alongside it. That gap is Category 1 directly. It's also the upstream cause of Categories 2 and 3: EMs rebuild decks and explanations from scratch (Category 2) because no standard version ever got produced at ship time. Onboarding has no designed aha moment (Category 3) because there's no current, trustworthy material to build one around, so EMs improvise a new one every time.

Three categories, one root cause, three distances from the customer. Category 1 is the failure at the source. Category 2 is that failure showing up as duplicated EM labor. Category 3 is that failure showing up as inconsistent customer outcomes. Fix Category 1 and the other two lose their fuel supply, not because they disappear on their own, but because EMs stop working from nothing.

## Prioritization logic

Rank by urgency times fixability, not urgency alone. A quote can describe real pain and still be the wrong place to start if fixing it requires redesigning a process rather than closing a distribution gap.

Category 1 quotes score high on both. Three of five hit urgency 3 - a customer-facing fumble, an unmanaged risk window, a customer question an EM couldn't answer - and fixability holds at 3 for four of five, because the fix is "ship the explanation with the feature," not "invent a new workflow." Quote 15 is the outlier on fixability, scored a 2, and that's the point: it shows the team already tried the obvious fix (schedule training) and watched it lose to shipping velocity every time. That combination is why Category 1 goes first: it's where the damage is already reaching customers and where the fix is closest to a comms and documentation change, not a rebuild - as long as the fix is built to survive the exact failure mode quote 15 describes.

Category 2 is real cost but lower urgency. Rebuilding a deck or a workflow doc wastes EM time; it rarely loses a customer by itself. It's also highly fixable - a shared repository or template closes most of it - but low urgency means it's not where the bleeding is.

Category 3 has the highest average urgency of the three (churn, no week-two answer, no aha moment) and the lowest average fixability. Fixing it means designing an activation path, not distributing an existing asset, and one of its quotes (13, the internal-champion dependency) is partly outside Profound's control regardless of what gets built. High-urgency, low-fixability problems are the ones teams default to solving first because they hurt the most, and that instinct is backwards here: without Category 1 fixed, any activation loop Category 3 builds will run on stale or missing material anyway.

Fix order: Category 1, then 2, then 3.

## Why the other two aren't the starting point

Category 2 isn't first because it's a cost problem, not a churn problem - it wastes EM hours but the quotes don't show it losing customers on its own, and it's already the easiest of the three to fix once Category 1 gives EMs a source of truth to standardize from.

Category 3 isn't first despite being the highest-stakes category because its fixes require building new onboarding infrastructure rather than closing a distribution gap, and building that infrastructure now would mean designing activation moments around product knowledge that's still arriving late and incomplete.
