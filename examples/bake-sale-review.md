# Example: a `standard` review of a school bake-sale plan

Real output of `/sota:sota review plan.md` on the 1.0.0 protocol, with the prompt "I am a parent volunteer at the school. Do not ask me anything." The plan was written as a test input. The report below is unedited. Measured cost: USD 7.24 at API prices on an Opus-class model.

## The input

```markdown
# Bake sale for the school library

Goal: raise $5,000 in one Saturday so the library can buy new books.

1. Ask parents to bake 50 cakes.
2. Sell each cake for $10 at the school gate from 9 to 11 am.
3. Announce it in the newsletter the day before.
4. Food safety is not a concern because everything is homemade.
```

## The report

# Curia verdict: Bake sale for the school library (`plan.md`)

**Verdict:** NOT YET, reframed
**Why, in one line:** Selling every cake raises $500, a tenth of the $5,000 goal, and the plan's food-safety statement is false. Both can be fixed before anything is announced.
**Confidence:** High on the verdict: the sum was computed, and a separate verifier opened the food-safety sources. Low on how much the redesigned drive would raise, because school size is unknown and the comparable sales are anecdotes.
**Mode:** standard · Seats: Verifier, Red Team, Steelman, Outside View, Pragmatist, food-safety source check (not a professional)
**Model families:** 1. Seats ran in separate contexts with different methods; this is not independent human review.
**For a qualified person:** This prepares the conversation and does not replace it. Your local health office or council and the school must decide whether a permit, registration or sign applies, whether the seller qualifies as a charity, whether the gate counts as school premises, which foods are allowed, and what allergen wording is needed. The rules differ by place, and the plan does not say where the school is.

## Objective Curia evaluated against

"Raise $5,000 in one Saturday so the library can buy new books." Assumed success criteria: the sum reaches the library, nobody is harmed, and the school and volunteers would run it again.

### Challenge to the objective

Five of six seats challenged the objective, in two ways:

- **The goal bundles a need with a chosen method.** The library needs money for books. "One Saturday" and "bake sale" are means.
- **Nothing shows where $5,000 comes from.** The plan has no book list or prices.

**Corrected objective:** pay for the library's confirmed book list, safely, with donations carrying most of the sum and the Saturday sale as the event that brings families together.

If the single day truly matters, the honest target for cakes alone is about $500 (the plan's own maximum, if every cake sells). The verdict and curated plan below assume the corrected objective.

## Must change

1. **R1. The sums fall short by $4,500.** (blocker) `verified` · `converged`, all six seats
   - Evidence: step 1 "50 cakes" × step 2 "$10" = $500. Reaching $5,000 takes 500 cakes at $10, one sale every 14.4 seconds for two hours, or $100 a cake. Slices do not close the gap: 50 cakes × 12 slices × $3 = $1,800, at an assumed price.
   - Fix: state $500 as the sale's maximum and name a separate source for the rest (curated goal and figures).

2. **R2. Step 4 is false, and buyers have no way to learn what is in a cake.** (major, after contention) `verified` that the statement is wrong; how often harm occurs is unmeasured · `converged`
   - Evidence: "Food safety is not a concern because everything is homemade."
     - The official sources opened treat home baking as needing conditions. FDA's model Food Code excludes a home kitchen only for food not needing temperature control, if allowed by law, with a placard saying the kitchen is "not subject to regulation and inspection".
     - In 2021, 5.8% of US children aged 0–17 had a food allergy, per CDC.
     - FDA says reactions can involve "severe, life-threatening symptoms, often called anaphylaxis".
     - The allergen duty varies. Illinois recommends labels. Australia requires a declaration on request or on display. The UK has no legal duty for unregistered events but encourages allergen information.
   - Fix: replace step 4 with the curated food rules, including "no card, no sale".

3. **R3. Nothing limits cake type.** (major) `verified` for the rules; which rule binds this event is unknown · `converged`
   - Evidence: Illinois: "Pumpkin, sweet potato, custard, and cream fillings are NOT allowed." Nova Scotia does not allow "Cakes or pies that contain cream, cheese, egg, or pudding filling". Kansas State Extension bars selling home-baked foods needing refrigeration, including "cream cheese-based frostings or fillings", without a licence. The UK allows cheesecake and fresh-cream desserts out of the fridge only "for the shortest time possible, ideally not longer than 4 hours".
   - Fix: only cakes that need no fridge, and refuse anything else at the table.

4. **R4. No approval, owner or path for the money.** (major) `verified` as absent · `converged`
   - Evidence: the four steps name no approver, organiser, cash handling or handover to the library.
   - Fix: written approval, a named organiser and treasurer, two people counting, and a published total (curated steps 1 and 7).

5. **R5. Local food rules and school rules are unchecked.** (major) `verified` that the clauses exist; whether they apply here is unknown · `unique`, from the food-safety seat
   - Evidence: exemptions are conditional. Illinois covers goods sold by "a religious, charitable, or nonprofit organization for fundraising purposes". FSANZ says "Food has been 'sold' even if you just ask for a donation". Ontario's school food policy covers "all events (e.g., bake sales, sports events)" and limits most cakes, unless they meet its nutrition criteria or fall on a principal-designated special-event day.
   - Fix: ask the school and the local health office in writing before announcing (curated step 1).

6. **R6. One day's notice undercuts even the $500.** (major) `plausible` · `converged`
   - Evidence: step 3, "the day before". Advice elsewhere is one to two weeks, but it is practitioner opinion and no study was found. It also leaves no time for the checks in R5.
   - Fix: notices three weeks, one week and the day before, with pre-orders.

7. **R7. A Saturday gate has no named crowd.** (major) `plausible` · `converged`
   - Evidence: step 2 names no event, and selling 50 cakes needs one sale every 2.4 minutes. The school's Saturday footfall is unmeasured.
   - Fix: hold the sale alongside something that already brings families. If nothing does, bake to pre-orders.

## Should change

1. **Ask the school for its past fundraiser totals.** Effort: small. They beat every outside number here.
2. **Ask the librarian for a priced book list.** Effort: small. It confirms the sum and shows what a smaller total still buys.
3. **Count baker sign-ups before promising 50 cakes.** Effort: small. It is the cheapest test of whether 50 cakes exist.

## Could change

- Sell wrapped slices as well as whole cakes. This may raise more, but it adds food handling.
- Add a "sponsor a book" bookplate, or a thermometer showing progress. The $25 bookplate price a seat suggested is untested.
- Try a sponsored read in place of the sale in a later year. The only large figure found comes from a vendor and shows no method.

## Keep

- **The purpose.** "So the library can buy new books" is concrete and easy to repeat.
- **Plain cakes.** Illinois, Nova Scotia and Australia all allow cakes without cream-type fillings, so the product can stay.
- **Explicit numbers.** The plan states its price, count and hours, which is why the error could be found at once.
- **Low commitment.** There is almost no cash at risk, and the plan can change freely until it is announced.

**Conflict with the fixes:** the Steelman seat asked to protect the plan's four-step simplicity. The curated plan has seven steps, because approval, food rules and money need an owner. The goal also no longer rests on one Saturday. The food rules and step 1 are the parts not to cut.

## Curated version

**Status:** checked twice by fresh contexts.
- The first check found a timeline that could not be followed and no way to collect donations. Both were fixed.
- The second check rated all seven must-change items resolved, but found gaps in the failure branches.
- Those gaps were then closed with small wording changes, and this final wording has not been re-checked.
- Remaining limits: the lead times, the 10-family test and the $1,500 trigger are judgement calls, not evidence. At $50 a family, the trigger needs about $333 each from the three businesses.

The original `plan.md` was not changed.

```markdown
# Book drive and bake sale for the school library

Goal: pay for the library's book list, about $5,000 (confirm the figure with the
librarian). Donations carry most of the sum. The bake sale on one Saturday brings
families together, closes the drive and adds up to $500.

Figures: 50 cakes × $10 = $500 if every cake sells. The other $4,500 comes from
donations and sponsors, for example 90 gifts of $50 or 225 gifts of $20. These are
targets to test, not promises. Lead times and the check in step 2 are judgement
calls; adjust them to your school.

1. Get permission first (about 7 weeks before). Pick a Saturday when something
   already brings families to the school (a match, fair or open day). It is also
   the drive's last day. Ask the head or parent association to approve the drive
   and the sale in writing, and to name one organiser and a treasurer. Email the
   school and the local health office or council with the date, place, who is
   selling and the plan to sell plain cakes that need no fridge. Ask whether a
   permit, registration or sign is needed, whether the gate counts as school
   premises, and whether school food rules allow these cakes. If nobody replies
   in a week, phone. Announce nothing until the school has replied.
   - Permit or sign needed: get it before going on.
   - Cakes not allowed, a permit refused or late, or no answer from the office by
     3 weeks before: run the drive without cakes, so donations must cover the full
     sum.
   - Approval refused: stop.
2. Test the money quietly (about 5 weeks before). Ask the librarian for a priced
   book list. Ask 10 families and 3 local businesses what they would give. If they
   indicate less than about $1,500 (a rule of thumb), ask the librarian which books
   to drop, and announce the price of the books that remain.
3. Ask parents to bake (3 weeks before). Use a sign-up sheet for up to 50 named
   cakes, following the food rules in step 6. The cake is the baker's donation.
   Offer "or give the price of a cake instead".
4. Announce and collect. Newsletter notices three weeks, one week and the day
   before. The treasurer sets a way to give that the school approves. One named
   person follows up the sponsors. The organiser takes cake pre-orders, only up to
   the number of cakes signed up; buyers pay and collect at the table.
5. Sell. Sell at the gate while the crowd is there, at $10 a cake. If no Saturday
   has a crowd, sell from 9 to 11 am: the organiser closes pre-orders a week before
   and tells bakers how many to make, which is the pre-orders plus a few. Use a
   covered table, with food off the ground. Keep two people at the table: one for
   food, one for money. Near the end, sell unsold cakes cheaply or give them away.
6. Food rules. Homemade food needs care: it comes from home kitchens, and it
   carries no label unless you add one.
   - Only cakes that need no fridge. No fresh cream, custard, cheesecake or
     cream-cheese frosting. Local rules win where they are stricter.
   - Each cake is wrapped and carries a card with its name, full ingredients and
     allergens, plus "made in a home kitchen that may contain other allergens".
   - No card, no sale.
   - The organiser keeps a list of who baked what, with a phone number and the
     bake date.
   - Nobody bakes if they, or anyone at home, are ill.
   - Volunteers read the card aloud. They never tell a buyer a cake is safe for
     someone.
7. Money. Two people count the cash and sign the total. It goes to the treasurer
   the same day, with a receipt. The treasurer pays for the books on the list; if
   the total falls short, the librarian chooses which. Publish the total and the
   books it bought.
```

**Changelog**

| Change | Finding |
|---|---|
| New goal, and figures showing the $4,500 gap | R1, objective challenge |
| Step 1: approval, owner, rule checks | R4, R5 |
| Step 2: quiet money test and book list | R1, objective challenge |
| Step 3: sign-up, and the option to give instead of baking | R8 |
| Step 4: earlier notices, a way to give, pre-orders | R6, R1 |
| Step 5: chosen crowd, and baking to pre-orders if there is none | R7 |
| Step 5 table setup, step 6 baker list and illness rule | R10 |
| Step 6: replaces the false statement; adds cake limits and cards | R2, R3 |
| Step 7: cash handling and route to the books | R4 |

## Dissent register

- **Is step 4 a blocker or a major?** Four seats said blocker, two said major. Both contention agents ended at major, at about 75% confidence, including the one assigned to argue blocker. It changed position on the fatality rate. Ruled major, because the scale reserves blocker for harm that occurs, and fatal food anaphylaxis is rare: about 3.25 per million person-years in food-allergic under-20s.
  - *For blocker:* a foreseeable, unmanaged risk to a child conflicts with "nobody is harmed", and no per-sale data exists to show it is small.
  - The fix is required either way, so this does not change the verdict.
- **Can a direct appeal work here?**
  - *For:* it is the only option examined with a plausible route to $5,000, and it carries no food risk.
  - *Against:* it can tire or pressure families, is too heavy for a small school, and the evidence that it beats other fundraisers is anecdotal and mixed.
  - Unresolved, because school size is unknown. Curated step 2 tests it.

## What would change this verdict

- **The librarian needs far less than $5,000.** R1 shrinks, and a fixed sale alone may be enough. Cheapest test: ask the librarian.
- **The school's own sales have taken several thousand dollars.** Larger targets become credible. Search summaries mentioned community events of about $5,000 and $12,000, but no seat opened them, and they had a different structure. Cheapest test: ask the school for past totals.
- **Local or school rules bar home-baked sales.** The cake sale is a no-go, and only the drive remains. Cheapest test: one email each to the school and the local health office.

**Pre-mortem:** If this fails in 12 months, the most likely reason is that the sale went ahead as a bake sale alone, sold well and still left the library $4,500 short after $5,000 had been announced.

## Dimension assessment

| Correctness | Fit | Risk | Cost/simplicity | Execution | Stakeholders | Outside view |
|---|---|---|---|---|---|---|
| unsound: the sum and step 4 are both wrong | weak: at most 10% of the goal | material: harm is rare but can be severe; the plan can change until announced | lean: the plan is too thin, not bloated | poor: clear, but no owner, money path or checks | with reservations: bakers and allergic families bear the unaddressed costs | ignores: no comparable school sale found near the target |

<details><summary>Finding registry and process notes</summary>

| ID | Finding | Seats | Class | Severity | Status | Evidence |
|---|---|---|---|---|---|---|
| R1 | Sell-out raises $500, not $5,000 | 6 of 6 | convergent | blocker | verified | Computed by the Chair and the fresh verifier |
| R2 | Step 4 false; no allergen information | 6 of 6 | convergent; severity contested | major | verified, likelihood unmeasured | Food Code, CDC, FDA, Illinois, FSANZ, gov.uk |
| R3 | No limit on cake type | food safety; others in their fixes | convergent | major | verified | Illinois, Nova Scotia, Kansas, gov.uk |
| R4 | No approval, owner or money path | 6 of 6 | convergent | major | verified as absent | The plan's four steps |
| R5 | Local and school rules unchecked | food safety | unique | major | verified clause, applicability unknown | Illinois, FSANZ, Ontario PPM 150 |
| R6 | One day's notice | 6 of 6 | convergent | major | plausible | Step 3; PTO Today (opinion) |
| R7 | No named crowd at a Saturday gate | 5 of 6 | convergent | major | plausible | Step 2; footfall unmeasured |
| R8 | Bakers' ingredient cost uncounted | 3 of 6 | convergent | minor | speculative | Seats' estimates only |
| R10 | No baker list or handling basics | food safety | unique | minor | verified | Nova Scotia, Illinois |

R9 was merged into the objective challenge (the $5,000 has no stated source).

**Comparable sales, not a representative sample:**
- Oldfield primary PTA: £315.69, for a theatre contribution.
- Anthony Curton school, for library books: £300.
- Publicised Los Angeles food-blogger sale, 2010, about 50 bakers and 19 volunteers: $2,456.50.

No seat found a national average, or a single school reaching several thousand dollars from a one-day bake sale. That is absence of evidence, not proof.

**Contention:** step 4 severity, one round. Outcome above. Both per-event risk figures produced were illustrative, using an arbitrary multiplier, and are not quoted as risks. A seat's search found no outbreak traced to a school bake sale; those searches were shallow and such events may go unreported.

**Verification:** a fresh verifier checked 12 items and refuted none. It saw most quotes in page text fetched directly. Corrections carried into this report:
- Ontario's rule is not a blanket ban on cakes.
- Australia's allergen duty can be met on request.
- The UK wording covers cheesecake and fresh-cream desserts.

Live pages blocked: CDC Data Brief 459 and PTO Today were read through archive copies (January and May 2025). The PTO Today advice comes from a timeline for packet-based fundraisers, not bake sales. The fatality rate was opened by a contention agent and not re-checked by the verifier.

**Not verified:** jurisdiction, school size, past totals, Saturday footfall, willing bakers, willingness to pay, school policy and the source of the $5,000. No rate of illness or reaction per bake sale was found. None of these was checked with the school, since the request was to ask nothing and nothing was sent anywhere.

**Limits and signs of collapse:** all seats shared one model family. R1 and the fixes for R4 and R6 were near-identical across seats, which is expected for plain arithmetic and missing items, so they count as one voice on the facts. The material holds no personal data, and seats were told to search only general questions.

**Sources**
- [Illinois DPH bake-sale guidelines](https://dph.illinois.gov/topics-services/food-safety/retail-food/guidelines-for-bake-sales.html)
- [Kansas State Extension MF3382](https://bookstore.ksre.ksu.edu/download/food-handling-guidelines-for-bake-sales_MF3382)
- [FDA Food Code 2022](https://www.fda.gov/files/food/published/FDA-FoodCode2022-FullDocument-01182023_0.pdf), ¶1-201.10(B)
- [FDA food allergies](https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies)
- [CDC Data Brief 459, archive copy](https://web.archive.org/web/20250103112758/https://www.cdc.gov/nchs/products/databriefs/db459.htm)
- [UK: providing food at community and charity events](https://www.gov.uk/government/publications/providing-food-at-community-and-charity-events/providing-food-at-community-and-charity-events)
- [Nova Scotia bake-sale guidelines](https://www.novascotia.ca/sites/default/files/documents/1-4220/bake-sales-guidelines-en.pdf)
- [FSANZ charities](https://www.foodstandards.gov.au/business/charities) and [labelling factsheet](https://www.foodstandards.gov.au/business/safety/factsheets/charitiesandcommunityorganisationsfactsheets/labellingseptember)
- [Ontario PPM 150](https://www.ontario.ca/document/education-ontario-policy-and-program-direction/policyprogram-memorandum-150)
- [Umasunthar 2013, fatal anaphylaxis](https://pmc.ncbi.nlm.nih.gov/articles/PMC4165304)
- [PTO Today, archive copy](https://web.archive.org/web/20250523215227/https://www.ptotoday.com/pto-today-articles/keys-to-fundraising-success)
- Comparables: [Oldfield](https://www.oldfield.cheshire.sch.uk/work/pta-bake-sale/76948), [Anthony Curton](https://www.fenlandcitizen.co.uk/news/bake-sale-brings-300-book-boost-for-anthony-curton-school-9302699), [Los Angeles](https://www.lafujimama.com/national-food-blogger-bake-sale-los-angeles-recap/)

</details>
