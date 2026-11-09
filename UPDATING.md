# Weekly update instructions

`cases.json` feeds the STL Self-Defense Cases phone widget. The phone downloads it once a week.

## Each week
1. Search St. Louis–area local news (St. Louis City, St. Louis County, St. Charles County, and the Metro East in Illinois) for:
   - new cases where someone claimed self-defense in a shooting, stabbing or other use of force;
   - outcome changes in cases already listed (charges filed or declined, dismissed, verdicts, pleas, sentences).
   Useful outlets: STLtoday (Post-Dispatch), KSDK, KMOV / First Alert 4, FOX 2 (KTVI), St. Louis Public Radio, Riverfront Times.
2. Only include facts from the articles. Each case needs at least one https source link.
3. Do not name anyone who was not charged (victims, witnesses, shooters who were cleared). Name a person only if they were charged.
   When an article names someone who was not charged, add their name to `UNCHARGED` in `validate.py`.
4. Field rules (every field is required text):
   - `id`: short unique slug, e.g. `soulard-2026`
   - `date`: month the case was reported or last changed, e.g. `Aug 2026`
   - `area`: neighborhood or town, plus "St. Louis City" / "St. Louis County" etc.
   - `title`: short headline, no names
   - `outcome`: short status, e.g. "No charges filed", "Guilty of first-degree murder", "Decision pending when last reported"
   - `kind`: `cleared` (no charges, dismissed, not guilty), `convicted`, `mixed`, or `open` (pending/unconfirmed)
   - `happened`, `claim`, `ended`, `note`: a few plain sentences each; `note` says "Status as of <date>" and any caveats
5. Order: newest first. Keep the list to about 25 cases; drop the oldest settled ones if it grows past that.
6. Set top-level `checked` to today's date in the form `Nov 9, 2026`, even if no cases changed.
7. Run `python3 validate.py`. Fix everything until it prints ALL PASS. Never commit a file that fails.
8. Commit to `main` and push.
