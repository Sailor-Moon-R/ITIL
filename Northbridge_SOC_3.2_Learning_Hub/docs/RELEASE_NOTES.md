# Northbridge SOC 3.1 – Release notes

## Changes requested

1. **Window close bug fixed** – Close (×) now removes the actual DOM window and its taskbar entry, not merely a state flag. Close/reopen/minimise/restore/maximise passed browser interaction tests.
2. **Estio branding** – Bundles an actual Estio coloured-block logo and wordmark sourced from the user’s earlier Estio Module 12 slide/poster, displayed in the entry agreement, workstation header and preserved Academy header. No online image dependency.
3. **28 hands-on practical assignments** – 7 for Password Storm, 7 for Invoice Trap, 7 for Finance Lockdown and 8 for the Northbridge capstone. Their completion requires appropriate simulated terminal commands and investigation or response evidence rather than multiple-choice selections.
4. **Multiple console windows** – Separate PowerShell, Linux Shell and Cloud/Identity CLI windows, plus a dedicated in-mission terminal, with independent targets and per-session transcripts on the same fictional evidence.
5. **Guidance and repeatability** – Every mission has a clear brief, a checklist, three optional hints, a stretch task, a learner investigation field, automated practice checks and an independent assignment reset. Lab progress and terminal history are included in the exported case file.

## Compatibility

The application retains the original v3 state storage key and loads existing v3 progress; previous missions remain intact and the new practical missions start empty. The v2 Academy remains available as a separate local app and keeps its own storage key. Install **v3.1 into a new directory initially**, while you test it.

## Educational boundary

Everything in the consoles is fictional and executed only against in-memory case data. They are intentionally limited emulations, not full Windows, Linux or cloud shells. Completion checks verify practice actions, not the professional quality of prose or formal competence. Learners must follow real organisational authority and law outside the simulation.

## QA

Automated suites `test_v3.py`, `test_v3_extended.py`, `test_v31.py`, and `test_all_missions.py` passed. All 28 assignments were reachable with corresponding resources and controls. Browser navigation to loopback was blocked in the test environment, although static asset HTTP responses were checked separately. Deployment on your actual HTTPS host and with a managed learner browser still needs manual acceptance testing.
