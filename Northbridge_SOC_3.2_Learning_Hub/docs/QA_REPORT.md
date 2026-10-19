# Northbridge SOC 3.1 – QA report

Release candidate: October 2026. Browser logic and UI tested in headless Chromium using bundled release assets.

## Automated suites

**tests/test_v3.py:** PASS. Mandatory acceptance, the Shift Briefing, first incident, SIEM record selection, evidence flagging, SHA-256 preservation, terminal commands, authorised targeted response, notes, HTML case-file export, change of case, process investigation, workstation isolation, network flow consistency, recovery readiness, tool-scoped reset, delayed Northbridge evidence, responsive view and zero uncaught page errors.

**tests/test_v3_extended.py:** PASS. Event Viewer, Packet Inspector, service-desk ticket and stakeholder communications, reconstructed timeline, SHA-256 known vectors including Unicode, intentional evidence-copy alteration and failed verification, reset independence, HTML report content, progress JSON, separate mission states and narrow viewport.

**tests/test_v31.py:** PASS. Estio logo asset delivery via a local HTTP server, logo rendering from the exact bundled pixels in the browser, window × removal and reopening, minimise, restore and maximise, 3 concurrently opened command consoles with separate targets/transcripts, new assignment completion, single-assignment reset with new terminal work required, expanded report, responsive layout, zero uncaught JavaScript errors. The test environment blocked browser navigation to the loopback address, so the browser interaction test used the exact bundled script and CSS source with inlined local logo. Individual real HTTP asset URLs were fetched successfully by a local test client.

**tests/test_all_missions.py:** PASS. All 28 practical assignments across all four cases were exercised against matching local terminal commands, available evidence records, preservation, recovery and response actions, plus on-screen mission checks. This demonstrates reachability and consistency, not independent proof of educational quality or learner usability.

## Additional code and packaging checks

- JavaScript syntax checked using `node --check` on the four release scripts and the preserved legacy application script.
- No npm packages, runtime CDN requests, external images, analytics, fonts or API keys in the v3.1 release. The bundled Estio PNG was taken from the user’s earlier Estio Module 12 teaching poster; no remote image fetch is needed.
- V2 five-file Academy preserved under `legacy-academy/` with local script/CSS paths.
- Sanitised scenario source uses RFC 5737 reserved address spaces and `.example` names.
- Input text is HTML-escaped in UI and downloadable HTML case report.
- Evidence SHA-256 implementation verified with independent known-vector hashes; WebCrypto used when available and bundled fallback otherwise.
- Exercise resets are scoped; note that response-tool reset reverts shared simulated controls and removes their audit events. Timeline reset removes only learner-built timeline records; the shared clock is retained to avoid retroactively unreleasing evidence.

## Still to verify on hosting

1. Verify the uploaded directory structure and relative paths return success via HTTPS.
2. Confirm browser progress persists after refresh, can be exported/imported and is treated correctly by managed corporate browser policies.
3. Confirm users can open/download HTML reports and JSON files with their corporate device restrictions.
4. Perform tutor review of scenario realism, business risk, evidence limitations and UK legal statements before delivery.
5. Perform further manual accessibility testing, particularly with screen readers, high zoom and keyboard-only operation. This release does **not** claim WCAG conformance.
6. Perform manual cross-browser testing on the learner and tutor device/browser mix.

## Known limitations

- This is a **teaching simulator**, not an operating system, complete PowerShell environment, real SIEM, EDR product, PCAP parser, secure evidence repository or forensic acquisition tool.
- Event Viewer channels and Event ID labels are mapped for teaching and should not be treated as an original Windows EVTX export.
- The Packet Inspector is a flow-level illustrative view. It deliberately declines to invent encrypted payload content or precise packet lengths.
- The response engine has simplified control scope and illustrative threat indicators. Free-text quality is not automatically scored.
- Windows can be dragged on desktop displays, but are not full operating-system windows. Touch/small-screen presentation uses a single-focused-window layout.
- The release is entirely local; there is no multi-learner server dashboard, remote monitoring, authenticated trainer mode or built-in assessment submission.
- No direct `file://` or HTTP localhost *browser-navigation* end-to-end deployment test was possible because Chromium navigation to these routes was blocked by the test environment. Testing was conducted by injecting the exact packaged release resources into a browser page; the local-file/source and hosting-path behaviour must be checked after deployment.

The application retains its mandatory initial educational-use agreement and clearly distinguishes scenario interpretation from operational/legal instruction.
