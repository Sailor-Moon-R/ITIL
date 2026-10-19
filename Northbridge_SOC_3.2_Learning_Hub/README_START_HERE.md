# Northbridge SOC 3.2 — Estio Incident Response Knowledge Hub + Practical Workstation

**Complete, self-contained teaching application · October 2026**

This release adds a concept-first learning experience to the existing Northbridge SOC virtual analyst workstation. Its main goal is to explain **what a part of incident response means, why it is done, what evidence or process is involved, and exactly where learners can practise that concept**.

## Getting started

1. Extract `Northbridge_SOC_3.2_Complete_Learning_Hub.zip`.
2. Upload the **entire extracted `Northbridge_SOC_3.2_Learning_Hub` folder**, preserving all subfolders, to your self-hosted HTTPS website. For example, put it into `.../sim/module12/northbridge-v32/`.
3. Open `.../northbridge-v32/START_HERE.html` for the simple two-route launcher, or `knowledge/index.html` to go straight to the explanatory Knowledge Hub.
4. Open `.../northbridge-v32/index.html` for the SOC virtual workstation. You can also open it directly from every knowledge page.
5. Try a Knowledge Hub practical link (e.g. **Evidence collection and preservation → Finance Lockdown → Preserve ransomware evidence**). It should take you through the educational agreement (on first use) and open the chosen case and practical assignment.

### Folder structure

- `START_HERE.html` — choose Knowledge Hub or SOC workstation
- `index.html` — original SOC workstation, now v3.2 with Knowledge Hub navigation and deep-link support
- `knowledge/index.html` — new concept-led interactive guide (no tests or mandatory progress)
- `knowledge/knowledge.css` — locally hosted design and responsive layout
- `knowledge/content.js` — 15 detailed concept-led learning sections, mapped to slide references
- `knowledge/knowledge.js` — search, navigation, visual demonstrations, practical assignment links, display preferences
- `knowledge/assets/` — optimised screenshots from the v3.1 app; no remote image service
- `assets/`, `core/`, `data/` — unchanged SOC application resources except for integration and version identification
- `legacy-academy/` — original guided academy retained
- `tests/` — automated regression and knowledge tests
- `docs/` — previous learner, QA and release resources

### No external software or accounts

All core teaching content, the Estio logo, scripts, styles, screenshots, incident datasets and simulated commands are local files. Hosting needs a standard static web server (Apache, Nginx or equivalent); learners need only a modern browser. There are no CDNs, external runtime APIs, virtual machines, installer, real terminals or administrative permissions. Official NIST, NCSC and ICO reference links are optional and require internet access.

**Important:** A static HTML site still needs a web server if using the intended hosted URLs and progress storage. Browser `file://` use may be restricted and is not the acceptance-tested deployment method.

## How learners should use it

1. **Understand:** Read any of the 15 concept sections in `knowledge/`. Each section explains its meaning, why it matters and a realistic example.
2. **Explore:** Use an interactive demonstration where shown (the response stages, evidence interpretation or impact/urgency controls). These are *explanations*, not quizzes.
3. **Apply:** Choose one of the labelled linked practical missions. The link specifies the case, exact task and tool (`?case=...&task=...&tool=practice`).
4. **Return:** Select **Learn the process** in the SOC header and continue reading. The Knowledge Hub remembers the last section where local storage is available.

There are no forced prerequisite checks, scores or mandatory tasks in the Knowledge Hub. The SOC workstation remains deliberately hands-on and retains independent practical mission resets.

## Curriculum and presentation alignment

Based on the uploaded Estio presentation *Incident Management Processes and Evidence Collection/Preservation*:

- Slides 4–6: why incident management and evidence handling matter
- Slides 7–9: preparation, identification, reporting and assessment
- Slides 10–11: containment, mitigation, eradication and recovery
- Slide 12 and 19: review and continual improvement
- Slides 13–17: evidence, proportionate collection, custody, legal considerations and documentation
- Slide 18: organising, interpreting and communicating findings

**Clarifications added to the original material:** NIST SP 800-61 Rev. 3 and CSF 2.0 are the current incident-response baseline; a hash or custody form supports reliability but does not guarantee admissibility; a cyber incident is not automatically an ICO-notifiable personal data breach. These additions are explicitly identified as context, rather than attributed to the uploaded slides.

## Educational and legal boundaries

The simulator contains fictional people, IP addresses, hosts, accounts and evidence. Do not input actual credentials, confidential data or personal information. The SOC retains its compulsory educational-use agreement. Nothing in the Knowledge Hub or workstation authorises testing real systems or constitutes legal advice, a forensic proof or a professional certification. Learners must follow their own organisation’s procedures and seek authorised specialist advice for reporting questions.

## Local progress

- Workstation saves incident progress to browser local storage and offers JSON export/import.
- Knowledge Hub stores only optional display preferences and last-read topic locally, if permitted.
- The Knowledge Hub never resets workstation progress or requires completing practical missions.
- Restoring an older v3.1 package to the **same origin** can still interact with existing local progress; back it up with the workstation export function before making hosting changes.

## Release testing

Checked with Chromium automation:

- All knowledge pages render, all topic links and assignment IDs resolve.
- Three interactive explainers respond correctly, search filters the topics and mobile layouts render.
- Guide-to-workstation first-run educational agreement and task selection logic pass simulated deep-link tests.
- Existing v3.1 workstation regression test (window controls, simultaneous terminals, individual reset and export) passes against this package.
- Every local asset/resource is readable through a test HTTP server.

**Remaining live deployment check:** In this development environment Chromium blocks navigation to local/localhost URLs. Resource delivery was checked with HTTP requests and the same release scripts were exercised inline. After uploading to your own host, test an actual hyperlink between the two pages, including a clean browser profile, and test with Edge on any locked-down learner devices.

## Tutor advice

A suggested low-talk route: introduce the concept for 5 minutes, let learners explore and talk through the example for 5 minutes, then send them into the corresponding practical assignment for 20–40 minutes. Debrief what they observed, what remains unknown, and the reason for their decisions. Do not automatically turn the Knowledge Hub into a test.
