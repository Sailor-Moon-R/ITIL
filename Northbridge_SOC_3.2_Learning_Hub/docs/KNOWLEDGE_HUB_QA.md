# Northbridge SOC 3.2 — Knowledge Hub QA summary

Built 18 October 2026.

## Passed in automated Chromium or programmatic checks

- 15 complete explanatory topics using the source presentation's sequence, with 42 genuine application-task links.
- Local Estio logo, screenshot files, CSS and JS available via HTTP server.
- Knowledge Hub launches and displays every topic and the first introductory page.
- Concept search, optional visual diagrams, evidence interpretation selector, impact/urgency selector, next/previous navigation, theme, reading mode and font adjustment.
- Responsive mobile rendering and keyboard-operable native controls.
- Educational agreement and deep-link task selection tested with released application scripts in the inline browser harness.
- Existing `tests/test_v31.py` regression checks passed: logo, window controls, three terminal windows, practical tasks, individual reset, report export and mobile layout.
- All 42 knowledge-to-practice references validated against the source `practical_missions.js`.

## Requires live-host acceptance

- Browser click-through to actual HTTPS `index.html?case=...&task=...` links on your own host.
- User profile progress behaviour in managed Edge/Chrome instances.
- Learner feedback on conceptual difficulty, screen readers and SEND settings in their environments.

## Pedagogical boundaries

Knowledge Hub is a concept-focused guide and does not contain the practical assignment solutions. It references uploaded Estio presentation slides 4–19 and separately clarifies current regulatory/technical distinctions. The SOC remains a controlled, non-networked fictional simulation.
