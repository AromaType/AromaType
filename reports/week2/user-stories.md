User Stories - AromaType Week 2

Context from Customer Interview (Week 1)

Based on the interview with Mark (NeuroLife) on June 4, 2026:

- No existing MVP: "No, there is nothing at all. The project will be built entirely from scratch by you."
- Platform preference: "Telegram is likely the more natural channel — it will probably be easier to reach the audience there."
- Design freedom: "There was no brand book before. You can develop whatever style you want independently."

Competitive Gaps Addressed

Analysis of Scentbird, Fragrantica, Parfumo, Perfumist, and FragranceX.com revealed:

| Gap | AromaType Response |
|-----|-------------------|
| No lifestyle questions | US-01 asks about style, situations, weather |
| Complex perfume terminology | US-01, US-03 use plain language only |
| No explanation of recommendations | US-03 includes "why this scent suits you" |

---

Active User Stories

US-01: Complete fragrance survey

Requirement status: Active
MoSCoW priority: Must Have

As a user who doesn't understand perfume terminology,
I want to complete a short dialog survey about my lifestyle, style, and situations,
so that I can receive personalized fragrance recommendations without learning about perfume notes.

Notes and constraints
- Survey questions based on lifestyle, NOT perfume notes (addressing Gap 2)
- 5-7 questions maximum (client preference)
- Topics: style, situations, weather, habits, budget, sillage preference
- No terminology like "bergamot", "vetiver", "patchouli"
- Format: multi-step dialog (Telegram Mini App native style)

---

US-02: Receive fragrance profile

Requirement status: Active
MoSCoW priority: Must Have

As a user,
I want to receive a personal "fragrance profile" based on my survey answers,
so that I understand what kind of scents generally suit me.

Notes and constraints
- Profile describes: style match, recommended sillage, suitable occasions
- Plain language only
- Inspired by "fragrance color type" concept from project description
- LLM processes survey responses to generate profile

---

US-03: Get fragrance recommendations with explanations

Requirement status: Active
MoSCoW priority: Must Have

As a user,
I want to see 3-5 fragrance recommendations with plain-language explanations,
so that I understand why each scent suits me.

Notes and constraints
- Each recommendation includes: name, when to wear, character, sillage level
- Explanation must answer "why this scent suits you" (addressing Gap 3)
- No "magic guessing" — AI translates answers, not random selection
- LLM API (OpenAI or Yandex GPT) generates explanations
- Matches against prepared fragrance database

---

US-04: View fragrance cards

Requirement status: Active
MoSCoW priority: Must Have

As a user,
I want to see visual fragrance cards with key information,
so that I can quickly compare recommendations.

Notes and constraints
- Cards include: name, description, sillage indicator, occasion badge
- Mobile-friendly design for Telegram Mini App
- Visual elements decided by team (no brand book constraints)

---

US-05: Order sample kit

Requirement status: Active
MoSCoW priority: Must Have

As a user,
I want to click a link to order a sample kit with my recommended fragrances,
so that I can try them before buying full bottles.

Notes and constraints
- Link to external marketplace (potential partner: FragranceX.com identified in competitive analysis)
- MVP can use placeholder link
- No checkout integration required for MVP

---

US-06: Save profile and get future recommendations

Requirement status: Active
MoSCoW priority: Should Have

As a user,
I want to save my fragrance profile,
so that I can get updated recommendations later without retaking the survey.

Notes and constraints
- Explicitly deferred from MVP scope in project description
- Requires database and user authentication
- Target: V2 or later

---

US-07: Share results with friends

Requirement status: Active
MoSCoW priority: Could Have

As a user,
I want to share my fragrance profile or recommendations with friends,
so that we can discuss and compare.

Notes and constraints
- Telegram share integration (natural for Mini App)
- Low priority for MVP
- Customer did not request this feature

---

US-08: Provide feedback on recommendations

Requirement status: Active
MoSCoW priority: Could Have

As a user,
I want to rate or provide feedback on recommended fragrances,
so that the system improves future recommendations.

Notes and constraints
- Feedback can refine LLM prompts
- Simple like/dislike sufficient for V1
- Customer did not explicitly request; team-proposed improvement

---

US-09: Admin manage fragrance database

Requirement status: Active
MoSCoW priority: Should Have

As an admin,
I want to add, edit, or remove fragrances from the database,
so that the recommendation catalog stays up to date.

Notes and constraints
- Explicitly out of MVP scope in project description
- Initial database prepared by team (open sources or client-provided)
- Admin UI deferred to V2
- MVP uses direct database access or JSON file

---

Initial proposed MVP v1 scope

Based on customer interview and project description constraints:

Selected Must Have stories (MVP v1):

| ID | Title | Notes |
|----|-------|-------|
| US-01 | Complete fragrance survey | 5-7 lifestyle questions |
| US-02 | Receive fragrance profile | LLM-generated |
| US-03 | Get recommendations with explanations | 3-5 scents |
| US-04 | View fragrance cards | Visual comparison |
| US-05 | Order sample kit | External link |

Total: 5 stories

Deferred to V2 or later:

| ID | Title | Priority | Reason |
|----|-------|----------|--------|
| US-06 | Save profile | Should Have | Explicitly deferred in project description |
| US-07 | Share results | Could Have | Not requested |
| US-08 | Provide feedback | Could Have | Nice to have |
| US-09 | Admin database | Should Have | Explicitly out of MVP scope |

---

Removed stories

US-10: Voice input for survey

Requirement status: Removed
Previous MoSCoW priority: Could Have

As a user,
I want to answer survey questions using voice input,
so that I can complete the survey hands-free.

Reason: Voice input adds significant complexity (speech recognition, async processing) and is not essential for the core value proposition. Users can type answers easily in Telegram. Removed to focus on text-based MVP. No customer request for this feature.

---

US-11: Augmented reality try-on

Requirement status: Removed
Previous MoSCoW priority: Won't Have

As a user,
I want to see how a fragrance bottle would look on my shelf using AR,
so that I can visualize the product.

Reason: AR functionality is far outside the current scope. Requires complex 3D rendering and mobile AR frameworks. Customer explicitly excluded similar "nice to have" features during interview. Removed.

---

US-12: Web version alongside Telegram Mini App

Requirement status: Removed
Previous MoSCoW priority: Could Have

As a user,
I want to use AromaType on a web browser instead of Telegram,
so that I can access recommendations without installing Telegram.

Reason: Customer explicitly stated: "Telegram is likely the more natural channel — it will probably be easier to reach the audience there." Team decision to focus on Telegram Mini App only for MVP. Web version may be reconsidered for V2 if needed.

---

Story ID Summary

| ID | Status | Priority |
|----|--------|----------|
| US-01 | Active | Must Have |
| US-02 | Active | Must Have |
| US-03 | Active | Must Have |
| US-04 | Active | Must Have |
| US-05 | Active | Must Have |
| US-06 | Active | Should Have |
| US-07 | Active | Could Have |
| US-08 | Active | Could Have |
| US-09 | Active | Should Have |
| US-10 | Removed | (was Could Have) |
| US-11 | Removed | (was Won't Have) |
| US-12 | Removed | a(was Could Have) |

Total active stories: 9
Total removed stories: 3
Must Have for MVP v1: 5
