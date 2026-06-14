Customer Meeting Summary - AromaType Week 2

Meeting 1: Introductory Meeting (Online)

Date: June 4, 2026
Time: 12:00
Format: Online (Yandex Telemost)
Participants: Mark (NeuroLife), AromaType Team (Nikita, Danil, Polina, Matvey, Madina)

Team Roles During Interview
- Interviewer: Nikita Ionov — led the conversation and asked all prepared questions
- Note-taker: Nikita Ionov — captured key responses
- Observers: Remaining team members attended to gain first-hand context

Meeting Objective
To clarify the basic parameters of the project without imposing the team's own ideas — in order to receive honest answers rather than validation of pre-formed hypotheses.

Core Discovery Questions (Mom Test principles applied)
1. "Is there anything already prepared for the project that you can provide to the team?"
2. "The project description mentions a choice between Telegram Mini App and a web version - what is your preference and why?"
3. "Are there any examples of applications you like in terms of style, or is the design entirely up to the team?"

Key Answers from Customer
- "No, there is nothing at all. The project will be built entirely from scratch by you."
- "Telegram is likely the more natural channel — it will probably be easier to reach the audience there."
- "You have more expertise — choose whichever you prefer, because both options work well overall."
- "There was no brand book before. You can develop whatever style you want independently."

Methodological Adjustments (The Mom Test)
1. Ask about facts, not opinions
2. Do not pitch ideas in advance
3. Open questions without suggested answer

Question Improvements
| Flawed/Biased Question | Improved Mom-Test Question |
|------------------------|---------------------------|
| "What features are most important for the project?" | "Is there anything already prepared for the project that you can provide to the team?" |
| "Is it definitely Telegram Mini App, or do you also need a web version?" | "Do you have a platform preference — Telegram Mini App or web? Why?" |
| "Do you have a brand book, logo, colours — or is the design up to us?" | "Are there any applications you like in terms of style, or is the design entirely up to the team?" |

Decisions Made
- Platform: Telegram Mini App (customer preference, team has final choice)
- Design: Full freedom for the team
- MVP: Built entirely from scratch, no existing technical base

Wrap-Up & Next Steps
- Full meeting scheduled for Monday to discuss product details in depth
- Communication channel agreed for ongoing design approval (direct messages to client)

---

Meeting 2: Full Team Meeting (In-person)

Date: June 8, 2026
Time: 19:00
Location: Room 101, Innopolis University
Format: In-person
Participants: Mark (NeuroLife), Full AromaType Team

Meeting Agenda
- Present products and project plans for the semester
- Introduce what team will work on during the semester
- Get to know each other in informal setting
- Answer any questions before development starts
- Pizza 🍕

Discussion Points
- Project functionality overview for Assignment 2
- Feedback on project approach and explanation
- Technical discussions
- Database architecture and requirements
- LLM API integration planning

Key Outcomes
- Customer provided feedback on proposed project direction
- Technical specifications discussed
- Database structure requirements clarified
- Positive reception of the "fragrance color type" concept

---

Meeting 3: Technical Review

Date: June 11, 2026
Time: 13:00
Format: Online
Participants: Mark (NeuroLife), Backend/AI team members

Technical Topics Discussed
- Database design and architecture
- LLM API selection (OpenAI or Yandex GPT)
- Integration approach for recommendation engine

Pending Clarifications (from Assignment 1)
1. Fragrance dataset: Will the client provide a ready-made dataset, or will the team compile it independently? Which attributes are required: notes, family, brand, price, longevity?
2. LLM API: Which AI service is preferred? Does the client provide API access or a budget, or will the team use a free tier independently?
3. MVP feature priorities: Validate and align preliminary MVP scope — confirm must-have features and explicit boundaries between V1 and V2
4. Communication format: How often should the team sync with the client? What format is preferred for progress updates (demos, screenshots, test build)?

Technical Decisions (Proposed by Team)
- Backend: Python/FastAPI
- Database: PostgreSQL for production, SQLite for development
- LLM: OpenAI GPT or Yandex GPT (to be decided)
- Frontend: Telegram Mini App (React/Vue)

---

Competitive Analysis Summary (5 Existing Solutions)

| Product | Key Limitation |
|---------|----------------|
| Scentbird | No lifestyle context |
| Fragrantica | Expert-level language, no personalisation |
| Parfumo | Note-based language, no lifestyle filtering |
| Perfumist | Based on favourite perfumes, not lifestyle |
| FragranceX.com | No personalisation, outdated interface |

Identified Gaps & Opportunity for AromaType
- GAP 1: No lifestyle/mood/weather questions in existing products
- GAP 2: Complex terminology creates barrier for beginners
- GAP 3: No explanation why a fragrance is recommended

AromaType Opportunity: Telegram Mini App combining lifestyle-based survey, visual recommendation cards, and plain-language explanations.

---

MVP v1 Scope (Proposed)

Core Included Features (Must Have)
- User questionnaire: multi-step survey (5-7 questions) covering lifestyle, occasions, scent intensity, budget
- Profile generation: LLM processes survey responses
- Fragrance matching: 3-5 personalised recommendations
- Recommendation cards with plain-language explanation

Explicitly Deferred / Out of Scope
- User account and history (deferred to V2)
- Admin panel (out of MVP scope)

---

Customer Approvals Obtained

| Item | Status | Evidence |
|------|--------|----------|
| Public MIT-licensed development | ✅ Approved | Written consent via Telegram, June 7, 2026 |
| User stories and priorities | ✅ Approved | Meeting 2 (June 8, 2026) |
| Initial proposed MVP v1 scope | ✅ Approved | Meeting 2 (June 8, 2026) |
| Platform choice (Telegram) | ✅ Confirmed | Meeting 1 (June 4, 2026) |

---

AI/LLM Utilization Disclosure (Week 1)
- Claude (Anthropic) used for:
  - Generating interview transcript from recording
  - Providing overview of Mom Test framework
  - Structuring and compiling team report

Refinement Strategy: All AI-generated materials were reviewed and revised by team to reflect actual project data.

---

Action Points for Week 3

| Action | Owner | Deadline |
|--------|-------|----------|
| Finalize database schema | Polina | Week 3 |
| Set up LLM API integration | Matvey | Week 3 |
| Create Telegram Mini App skeleton | Nikita, Danil | Week 3 |
| Complete prototype design | Madina | Week 3 |
| Compile fragrance database | All | Week 3 |
