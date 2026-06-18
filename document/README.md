AromaType — personalised fragrance recommendations through style, situations and feelings

[![Lychee Link Checker](https://github.com/AromaType/AromaType/actions/workflows/links.yml/badge.svg)](https://github.com/AromaType/AromaType/actions/workflows/links.yml/badge.svg)

AromaType is a service (Telegram Mini App or web version) for people who want to choose a good fragrance for themselves but do not want to deal with notes, families and perfume terminology.

Instead of the complex language of perfumers, we ask simple questions about lifestyle, situations, weather, habits and comfortable scent projection. Based on the answers, we form a personal fragrance profile (similar to a colour type) and select 3–5 samples with a clear explanation of why this scent suits you.

> Key idea: "fragrance colour type" — the product does not define appearance, but rather style, situations, comfortable level of projection and the feelings a person wants to convey through a scent.

---

Live project links

| Resource | Purpose | Link |
|----------|---------|------|
| Linear | Task and sprint management | [Go to](https://linear.app/swparomatype/join/8444b54d83af6d701b023c1df7094fdc?s=0) |
| Telegram | Team and client communication | [Join](https://t.me/+agyc9ZEMXPllZGQy) |
| Google Drive — interview recording | Client interview (NeuroLife) | [Open](https://drive.google.com/file/d/1oQkldtjC-fiSvReJBSpMnhUVDrycb0G-/view?usp=sharing) |
| Google Sheets — fragrance database | Prepared database for recommendations | [Open](https://docs.google.com/spreadsheets/d/14y3d7_gdY5NgMnxHO8ARMQP4fTi-kFqYeAPke0S0kU8/edit?usp=sharing) |
| AI Studio — prompt prototype | Testing LLM for profile generation | [Open](https://ai.studio/apps/c97d1f4b-a8db-4057-9653-624620cbdcae) |
| Google Drive — full report | Assignment 1 (interview, analysis, MVP scope) | [Open](https://drive.google.com/file/d/1KfurtcC5zIDHHads_lCB881UfvJR90pC/view?usp=sharing) |

---

What is included in MVP (version 1)

Included in MVP

- Dialogue survey (5–7 questions): style, situations, weather, habits, budget, comfortable scent projection.
- Fragrance profile generation: LLM processes responses and creates a personal profile.
- Selection of 3–5 fragrances from the prepared database.
- Fragrance cards with explanations:
  - When to wear
  - Character of the fragrance
  - How noticeable it is
  - Why it was chosen for you
- Plain language explanation — without perfume terminology.
- Transition to ordering a sample set.
- Saving the profile and feedback after the test.

Deferred / out of scope for MVP

- Admin panel for managing the fragrance database
- Recommendation history for unregistered users (profile is saved, but full history comes later)

---

Role of AI (LLM)

AI does not magically guess and does not train an ML model from scratch. Its tasks:

1. Ask the right questions (using Mom Test methodology).
2. Translate user responses into a structured fragrance profile.
3. Explain the selection — why each fragrance fits the user's style and situations.

Uses LLM API (basic prompt available in AI Studio via link above) + prepared fragrance database (Google Sheets).

---

Local setup (development)

Requirements

- Node.js 20+ / Python 3.11+ (choose based on stack)
- Git
- Access to LLM API (key — in .env)

Installation

git clone https://github.com/your-org/aromatype.git
cd aromatype

Environment configuration

cp .env.example .env
# Add API keys and settings

Run (example for Node.js)

npm install
npm run dev

Link check (Lychee)

lychee --verbose './**/*.md'

---

Monorepo structure

aromatype/
├── src/               # Source code (Telegram Mini App / web)
├── docs/              # Technical documentation
├── reports/           # Team reports (including Assignment 1)
├── api/               # API artifacts (OpenAPI, request examples)
├── artifacts/         # Other artifacts (prototypes, diagrams)
├── LICENSE            # MIT
├── README.md          # This file
├── .gitignore
├── .env.example
├── ATTRIBUTION.md     # Attribution of third-party assets
└── .github/           # PR templates, CI/CD

---

Team

| Name | Role |
|------|------|
| Nikita Ionov | Team Lead / Frontend Developer |
| Danil Lebedev | Frontend Developer (UI / Layout) |
| Polina Yakovleva | Backend Developer |
| Matvey Gerasimov | Backend & AI Developer |
| Madina Valetova | Design / Reporting |

---

License

All content created by the team is distributed under the MIT license (see LICENSE file).

Third-party assets (if any) — see ATTRIBUTION.md.

---

Related documents

- Full report (Assignment 1) — Google Drive
- Fragrance database (Google Sheets)
- Prompt prototype in AI Studio
- Client interview recording
- Linear Board
- Team Telegram chat

---

Important for development

- The main branch is protected: direct push is prohibited, only PR with approval from another team member.
- CI checks links (Lychee) for all .md files.
- No secrets in code — only .env.example, real keys — locally or in CI secrets.
- All changes (even documentation) — via Pull Request.

---

AromaType — making fragrance selection understandable, human and accessible. Questions or suggestions — in the team Telegram chat.

```bash
git clone https://github.com/your-org/aromatype.git
cd aromatype
