/* Lesson content based on Estio slide deck, with explicitly added current-framework clarifications. */
window.NB_KNOWLEDGE_LESSONS = [
  {
    "id": "overview",
    "part": "Start here",
    "title": "What is incident management?",
    "short": "The difference between getting a service running and making a cyber incident safe.",
    "slide": "4–6",
    "phase": "Understand the whole response",
    "why": "Incidents are business problems as well as technical problems. Customers need services, responders need evidence, and leaders need reliable decisions.",
    "body": [
      [
        "Incident management",
        "A structured way to record, coordinate, prioritise and restore services following disruption. It provides ownership, escalation, communication and a dependable incident record."
      ],
      [
        "Cyber incident response",
        "The security-focused work of detecting and analysing malicious or suspicious activity, containing harm, removing the threat, preserving evidence and achieving safe recovery."
      ],
      [
        "These are connected, not identical",
        "Service management helps restore the service and manage ownership and risk. Cyber incident response addresses the threat and its causes. Restoring a service without checking for continuing attacker access can restart the problem."
      ]
    ],
    "example": "CaseFlow is slow. The service desk sees a disruption, while the SOC spots unusual privileged access. Both teams need one coordinated incident record, not separate assumptions.",
    "pitfall": "Not every outage is cyber-related; not every cyber incident takes a service offline.",
    "reflection": "Who owns customer restoration? Who owns the security investigation? How do their decisions affect each other?",
    "tags": [
      "incident",
      "service management",
      "K6",
      "K7"
    ],
    "practice": [
      [
        "storm",
        "s1"
      ],
      [
        "storm",
        "s2"
      ],
      [
        "northbridge",
        "n8"
      ]
    ]
  },
  {
    "id": "terminology",
    "part": "Understand",
    "title": "Event, alert, incident, problem or request?",
    "short": "Why classification affects response, urgency and ownership.",
    "slide": "6, 9",
    "phase": "Identify and classify",
    "why": "A flood of alerts is not proof of compromise. Incorrect classification can waste scarce response time or conceal significant threats.",
    "body": [
      [
        "Event",
        "A recorded observation: one successful login, process creation, DNS query or user action."
      ],
      [
        "Alert",
        "A monitoring rule or person highlights something that may require attention. An alert might be a false positive."
      ],
      [
        "Incident",
        "A security compromise, serious threat or disruption requiring coordinated response, depending on the organisation’s criteria."
      ],
      [
        "Problem / service request",
        "A problem seeks underlying causes of one or more incidents; a service request seeks an agreed routine service. Neither replaces an active security incident response."
      ]
    ],
    "example": "Thirty failed logins might be password spray; check for successes, unusual access and policy events before claiming an account was taken over.",
    "pitfall": "“High-severity SIEM alert” and “confirmed high-severity incident” are not synonyms.",
    "reflection": "Which additional record would turn a suspicious alert into a stronger incident declaration?",
    "tags": [
      "triage",
      "event",
      "alert",
      "classification"
    ],
    "practice": [
      [
        "storm",
        "s2"
      ],
      [
        "storm",
        "s7"
      ]
    ]
  },
  {
    "id": "prepare",
    "part": "Before the incident",
    "title": "Preparation and planning",
    "short": "Know your systems, roles, plans and recovery options before an emergency.",
    "slide": "7–8",
    "phase": "Prepare / Govern · Identify · Protect",
    "why": "A first response is much faster when people already know who may approve isolation, which services are essential and where reliable backups and logs are.",
    "body": [
      [
        "Plan and playbooks",
        "Agree incident criteria, contacts, escalation, containment options, communications and evidence procedures. A playbook guides but never removes judgement."
      ],
      [
        "Know your environment",
        "Maintain service maps, owners, asset lists, identity dependencies, baselines, logging and retention."
      ],
      [
        "Rehearse and improve",
        "Tabletops and technical exercises reveal permissions, missing evidence, weak restoration procedures and conflicting business priorities before a real incident."
      ]
    ],
    "example": "Before any Northbridge incident, find the identity tenant and the business-critical application. Both influence safe response choices.",
    "pitfall": "A plan that has not been exercised may be unusable when the primary email or identity system fails.",
    "reflection": "Which two teams and which two records would you need in the first 15 minutes?",
    "tags": [
      "preparation",
      "roles",
      "business continuity"
    ],
    "practice": [
      [
        "storm",
        "s1"
      ],
      [
        "lockdown",
        "l5"
      ],
      [
        "northbridge",
        "n1"
      ]
    ]
  },
  {
    "id": "detect",
    "part": "Find the incident",
    "title": "Detection, identification and reporting",
    "short": "From the first observation to a reasoned security judgement.",
    "slide": "7, 9",
    "phase": "Detect and analyse",
    "why": "The first alert seldom gives the whole answer. Prompt reporting, validation and a clear record allow teams to take proportionate action.",
    "body": [
      [
        "Signals",
        "SIEM, EDR, identity, proxy, DNS, email and user reports reveal different aspects of the environment. Any one signal can be incomplete."
      ],
      [
        "Triage",
        "Confirm event authenticity, time, affected host/account and scope. Examine alternative explanations and assign an initial priority and owner."
      ],
      [
        "Notify and document",
        "Record facts, assumptions, confidence, impact, who is informed, and what evidence or decision is needed next. Reassess when new evidence appears."
      ]
    ],
    "example": "A privileged sign-in and a suspicious export job occur close together. Their timing warrants investigation, but doesn’t alone identify the attacker.",
    "pitfall": "A SIEM correlation indicates a relationship worth investigating; it does not necessarily prove a shared cause.",
    "reflection": "What would you need to see to decide “possible compromise”, “confirmed incident”, or “benign activity”?",
    "tags": [
      "SIEM",
      "analysis",
      "reporting",
      "alert"
    ],
    "practice": [
      [
        "storm",
        "s2"
      ],
      [
        "northbridge",
        "n1"
      ],
      [
        "northbridge",
        "n7"
      ],
      [
        "invoice",
        "i3"
      ]
    ]
  },
  {
    "id": "severity",
    "part": "Find the incident",
    "title": "Impact, urgency and incident priority",
    "short": "Prioritise what matters to the service and the organisation.",
    "slide": "9–10",
    "phase": "Triage and escalation",
    "why": "The most technically dramatic alert may not be the most damaging. Priority should reflect impact, exposure, urgency and service dependencies.",
    "body": [
      [
        "Impact",
        "What users, data, safety, operations, customers or critical services are affected or potentially at risk?"
      ],
      [
        "Urgency",
        "How quickly could harm increase, evidence disappear or an important deadline pass?"
      ],
      [
        "Confidence and revision",
        "Severity and confidence are separate. You may urgently contain a credible threat while remaining uncertain about attribution or data disclosure."
      ]
    ],
    "example": "An isolated failed-login storm might be lower priority than suspicious administrator access linked to a sensitive export service.",
    "pitfall": "Do not confuse an arbitrary P1–P4 scheme with universal legal classifications; each organisation defines its thresholds.",
    "reflection": "What could move an incident up or down in priority when later records arrive?",
    "tags": [
      "priority",
      "impact",
      "urgency"
    ],
    "practice": [
      [
        "storm",
        "s7"
      ],
      [
        "northbridge",
        "n7"
      ],
      [
        "lockdown",
        "l7"
      ]
    ]
  },
  {
    "id": "contain",
    "part": "Respond",
    "title": "Containment and mitigation",
    "short": "Limit damage without unnecessarily destroying evidence or essential services.",
    "slide": "7, 10",
    "phase": "Respond: limit harm",
    "why": "An attacker may still have access even when the first infected device is disconnected. Actions must account for evidence preservation and service effects.",
    "body": [
      [
        "Immediate containment",
        "Reduce present harm by isolating an endpoint, revoking a session, stopping an unauthorised job or limiting a network path."
      ],
      [
        "Scope and authorisation",
        "Select the correct asset and control, check dependencies, obtain delegated authority, document the reason and plan validation or rollback."
      ],
      [
        "Watch for persistence elsewhere",
        "Blocking one connection does not prove the attacker has lost other sessions, secrets, services or hosts."
      ]
    ],
    "example": "In Northbridge, revoking a privileged session and stopping the export job may protect CaseFlow better than switching off the entire production service.",
    "pitfall": "The fastest-looking control is not always the safest; avoid blanket shutdowns that disrupt essential functions or erase volatile data.",
    "reflection": "Which asset would you isolate? What would you check before and after?",
    "tags": [
      "containment",
      "mitigation",
      "authorisation"
    ],
    "practice": [
      [
        "lockdown",
        "l5"
      ],
      [
        "northbridge",
        "n6"
      ]
    ]
  },
  {
    "id": "eradicate",
    "part": "Respond",
    "title": "Eradication and root-cause investigation",
    "short": "Remove the threat, persistence and exploited weakness—not just the symptom.",
    "slide": "7, 11",
    "phase": "Respond: remove the cause",
    "why": "A quiet network after containment can hide a malicious client secret, stolen session, scheduled task or vulnerable account still available to an attacker.",
    "body": [
      [
        "Threat removal",
        "Investigate malicious processes, unauthorised accounts/secrets, persistence, exploited software and other affected hosts before calling the threat removed."
      ],
      [
        "Understand the cause",
        "Distinguish what an attacker used from how they first entered. Some evidence may support a hypothesis without proving attribution."
      ],
      [
        "Verify removal",
        "Use fresh searches, endpoint checks, permission review, log monitoring and compensating controls to establish defensible confidence."
      ]
    ],
    "example": "Killing a suspicious PowerShell process is not automatically enough if a service secret or alternate route remains active.",
    "pitfall": "“No malware found” does not prove “no compromise occurred”.",
    "reflection": "If an attacker created an application credential, which other response actions might still be required?",
    "tags": [
      "eradication",
      "root cause",
      "persistence"
    ],
    "practice": [
      [
        "lockdown",
        "l2"
      ],
      [
        "northbridge",
        "n2"
      ],
      [
        "northbridge",
        "n6"
      ]
    ]
  },
  {
    "id": "recover",
    "part": "Restore",
    "title": "Recovery and validation",
    "short": "Restore trusted service operation without reopening the incident.",
    "slide": "7, 11",
    "phase": "Recover",
    "why": "Business pressure to resume operations is real. Recovery must restore dependable service and avoid using unsafe images, backups or credentials.",
    "body": [
      [
        "Recovery sequence",
        "Agree owners, changes, isolated testing, restored dependencies, security checks and a controlled return to production."
      ],
      [
        "RTO and RPO",
        "Recovery Time Objective concerns the acceptable restoration period. Recovery Point Objective concerns acceptable data loss measured in time."
      ],
      [
        "Confirm success",
        "Validate system function, integrity, identities, monitoring, customer impact and incident-manager/service-owner acceptance before closure."
      ]
    ],
    "example": "A backup marked “successful” has not necessarily been tested for integrity or freedom from compromise.",
    "pitfall": "Availability returning to normal is not the same as the security incident being closed.",
    "reflection": "Would you restore the whole application after stopping a rogue job if the service is already healthy? Why?",
    "tags": [
      "recovery",
      "backups",
      "RTO",
      "RPO"
    ],
    "practice": [
      [
        "lockdown",
        "l6"
      ],
      [
        "northbridge",
        "n8"
      ]
    ]
  },
  {
    "id": "evidence",
    "part": "Evidence",
    "title": "What counts as evidence?",
    "short": "Find relevant artefacts and understand what each source can prove.",
    "slide": "13, 16–17",
    "phase": "Collect and analyse",
    "why": "Incident responders need credible records to reconstruct events, protect the organisation and support later investigation.",
    "body": [
      [
        "Source types",
        "Identity logs, Windows/Linux events, cloud audit events, process trees, DNS, network flows, emails, asset records and physical notes all carry different limitations."
      ],
      [
        "Fact versus interpretation",
        "An audit log may prove an action was recorded; it may not prove who physically operated the account. Network bytes do not prove payload contents."
      ],
      [
        "Select for relevance",
        "Ask a specific investigation question: which account signed in, what process executed, what destination was contacted or what changed?"
      ]
    ],
    "example": "The Northbridge firewall observes outbound TLS bytes while the database audit reports record queries. Correlation is useful, but neither source alone proves exactly which personal records left.",
    "pitfall": "Do not invent evidence where a log contains only a summary, a lookup or an incomplete export.",
    "reflection": "Which independent source could strengthen your confidence in a possible data transfer?",
    "tags": [
      "digital evidence",
      "logs",
      "correlation"
    ],
    "practice": [
      [
        "invoice",
        "i4"
      ],
      [
        "northbridge",
        "n4"
      ],
      [
        "lockdown",
        "l3"
      ],
      [
        "storm",
        "s3"
      ]
    ]
  },
  {
    "id": "preserve",
    "part": "Evidence",
    "title": "Evidence collection and preservation",
    "short": "Keep relevant material intact, traceable and reviewable.",
    "slide": "13–16",
    "phase": "Preserve before destructive change where practicable",
    "why": "A good investigation may fail if evidence is overwritten, altered, collected without authority, or cannot be traced to a source.",
    "body": [
      [
        "Preservation workflow",
        "Identify relevant artefact; record source, date/time and purpose; select a justified collection method; protect the retained copy; verify integrity; document handling."
      ],
      [
        "Volatility and order",
        "RAM, running processes and short-retention logs can disappear. Balance prompt containment against preservation without prolonging active harm."
      ],
      [
        "Hashing",
        "A SHA-256 digest helps check whether bytes changed between two checks. It does not prove the source’s authenticity, lawful collection, completeness or admissibility."
      ]
    ],
    "example": "Inspect an EDR process, flag the record, enter a collection purpose and handler in Evidence Locker, preserve the copy, then verify its digest.",
    "pitfall": "A file hash without an evidence register and handling history is not a complete preservation process.",
    "reflection": "What would a future investigator need to understand where this artefact came from?",
    "tags": [
      "integrity",
      "SHA-256",
      "volatile evidence"
    ],
    "practice": [
      [
        "lockdown",
        "l4"
      ],
      [
        "northbridge",
        "n5"
      ],
      [
        "storm",
        "s4"
      ],
      [
        "invoice",
        "i5"
      ]
    ]
  },
  {
    "id": "custody",
    "part": "Evidence",
    "title": "Chain of custody, authenticity and proportionality",
    "short": "Record who held evidence and why it can be trusted.",
    "slide": "14–16",
    "phase": "Provenance and lawful handling",
    "why": "Evidence may move between analysts, providers and investigators. Without a record, later users cannot establish who handled it, why, and whether it was altered.",
    "body": [
      [
        "Chain of custody",
        "Record collector, timestamps, item ID, location, transfer recipient, method, purpose, condition and any integrity rechecks."
      ],
      [
        "Authenticity and reliability",
        "Investigate whether a record really came from the claimed system and whether collection and normalisation altered its meaning."
      ],
      [
        "Legal caveat",
        "Integrity and a complete custody log SUPPORT reliability, but courts and regulators apply wider rules. A training simulator cannot determine admissibility."
      ]
    ],
    "example": "An item moves from SOC analyst to forensics specialist. The preservation record should explain the handover and any integrity verification.",
    "pitfall": "“The SHA-256 matched, so the evidence is admissible” is legally and technically overconfident.",
    "reflection": "What matters most if an artefact passes through three people?",
    "tags": [
      "chain of custody",
      "lawful access",
      "admissibility"
    ],
    "practice": [
      [
        "northbridge",
        "n5"
      ],
      [
        "lockdown",
        "l4"
      ]
    ]
  },
  {
    "id": "timeline",
    "part": "Evidence",
    "title": "Building an incident timeline",
    "short": "Turn unrelated records into a chronology of observations and actions.",
    "slide": "16–18",
    "phase": "Investigate and document",
    "why": "A timeline reveals causality hypotheses, missing periods and moments when responders acted, and supports accountable reporting.",
    "body": [
      [
        "Separate three lanes",
        "Observed event: what the source says. Analyst inference: what it may mean. Response action: what the team decided and did."
      ],
      [
        "Reliable time",
        "Capture the original timestamp and time zone; different systems may have clock drift or delayed exports."
      ],
      [
        "Support the narrative",
        "Reference the exact evidence ID, note missing logs, and distinguish when an event occurred from when it was discovered."
      ]
    ],
    "example": "Compare privileged sign-in, application secret creation, export schedule change, query volume and outbound TLS flows without claiming all are proven to have one cause.",
    "pitfall": "An ordered list of events is not proof that the first recorded event caused everything after it.",
    "reflection": "Where might a missing 6-minute firewall interval affect your conclusion?",
    "tags": [
      "timeline",
      "time zones",
      "documentation"
    ],
    "practice": [
      [
        "northbridge",
        "n4"
      ],
      [
        "northbridge",
        "n7"
      ],
      [
        "lockdown",
        "l2"
      ]
    ]
  },
  {
    "id": "comms",
    "part": "Coordinate",
    "title": "Roles, escalation and stakeholder communications",
    "short": "Give different audiences accurate information at the right time.",
    "slide": "9, 16, 18",
    "phase": "Coordinate and report",
    "why": "The technical team cannot own every business, legal or customer decision. Clear authority and honest communication reduce confusion and harm.",
    "body": [
      [
        "Different audiences",
        "Incident manager coordinates; service owner accepts business risk; analyst reports observations; legal/data protection decides specialist questions; communications manages external messages."
      ],
      [
        "A useful update",
        "What happened; known impact; what is confirmed; what remains unknown; what is being done; who must decide; when the next update is due."
      ],
      [
        "Avoid overclaiming",
        "Do not promise a restore time or guarantee no data was exposed unless supported by evidence and approved."
      ]
    ],
    "example": "The COO wants a definitive statement while the network evidence remains incomplete. Provide the established facts, uncertainty, containment undertaken and next evidence milestone.",
    "pitfall": "Technical certainty and organisational pressure are separate; neither justifies unsupported claims.",
    "reflection": "How would you word a customer holding message without guessing?",
    "tags": [
      "comms",
      "escalation",
      "stakeholder"
    ],
    "practice": [
      [
        "northbridge",
        "n8"
      ],
      [
        "lockdown",
        "l7"
      ],
      [
        "invoice",
        "i7"
      ]
    ]
  },
  {
    "id": "law",
    "part": "Coordinate",
    "title": "Legal duties and boundaries",
    "short": "Recognise when privacy and regulatory specialists need to assess the case.",
    "slide": "13–15",
    "phase": "Governance and reporting",
    "why": "Investigations can affect personal information, employee privacy, legal obligations and regulatory notification deadlines.",
    "body": [
      [
        "Authority and proportionality",
        "Access only systems and evidence you are authorised to examine. Collect what is necessary, preserve records securely and follow workplace procedures."
      ],
      [
        "Personal data breaches",
        "A cyber incident does not automatically mean a personal data breach, and a personal data breach is not automatically reportable to the ICO. Risk assessment determines obligations."
      ],
      [
        "UK GDPR notification",
        "Where the notification threshold is met, the controller must report without undue delay and, where feasible, within 72 hours of becoming aware. High-risk breaches may also require communicating to individuals without undue delay."
      ]
    ],
    "example": "Northbridge has signs of sensitive-record access and possible outbound traffic. Escalate promptly to the data protection lead with known facts and gaps; do not make a unilateral reporting conclusion.",
    "pitfall": "Never wait for perfect forensic certainty before raising a potential reportable incident with the authorised specialist.",
    "reflection": "What information would the data protection lead need immediately?",
    "tags": [
      "UK GDPR",
      "ICO",
      "data protection"
    ],
    "practice": [
      [
        "northbridge",
        "n4"
      ],
      [
        "northbridge",
        "n8"
      ]
    ]
  },
  {
    "id": "improve",
    "part": "Learn and improve",
    "title": "Lessons learned and continual improvement",
    "short": "Use the investigation to change future outcomes, not assign automatic blame.",
    "slide": "12, 19",
    "phase": "Learn and improve",
    "why": "A technically successful response can still expose weaknesses in monitoring, service ownership, staff awareness, backup testing or response approvals.",
    "body": [
      [
        "Root cause versus contributing factors",
        "Ask what supported the incident, what accelerated harm, what delayed detection and which assumptions prevented an earlier response."
      ],
      [
        "Actionable improvement",
        "Recommend an owner, action, due date, measure and follow-up review rather than vague “more training” or “better security”."
      ],
      [
        "Measure response",
        "Useful metrics may include detection delay, response time, restoration validation, repeat incidents, false-positive handling and exercised playbook coverage."
      ]
    ],
    "example": "A client secret was created without sufficient monitoring. Assign ownership for short-lived credentials, audit rules and a measured review, then retest.",
    "pitfall": "Lessons learned are not complete merely because a post-incident document has been written.",
    "reflection": "What measurable change would make a repeat incident less likely?",
    "tags": [
      "root cause",
      "improvement",
      "metrics"
    ],
    "practice": [
      [
        "northbridge",
        "n8"
      ],
      [
        "lockdown",
        "l7"
      ]
    ]
  }
];
