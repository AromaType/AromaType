ATTRIBUTION

Third-Party Resources and Components

Media and Branding

| Element | Source | Owner | License | Usage |
|---------|--------|-------|---------|-------|
| Client Logo | Provided by customer | LLC "AromaType" | Not subject to MIT | Used with written permission. Distribution outside the project is prohibited. |
| Fragrance Images | Perfume database (prepared) | LLC "AromaType" | Not subject to MIT | Trademarks and packaging belong to their respective owners. Used for demonstration purposes only in MVP. |

AI and LLM Components

| Component | Source | License | Usage |
|-----------|--------|---------|-------|
| LLM API | OpenAI / GPT-4 or Yandex GPT / Yandex Cloud | Provider's own license | Processing user responses, translating into fragrance profile, generating human-readable explanations of recommendations. API keys are stored in environment variables (.env) and are not included in the repository. |
| Prompt Engineering Templates | Team's own development | MIT (code templates only) | Structured requests to LLM for surveys, style analysis, and generation of personalized selections. |

Dependencies (managed via package.json / requirements.txt)

Regular dependencies do not require entries in this file. See package manifests for full list:

Backend / Python:
- fastapi, uvicorn — web framework (MIT/BSD license)
- openai / yandexcloud — SDK for LLM API (provider licenses)
- pydantic — data validation (MIT license)
- python-dotenv — environment variable management (BSD license)

Frontend / Telegram Mini App:
- react or vue — UI framework (MIT license)
- @telegram-apps/sdk — Telegram integration (MIT license)

Fragrance Database

| Component | Source | License | Usage |
|-----------|--------|---------|-------|
| Prepared Fragrance Database | Collected by team / provided by client | Not subject to MIT | Contains perfume names, brands, characteristics (sillage, season, style). Client's commercial information. Stored separately; repository contains only schema and test data. |

Test Data for Public Repository

| File | Content | Status |
|------|---------|--------|
| src/data/sample_perfumes.json | 5-10 demo fragrances with fictional names | Cleaned, no real brands |
| src/prompts/profile_builder.txt | Prompt templates (anonymized) | Can be published |
| .env.example | Environment variables (no real keys) | Can be published |
| reports/ | Project reports | Can be published |

Important Restrictions

1. LLM API keys are never committed to the repository. Use .env (ignored by git).
2. Client's real fragrance database is not published. Repository contains only schema and anonymized examples.
3. AromaType logo and branding are not distributed under the MIT license.
4. User personal data (survey results) is not stored in the repository or published.

License for Team Code

All source code written by the team (survey logic, profile logic, LLM integration, Telegram Mini App) is distributed under the MIT license (see LICENSE file).

---
Last updated: June 14, 2026
For attribution inquiries: Neurolife

