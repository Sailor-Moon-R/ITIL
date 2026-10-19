# Northbridge SOC 3.1 – Learner quick start

**Level 4 Cyber Security · Module 12 · Incident Response & Service Management**

Welcome to your fictional SOC analyst workstation. You are not being asked to guess a hidden multiple-choice answer: you will review event records, investigate processes and connections, preserve relevant items, document your response and explain your reasoning to stakeholders.

## Starting your shift

Read and accept the three educational-use and legal statements, then select **Shift Briefing**. The brief explains the organisation, symptoms, critical services and current priority. The **Cases** button changes to another investigation without deleting existing work.

Follow the mission objectives in any sensible order. Many tools are interconnected and may be open in separate windows. Use the **taskbar** to return to a window. On a small screen, apps occupy most of the available display.

## How to investigate

- **SIEM Explorer / Event Viewer:** Filter alerts using terms like `source:identity`, `asset:NB-APP-02` or `level:high`. Open a suspicious event and flag evidence when justified. Be cautious of false positives and ambiguous alerts.
- **Endpoint EDR:** Look at an unexpected process, PID, parent process, running user and command description. Consider what process chain could explain an alert.
- **Network Flows / Packet Inspector:** Identify unusual host connections, destinations, protocols, timing and volume. Encrypted traffic does not reveal payload contents by itself.
- **Secure Mail:** Read messages, identify what was reported versus verified, and look for pressure from customers and management.
- **Virtual Files:** Explore inert text artefacts stored in the fictional case. No real malware or executable file is present.
- **PowerShell Console / Linux Shell / Cloud Identity CLI:** Type `help` for supported commands. Useful starting commands are `hosts`, `asset FIN-WS-07`, `Get-Process`, `Get-WinEvent`, `Get-NetTCPConnection`, `dir`, `cat 1` and `findstr PowerShell`.
- **Evidence Locker:** Flag records, explain why you need them, record a collector and collection method, then preserve a snapshot. Verify SHA-256 and observe what happens if a retained *simulation copy* is modified.
- **Response Console:** Choose a scoped control, identify the correct asset and justify your decision, authority and possible effects. Observe changes in other applications.
- **Recovery Lab:** Check system readiness, valid restore points, monitoring and ownership before recommending restoration.
- **Service Desk / Incident Comms:** Record the incident classification, priority, owner and escalation; write a factual update for an appropriate audience.
- **Case Notebook / Timeline:** Keep a clear distinction between facts, hypotheses, unknowns, actions and improvements. Add evidence references to the reconstructed timeline.

## Your 28 practical missions

Open **🎯 Practical Missions**. Choose one of the assignments and read the scenario question. You have an embedded terminal and can open separate PowerShell, Linux Shell and cloud/identity consoles at the same time. You will need to type suitable commands **and** work with evidence in the SIEM, EDR, mail, network, evidence or response tools. Use **Check my investigation** when you believe the task is complete. If a requirement is not demonstrated, the board tells you what is still missing without automatically providing a full solution.

There are **7 assignments each** for Password Storm, The Invoice Trap and Finance Lockdown, plus **8** for the Northbridge capstone. You do not need to complete every mission during one live lesson: the work is designed for additional independent practice.

Hints are offered in stages, and using them has no penalty. You can reset **one practical assignment** to clear its submission and hint state without affecting the other assignments or evidence. You must rerun its required terminal steps after that reset. The Evidence Locker, response actions and other shared system changes are intentionally preserved until you reset their tool or the whole case. The case-file download includes your practical mission results and command history.

**Caution:** The Linux, PowerShell and cloud consoles are command interpreters that simulate only a defined set of safe commands; they are not real shell environments and do not contact real services.

## The most useful habits

1. **Verify before concluding.** One alert rarely proves an entire attack chain.
2. **Consider who and what will be affected.** A critical service may depend on a host that looks expendable.
3. **Justify containment.** Acting quickly can be important, but destructive action or blanket shutdown can create new problems.
4. **Preserve relevant evidence.** A hash can help verify integrity, but cannot by itself prove authenticity or legal admissibility.
5. **Communicate uncertainty.** Explain what has been verified, what is being investigated and when the next update is due.
6. **Review and improve.** An incident is not truly finished because a service is merely switched back on.

## Getting help and resetting exercises

Select **Guided Help** for graduated hints, examples and official reference links. The learner does not lose marks for asking for help. Each practical window contains **Reset only this tool**. The × button closes the selected window and taskbar buttons can reopen it. It resets that particular activity, but the shared incident clock and already-released facts remain where appropriate. To start the entire case again, use **Reset this case** from Shift Briefing. Your work on other cases is preserved.

## Saving and submission

The application keeps your work in **this browser only**, not in a provider's database. Under **Display & data**, select **Export all progress** as a JSON backup before leaving. Use **Case file** to download a standalone HTML case report; it can be opened and printed as PDF. Submit only through the learning platform your tutor approves.

### Success criteria

By the end you should be able to explain what you observed, identify the most important artefacts, reconstruct a defensible chronology, justify proportionate response and restoration decisions, and provide a clear written advisory update to a non-specialist. Tool-completion indicators are for practice only: your tutor assesses the quality of your reasoning.

**Safety reminder:** Educational simulation only. Do not enter real company information, credentials or personal information. Do not attempt live exploitation, scanning or access without explicit authorisation. Follow the applicable professional and legal requirements in real work.
