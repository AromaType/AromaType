Summary of Changes
(What does this PR implement?)

Example:
- Added survey questions for style, situations, weather
- Integrated LLM API for profile generation
- Created fragrance recommendation cards

Related MVP Feature
- [ ] Short dialog survey (style, situations, weather)
- [ ] Personal fragrance profile generation
- [ ] Recommendation from fragrance database
- [ ] Plain language explanation for each recommendation
- [ ] Fragrance cards (when to wear, character, sillage, why chosen)
- [ ] Sample kit order link
- [ ] Profile saving and feedback storage

Testing Performed
- [ ] Survey flow tested manually (5-7 questions)
- [ ] LLM generates profile without "magic guessing"
- [ ] Recommendations include explanations in plain language
- [ ] All links work (checked by Lychee CI)

Reviewer Checklist
- [ ] Does the survey ask about lifestyle, NOT perfume notes?
- [ ] Are recommendations explained in beginner-friendly language?
- [ ] Does AI only translate answers, not guess randomly?
- [ ] No hardcoded secrets (.env not committed)
- [ ] Documentation updated if needed

Incident Notes (if any)
(Delete if not applicable)
- [ ] No secrets were committed
- [ ] No personal data exposed
- [ ] No real client fragrance database published
