<div align="center">

# ⚡ EiChaser
### Internal SLA & Commitment Tracker — Automated Workflow Engine for Support, IM & Service Manager Follow-Through

**Stop chasing your team manually. Let EiChaser chase them for you.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/Database-SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Engine-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Teams](https://img.shields.io/badge/Microsoft%20Teams-Integrated-6264A7?style=for-the-badge&logo=microsoftteams&logoColor=white)](https://www.microsoft.com/microsoft-teams)
[![Slack](https://img.shields.io/badge/Slack-Integrated-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://slack.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](#)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen?style=for-the-badge)](#)

**[Overview](#-executive-summary)** •
**[Problem](#-the-problem-statement)** •
**[Solution](#-the-eichaser-solution)** •
**[Architecture](#-system-architecture)** •
**[User Flows](#-user-flows)** •
**[Stall Score](#-the-stall-score-engine-the-heart-of-eichaser)** •
**[Setup](#-installation--setup-guide)** •
**[API](#-api-reference)** •
**[Roadmap](#-roadmap)**

</div>

---

<div align="center">

### 🧭 "The most dangerous phrase in customer support isn't 'I don't know.' It's 'I'll get back to you' — followed by silence."

</div>

---
## 🚀 LIVE PRODUCT

<p align="center">

### **[▶ LAUNCH EICHASER UNIVERSAL](https://eichaser-app-sla-tracker-bjptnhzercsdv2xq5rahmu.streamlit.app/)**

**Interactive AI-powered Commitment & SLA Intelligence Platform**

</p>

## 📖 Table of Contents

<details>
<summary><strong>Click to expand full table of contents</strong></summary>

1. [Executive Summary](#-executive-summary)
2. [The Problem Statement](#-the-problem-statement)
   - [The Silent SLA Killer](#the-silent-sla-killer)
   - [Why Manual Follow-Up Fails](#why-manual-follow-up-fails)
   - [The Human Cost](#the-human-cost)
   - [The Business Cost](#the-business-cost)
3. [The EiChaser Solution](#-the-eichaser-solution)
4. [What's New](#-whats-new)
5. [Core Philosophy & Design Principles](#-core-philosophy--design-principles)
6. [System Architecture](#-system-architecture)
   - [High-Level Architecture Diagram](#high-level-architecture-diagram)
   - [Component Breakdown](#component-breakdown)
   - [Data Flow Diagram](#data-flow-diagram)
   - [Sequence Diagram — Nudge Lifecycle](#sequence-diagram--nudge-lifecycle)
7. [The Stall Score Engine (The Heart of EiChaser)](#-the-stall-score-engine-the-heart-of-eichaser)
   - [Conceptual Model](#conceptual-model)
   - [Formula Breakdown](#formula-breakdown)
   - [Weighting Factors](#weighting-factors)
   - [Worked Examples](#worked-examples)
   - [Escalation Bands](#escalation-bands)
8. [User Flows](#-user-flows)
   - [Persona 1: Support Agent](#persona-1--support-agent-primary-case-owner)
   - [Persona 2: Incident Manager (IM)](#persona-2--incident-manager-im)
   - [Persona 3: Service Manager](#persona-3--service-manager)
   - [Persona 4: M1 Manager](#persona-4--m1-manager)
   - [Persona 5: IC1 Pod Member](#persona-5--ic1-pod-member)
   - [End-to-End Commitment Lifecycle](#end-to-end-commitment-lifecycle-flow)
9. [Feature Deep Dive](#-feature-deep-dive)
   - [Commitment Tracking](#1️⃣-commitment-tracking)
   - [Stall Scoring & Automated Chasing](#2️⃣-stall-scoring--automated-chasing)
   - [Pod Action Briefs](#3️⃣-pod-action-briefs)
   - [Nudge Tone Engine](#4️⃣-nudge-tone-engine)
   - [Escalation Engine](#5️⃣-escalation-engine)
10. [Data Model & Database Schema](#-data-model--database-schema)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Full SQL DDL](#full-sql-ddl)
    - [Table Reference Guide](#table-reference-guide)
11. [Tech Stack](#-tech-stack)
12. [Repository Structure](#-repository-structure)
13. [Installation & Setup Guide](#-installation--setup-guide)
14. [Configuration Reference](#-configuration-reference)
15. [API Reference](#-api-reference)
16. [Teams / Slack Integration Details](#-teams--slack-integration-details)
17. [Sample Action Brief](#-sample-action-brief-output)
18. [CLI Usage](#-cli-usage)
19. [Testing Strategy](#-testing-strategy)
20. [Security & Compliance](#-security--compliance)
21. [Performance & Scalability](#-performance--scalability)
22. [Monitoring & Observability](#-monitoring--observability)
23. [Impact & Metrics](#-impact--metrics)
24. [FAQ](#-frequently-asked-questions)
25. [Roadmap](#-roadmap)
26. [Contributing](#-contributing)
27. [License](#-license)
28. [Author](#-author--contact)
29. [Acknowledgments](#-acknowledgments)

</details>

---

## 🚀 Executive Summary

**EiChaser** is an internal workflow automation engine built to solve one of the most unglamorous but operationally critical problems inside any Support, Incident Management (IM), or Service Delivery organization: **the silent internal commitment that quietly dies in someone's inbox.**

Every day, Support engineers, Incident Managers, and Service Managers make **promises on behalf of the business** — "I'll check with the platform team and update you by EOD," "Engineering will confirm the fix window tomorrow," "The infra pod will re-verify by Friday." These promises become **implicit SLAs**. Customers wait on them. Trust is built or broken on them. And yet, internally, there is almost never a system that tracks whether these commitments were actually honored.

EiChaser closes that gap. It is a centralized, automated **commitment tracking and chasing engine** that:

- Logs every active case, its assigned internal owner, and the SLA promised to the customer.
- Continuously calculates a live **Stall Score** for every open commitment based on elapsed time versus expected owner response time.
- Automatically drafts and sends **polite-but-firm nudges** to stalled owners via Microsoft Teams or Slack — no human has to remember to chase anyone.
- Rolls up all stalled items into a daily **Pod Action Brief**, delivered automatically to the M1 Manager and the IC1 pod, so leadership sees exactly where the internal friction is *before* the customer does.

In short: **EiChaser is the tireless team member who never forgets to follow up.**

> **One-line pitch:** *EiChaser turns "I'll get back to you" into a tracked, time-boxed, automatically-escalated commitment — so nothing customer-facing ever breaches SLA because someone internally forgot to reply.*

---

## 🔥 The Problem Statement

### The Silent SLA Killer

In any support or service delivery organization, the **external SLA clock** (the one the customer sees) is almost always well-instrumented. Ticketing tools track first-response time, resolution time, breach alerts, and escalation paths for customer-facing timers.

But there is a second, invisible clock that almost nobody tracks: **the internal commitment clock.**

Consider a real, everyday scenario:

```
Day 0, 10:14 AM  — Customer reports a P2 issue.
Day 0, 10:20 AM  — Support Engineer (Owner A) opens the case,
                    tells the customer: "I'll check with the
                    Platform team and update you by EOD."
Day 0, 10:22 AM  — Owner A pings the Platform team on Teams.
Day 0, 5:45 PM   — Platform team hasn't responded. Owner A is
                    now in a different meeting.
Day 1, 9:00 AM   — Customer follows up: "Any update?"
Day 1, 9:03 AM   — Owner A realizes they never got a reply
                    from Platform, and never re-pinged them.
Day 1, 9:04 AM   — Owner A has now silently breached their own
                    promised SLA to the customer — not because
                    of a technical failure, but because of an
                    internal communication gap that nobody was
                    watching.
```

This is not a rare edge case. It is the **default failure mode** of any organization that relies on humans to remember to follow up on their own promises, made under pressure, in the middle of juggling five other cases.

### Why Manual Follow-Up Fails

| Failure Mode | Why It Happens | Result |
|---|---|---|
| **Cognitive overload** | Support engineers juggle 8–15 open cases at once | Follow-ups get mentally deprioritized |
| **No central ledger** | Commitments live in chat threads, not a system of record | No one entity has visibility across all promises |
| **Ownership diffusion** | "I pinged them, it's on them now" | Nobody feels accountable once the ball is passed |
| **Manager blind spots** | Managers only see escalations *after* they've already gone wrong | Reactive, not proactive, management |
| **No scoring/prioritization** | All stalled items look equally urgent (or equally invisible) | High-risk stalls get lost in the noise |
| **Chasing fatigue** | Manually chasing the same person repeatedly feels awkward | Humans under-chase to avoid social friction |

### The Human Cost

Support engineers and Incident Managers already operate in high-pressure, context-switching-heavy environments. Asking them to *also* be the mental tracking system for every promise they've ever made — across every case, every day — is an unreasonable and unsustainable cognitive burden. It leads to:

- **Burnout** from constantly worrying about "what did I forget to follow up on?"
- **Erosion of trust** with customers when promised updates don't arrive.
- **Blame ambiguity** when SLAs breach — was it the owner's fault, or was there never a system to catch it in time?

### The Business Cost

- Every breached commitment is a **trust tax** on the customer relationship.
- Repeated internal-cause breaches erode confidence in the support organization's operational discipline — even when the *technical* fix was completely fine.
- Leadership has **no early-warning system** for "where is our organization about to drop the ball internally" — they only find out from a customer escalation, which is the most expensive and reputationally costly way to find out.

---

## ✅ The EiChaser Solution

EiChaser reframes the problem from *"remember to follow up"* to *"let the system remember for you and chase for you."*

```
                  ❌ WITHOUT EICHASER                    ✅ WITH EICHASER
        ┌─────────────────────────────┐        ┌─────────────────────────────┐
        │ Commitment made in a chat    │        │ Commitment logged into a    │
        │ thread, buried in scrollback │  --->  │ centralized, queryable DB   │
        └─────────────────────────────┘        └─────────────────────────────┘
        ┌─────────────────────────────┐        ┌─────────────────────────────┐
        │ Owner has to remember to     │        │ Stall Score auto-calculated │
        │ follow up on their own       │  --->  │ every cycle — no memory     │
        └─────────────────────────────┘        │ required                    │
                                                 └─────────────────────────────┘
        ┌─────────────────────────────┐        ┌─────────────────────────────┐
        │ Manager finds out only when  │        │ Manager receives a daily    │
        │ customer escalates           │  --->  │ Action Brief before it ever │
        └─────────────────────────────┘        │ reaches that point          │
                                                 └─────────────────────────────┘
        ┌─────────────────────────────┐        ┌─────────────────────────────┐
        │ Chasing feels socially       │        │ Nudges are automated,       │
        │ awkward, so it's avoided     │  --->  │ polite-but-firm, and        │
        └─────────────────────────────┘        │ consistent every time       │
                                                 └─────────────────────────────┘
```

At its core, EiChaser is three systems working together:

1. **A ledger** — every active support case, its promised SLA, and its assigned internal owner, stored centrally.
2. **A scoring engine** — a Stall Score algorithm that continuously evaluates how "at risk" each commitment is, based on elapsed time vs. expected owner response time.
3. **A chasing & reporting layer** — automated Teams/Slack nudges for individual stalled owners, and a daily rolled-up Action Brief for managers and pods.

---

## 🆕 What's New

> This section tracks the evolution of EiChaser from concept to production tool. Update this changelog with every meaningful release.

| Version | Date | Highlights |
|---|---|---|
| **v1.0.0** | Initial Release | Core commitment ledger, Stall Score v1, manual-trigger nudges |
| **v1.1.0** | +2 weeks | Automated nudge scheduling (cron-based), Teams webhook integration |
| **v1.2.0** | +4 weeks | Slack integration added alongside Teams; multi-channel routing |
| **v1.3.0** | +6 weeks | Pod Action Briefs (daily digest) shipped to M1 Manager + IC1 pod |
| **v1.4.0** | +8 weeks | Escalation tiers (L1 → L2 → L3) added to Stall Score engine |
| **v1.5.0** | +10 weeks | Owner response-time baselining (per-owner historical averages) |
| **v2.0.0 (Planned)** | — | Predictive stall forecasting, self-serve dashboard, Grafana metrics |

> 💡 *Replace the "+N weeks" placeholders with actual release dates once you tag releases in this repository.*

---

## 🧠 Core Philosophy & Design Principles

EiChaser was built around five non-negotiable design principles:

1. **Zero manual tracking.** If a human has to remember to open a spreadsheet to see what's stalled, the system has already failed its core purpose.
2. **Polite but firm, always.** Automated nudges should never feel like a passive-aggressive bot. Every message is designed to preserve psychological safety while still creating urgency.
3. **Visibility before escalation.** The goal is never to "catch someone out" — it's to surface risk early enough that a human can course-correct before anything customer-facing breaks.
4. **One source of truth.** Every commitment lives in one place. No parallel spreadsheets, no shadow trackers, no "I thought someone else was tracking that."
5. **Boring reliability over flashy features.** This is infrastructure, not a demo. It should run quietly, every day, without needing anyone to babysit it.

---

## 🏗 System Architecture

### High-Level Architecture Diagram

```mermaid
flowchart TB
    subgraph Sources["📥 Commitment Sources"]
        A1[Support Ticketing System]
        A2[Manual Case Entry / API]
        A3[Chat Thread Parser - Teams/Slack]
    end

    subgraph Core["⚙️ EiChaser Core Engine"]
        B1[Commitment Ingestion Layer]
        B2[(Centralized Commitment DB)]
        B3[Stall Score Calculator]
        B4[Escalation Rules Engine]
        B5[Nudge Draft Generator]
        B6[Action Brief Compiler]
    end

    subgraph Delivery["📤 Delivery Layer"]
        C1[Microsoft Teams API]
        C2[Slack API]
        C3[Email Digest - optional]
    end

    subgraph Consumers["👥 Consumers"]
        D1[Individual Stalled Owner]
        D2[M1 Manager]
        D3[IC1 Pod Members]
        D4[Service Manager Dashboard]
    end

    A1 --> B1
    A2 --> B1
    A3 --> B1
    B1 --> B2
    B2 --> B3
    B3 --> B4
    B4 --> B5
    B4 --> B6
    B5 --> C1
    B5 --> C2
    B6 --> C1
    B6 --> C2
    B6 --> C3
    C1 --> D1
    C2 --> D1
    C1 --> D2
    C1 --> D3
    C2 --> D2
    C2 --> D3
    B2 --> D4
```

### Component Breakdown

| Component | Responsibility | Tech |
|---|---|---|
| **Commitment Ingestion Layer** | Normalizes incoming case/commitment data from ticketing systems, manual entry, or parsed chat commitments into a unified schema | Python, Pandas |
| **Centralized Commitment DB** | System of record for every active case, owner, promised SLA, and status history | SQL (PostgreSQL / SQL Server) |
| **Stall Score Calculator** | Runs on a scheduled cycle, computes live risk score per commitment | Python |
| **Escalation Rules Engine** | Applies threshold-based logic to decide whether an item needs a nudge, a brief mention, or a hard escalation | Python |
| **Nudge Draft Generator** | Generates natural-language, polite-but-firm nudge messages, personalized per owner and case | Python (template + tone engine) |
| **Action Brief Compiler** | Aggregates all stalled items across the pod into a single daily digest | Python, Pandas |
| **Delivery Layer** | Pushes nudges and briefs to the correct Teams channel / Slack channel / DM | REST APIs (Microsoft Graph, Slack Web API) |

### Data Flow Diagram

```mermaid
sequenceDiagram
    participant Ticketing as Ticketing System
    participant Ingest as Ingestion Layer
    participant DB as Commitment DB
    participant Scorer as Stall Score Engine
    participant Rules as Escalation Rules
    participant Nudge as Nudge Generator
    participant Teams as Teams / Slack
    participant Owner as Internal Owner
    participant Manager as M1 Manager / Pod

    Ticketing->>Ingest: New case + promised SLA + owner
    Ingest->>DB: Insert commitment record
    loop Every scoring cycle (e.g. every 30 min)
        DB->>Scorer: Fetch all open commitments
        Scorer->>Scorer: Compute Stall Score per commitment
        Scorer->>Rules: Pass scored commitments
        Rules->>Rules: Evaluate thresholds (L0/L1/L2/L3)
        alt Score crosses nudge threshold
            Rules->>Nudge: Trigger nudge draft
            Nudge->>Teams: Send polite-but-firm message
            Teams->>Owner: Owner receives nudge
        end
    end
    loop Every day at fixed time (e.g. 8:00 AM)
        DB->>Rules: Fetch all currently stalled items
        Rules->>Nudge: Compile Action Brief
        Nudge->>Teams: Post daily Pod Action Brief
        Teams->>Manager: Manager + pod receive brief
    end
```

### Sequence Diagram — Nudge Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Committed: Owner promises update by X
    Committed --> OnTrack: Time elapsed < expected response time
    OnTrack --> AtRisk: Time elapsed approaching threshold
    AtRisk --> Stalled: Threshold breached, no update logged
    Stalled --> NudgeSent: Automated nudge dispatched
    NudgeSent --> Resolved: Owner responds / updates case
    NudgeSent --> Escalated: No response after nudge + grace period
    Escalated --> ManagerNotified: Included in next Action Brief
    ManagerNotified --> Resolved: Manager intervenes, owner responds
    Resolved --> [*]
```

---

## 📊 The Stall Score Engine (The Heart of EiChaser)

### Conceptual Model

The **Stall Score** is a single, continuously-updated number (0–100) that represents how "at risk" a commitment is of breaching its promised SLA due to internal owner inaction. It is the single most important piece of intelligence EiChaser produces — everything else (nudges, escalations, action briefs) is downstream of this score.

The scoring model is intentionally simple to reason about, but tunable:

```
Stall Score = f(Time Elapsed, Expected Owner Response Time, Owner Historical Reliability, Case Severity)
```

### Formula Breakdown

At its simplest expressible form:

```
StallScore = min(100, (TimeElapsed / ExpectedResponseTime) × 100 × SeverityWeight × ReliabilityAdjustment)
```

Where:

| Variable | Meaning | Source |
|---|---|---|
| `TimeElapsed` | Minutes/hours since the commitment was made or last updated | System clock vs. `commitment_timestamp` |
| `ExpectedResponseTime` | The internally agreed SLA for that owner/role/case type (e.g., "Platform team: 4 business hours") | Configurable per team/role in `sla_baselines` table |
| `SeverityWeight` | Multiplier reflecting case priority (P1 = 1.5×, P2 = 1.2×, P3 = 1.0×, P4 = 0.8×) | Case severity field |
| `ReliabilityAdjustment` | A per-owner modifier based on historical on-time response rate — chronically slow responders get flagged earlier | Computed rolling average from `owner_response_history` |

### Weighting Factors

```python
SEVERITY_WEIGHTS = {
    "P1": 1.5,   # Critical — every minute counts
    "P2": 1.2,   # High
    "P3": 1.0,   # Medium — baseline
    "P4": 0.8,   # Low
}

def reliability_adjustment(owner_id: str) -> float:
    """
    Returns a multiplier between 0.85 and 1.25 based on the owner's
    trailing 30-day on-time response rate.
    A historically reliable owner gets slightly more benefit of the
    doubt (lower multiplier = score rises slower).
    A historically unreliable owner gets flagged earlier (higher
    multiplier = score rises faster), because past behavior predicts
    future stalls.
    """
    on_time_rate = get_owner_on_time_rate(owner_id)  # 0.0 - 1.0
    if on_time_rate >= 0.90:
        return 0.85
    elif on_time_rate >= 0.75:
        return 1.00
    elif on_time_rate >= 0.50:
        return 1.10
    else:
        return 1.25
```

### Worked Examples

**Example A — Healthy commitment, well within window**

```
Case: P3 billing inquiry
Owner: Finance Ops (on_time_rate = 0.92 → reliability = 0.85)
Expected response time: 8 business hours
Time elapsed: 2 hours

StallScore = min(100, (2/8) × 100 × 1.0 × 0.85)
           = min(100, 25 × 0.85)
           = 21.25  →  🟢 ON TRACK
```

**Example B — Approaching risk**

```
Case: P2 integration failure
Owner: Platform Team (on_time_rate = 0.70 → reliability = 1.10)
Expected response time: 4 business hours
Time elapsed: 3.5 hours

StallScore = min(100, (3.5/4) × 100 × 1.2 × 1.10)
           = min(100, 87.5 × 1.32)
           = min(100, 115.5) → capped at 100
           = 100  →  🔴 STALLED — Immediate nudge triggered
```

**Example C — Critical case, chronically slow owner**

```
Case: P1 production outage dependency
Owner: Infra Pod Member (on_time_rate = 0.40 → reliability = 1.25)
Expected response time: 1 business hour
Time elapsed: 0.75 hours

StallScore = min(100, (0.75/1) × 100 × 1.5 × 1.25)
           = min(100, 75 × 1.875)
           = min(100, 140.6) → capped at 100
           = 100  →  🔴 STALLED — Immediate nudge + auto-escalation
```

> Note how the P1 case with a chronically slow owner reaches maximum stall risk *before* the raw elapsed-time ratio would suggest — this is the reliability adjustment doing its job: **it front-loads urgency for owners who have a track record of letting things slip.**

### Escalation Bands

| Score Range | Status | Color | Action Taken |
|---|---|---|---|
| **0 – 39** | On Track | 🟢 Green | No action. Logged silently. |
| **40 – 64** | At Risk | 🟡 Yellow | Included in Action Brief as "Watch List," no direct nudge yet |
| **65 – 84** | Stalled | 🟠 Orange | Automated polite-but-firm nudge sent directly to owner |
| **85 – 100** | Critical Stall | 🔴 Red | Nudge sent + flagged for immediate inclusion in next Action Brief + optional manager DM |

---

## 🧭 User Flows

### Persona 1 — Support Agent (Primary Case Owner)

```mermaid
flowchart LR
    A[Open customer case] --> B[Make internal commitment<br>e.g. 'will check with Platform team']
    B --> C[Log commitment in EiChaser<br>via ticketing integration or manual entry]
    C --> D{EiChaser tracks<br>Stall Score in background}
    D -->|Score stays low| E[No action needed —<br>agent works other cases]
    D -->|Score crosses threshold| F[Agent's internal owner<br>receives automated nudge]
    F --> G[Owner responds]
    G --> H[Agent updates customer<br>with resolution/status]
    H --> I[Commitment marked Resolved<br>in EiChaser]
```

**Narrative walkthrough:**
A support agent opens a P2 case. Mid-conversation with the customer, they realize they need input from another internal team before they can respond definitively. Instead of just pinging that team in a chat thread and hoping for the best, the agent (or the system, via ticketing integration) logs this as a tracked commitment in EiChaser: *"Platform Team — response needed by EOD."* From that moment, the agent is free to move on to their next case with full confidence that if the Platform Team goes quiet, EiChaser will notice and chase on their behalf — they don't have to hold it in their head.

---

### Persona 2 — Incident Manager (IM)

```mermaid
flowchart TD
    A[Incident declared] --> B[IM assigns action items<br>to multiple internal owners]
    B --> C[Each action item logged<br>as a commitment in EiChaser]
    C --> D[EiChaser tracks all commitments<br>in parallel, independent Stall Scores]
    D --> E{Any owner stalls?}
    E -->|Yes| F[Owner nudged automatically —<br>IM not required to manually chase]
    E -->|No| G[Incident timeline stays clean]
    F --> H[IM sees stalled items surfaced<br>in real time via dashboard/brief]
    H --> I[IM can escalate directly if<br>nudge doesn't resolve in time]
```

**Narrative walkthrough:**
During a live incident, an Incident Manager typically has to track five, six, sometimes ten parallel action items across different teams simultaneously — while also managing customer communication and the technical bridge call. EiChaser removes the "who owes me an update" mental overhead entirely: every action item is a tracked commitment with its own live Stall Score, and the IM gets pinged only when something actually needs their attention, not for routine tracking.

---

### Persona 3 — Service Manager

```mermaid
flowchart LR
    A[Owns overall account health<br>& SLA relationship with customer] --> B[Reviews EiChaser dashboard /<br>Action Brief each morning]
    B --> C{Any high-risk<br>commitments for their accounts?}
    C -->|Yes| D[Proactively reaches out<br>internally before customer notices]
    C -->|No| E[Confidence that all promises<br>are on track]
    D --> F[Customer relationship<br>protected proactively]
```

**Narrative walkthrough:**
The Service Manager is the person who ultimately owns the customer relationship and reputational risk. Historically, they found out about internal stalls *after* the customer complained. With EiChaser, the Service Manager reviews the morning Action Brief and sees, in one glance, exactly which of their accounts have commitments trending toward risk — and can intervene hours or days before the customer ever notices anything was slow.

---

### Persona 4 — M1 Manager

```mermaid
flowchart TD
    A[Receives daily Pod Action Brief<br>at fixed time each morning] --> B[Reviews stalled/at-risk items<br>across entire pod]
    B --> C{Pattern detected?<br>e.g. same owner stalling repeatedly}
    C -->|Yes| D[1:1 coaching conversation<br>with repeat-offender owner]
    C -->|No| E[Spot-checks individual<br>high-severity stalls]
    D --> F[Owner reliability score<br>improves over time]
    E --> G[Pod-wide SLA discipline<br>maintained]
```

**Narrative walkthrough:**
The M1 Manager no longer has to manually audit every case to find operational risk. Instead, EiChaser surfaces it to them automatically, every single morning, as a ranked, prioritized brief. Over time, this also becomes a coaching tool — patterns of repeat stalling by the same owner become visible and actionable, rather than anecdotal.

---

### Persona 5 — IC1 Pod Member

```mermaid
flowchart LR
    A[Receives own name in<br>Pod Action Brief if stalled] --> B[Immediately understands<br>which commitment is at risk]
    B --> C[Takes action / responds<br>to close the loop]
    C --> D[Commitment resolved,<br>removed from next brief]
```

**Narrative walkthrough:**
For an individual contributor, visibility is itself the intervention. Most people don't stall out of negligence — they stall because they're juggling too much and something slipped their mind. Seeing their name attached to a specific, time-boxed commitment in a shared, visible brief is usually all it takes to trigger immediate action — no manager intervention required in the majority of cases.

---

### End-to-End Commitment Lifecycle Flow

```mermaid
flowchart TD
    Start([Customer-facing commitment made]) --> Log[Commitment logged in EiChaser]
    Log --> Score[Stall Score engine begins tracking]
    Score --> Check{Score checked every cycle}
    Check -->|"0-39 Green"| Silent[Logged silently, no action]
    Check -->|"40-64 Yellow"| Watch[Added to Watch List section<br>of next Action Brief]
    Check -->|"65-84 Orange"| Nudge1[Automated nudge sent<br>directly to owner]
    Check -->|"85-100 Red"| Nudge2[Urgent nudge sent +<br>flagged for manager visibility]
    Silent --> Recheck[Re-evaluated next cycle]
    Watch --> Recheck
    Nudge1 --> Response{Owner responds<br>within grace period?}
    Nudge2 --> Response
    Response -->|Yes| Resolve([Commitment marked Resolved])
    Response -->|No| Escalate[Included in Pod Action Brief<br>as escalated item]
    Escalate --> ManagerAction[M1 Manager / Service Manager<br>intervenes directly]
    ManagerAction --> Resolve
    Recheck --> Check
```

---

## 🔍 Feature Deep Dive

### 1️⃣ Commitment Tracking

The foundation of EiChaser is a **centralized database** that logs, for every active support case:

- The **case ID** and link back to the source ticketing system.
- The **customer-facing promise** (verbatim or structured — e.g., "update by EOD," "fix confirmation by Friday 3PM").
- The **assigned internal owner** (individual, team, or pod).
- The **promised SLA window**, both to the customer and internally.
- A **full status history** — every state transition (Committed → On Track → At Risk → Stalled → Nudged → Resolved/Escalated) with timestamps, so nothing is ever lost or ambiguous after the fact.

This is intentionally designed as a **single source of truth**. No parallel spreadsheets. No "I thought Sarah was tracking that." One ledger, one query interface, one shared understanding of what's outstanding at any given moment.

### 2️⃣ Stall Scoring & Automated Chasing

Covered in full detail in [The Stall Score Engine](#-the-stall-score-engine-the-heart-of-eichaser) above. In summary: every open commitment gets a continuously-recalculated risk score, and once that score crosses a configurable threshold, EiChaser automatically drafts and sends a nudge — no human trigger required.

The nudges are deliberately engineered to be:
- **Polite** — never accusatory, never robotic-sounding.
- **Firm** — clearly states what's outstanding and by when it was expected.
- **Actionable** — always includes a direct link back to the case and a one-click way to respond/update.
- **Context-aware** — references the specific commitment language originally made, not a generic template.

### 3️⃣ Pod Action Briefs

Instead of relying on managers to manually audit case queues, EiChaser compiles a **daily digest** — the Pod Action Brief — automatically delivered each morning to the M1 Manager and IC1 pod members. It replaces what used to be a manual, error-prone "let me go check everyone's open cases" ritual with a **standing, standardized, automated report**.

The brief is organized by risk tier (Critical Stalls → Stalled → At Risk / Watch List) and by owner, so it takes under two minutes to scan and understand exactly where the pod's operational risk sits that day.

### 4️⃣ Nudge Tone Engine

A lightweight templating layer that ensures every automated message reads as **human-written, not robotic**. It varies phrasing across a curated set of polite-but-firm templates, injects specific case context, and scales tone slightly with urgency tier (a Yellow watch-list mention reads gently; a Red critical stall nudge reads with clear urgency, still respectfully).

### 5️⃣ Escalation Engine

Applies the [Escalation Bands](#escalation-bands) thresholds to decide exactly what happens at each score tier — from silent logging, to direct nudge, to inclusion in the manager-facing brief, to (optionally) a direct manager DM for the most critical, longest-running stalls.

---

## 🗄 Data Model & Database Schema

### Entity Relationship Diagram

```mermaid
erDiagram
    CASES ||--o{ COMMITMENTS : has
    COMMITMENTS ||--o{ STATUS_HISTORY : tracks
    COMMITMENTS }o--|| OWNERS : assigned_to
    OWNERS ||--o{ OWNER_RESPONSE_HISTORY : builds
    COMMITMENTS ||--o{ NUDGES : triggers
    OWNERS }o--|| TEAMS : belongs_to
    TEAMS ||--o{ SLA_BASELINES : defines

    CASES {
        string case_id PK
        string customer_name
        string severity
        string source_system
        datetime opened_at
        string status
    }

    COMMITMENTS {
        string commitment_id PK
        string case_id FK
        string owner_id FK
        text promised_text
        datetime committed_at
        datetime expected_by
        float stall_score
        string status
    }

    OWNERS {
        string owner_id PK
        string owner_name
        string team_id FK
        string role
        float on_time_rate
    }

    STATUS_HISTORY {
        string history_id PK
        string commitment_id FK
        string old_status
        string new_status
        datetime changed_at
    }

    NUDGES {
        string nudge_id PK
        string commitment_id FK
        string channel
        text message_text
        datetime sent_at
        string response_status
    }

    TEAMS {
        string team_id PK
        string team_name
    }

    SLA_BASELINES {
        string baseline_id PK
        string team_id FK
        string case_severity
        int expected_response_minutes
    }

    OWNER_RESPONSE_HISTORY {
        string record_id PK
        string owner_id FK
        datetime commitment_date
        boolean was_on_time
    }
```

### Full SQL DDL

```sql
-- =========================================================
-- EiChaser Core Schema
-- =========================================================

CREATE TABLE teams (
    team_id         VARCHAR(36) PRIMARY KEY,
    team_name       VARCHAR(120) NOT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE owners (
    owner_id        VARCHAR(36) PRIMARY KEY,
    owner_name      VARCHAR(120) NOT NULL,
    team_id         VARCHAR(36) REFERENCES teams(team_id),
    role            VARCHAR(80),
    email           VARCHAR(160),
    teams_user_id   VARCHAR(160),   -- Microsoft Teams identity
    slack_user_id   VARCHAR(160),   -- Slack identity
    on_time_rate    NUMERIC(4,3) DEFAULT 1.000,  -- rolling 30-day average
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sla_baselines (
    baseline_id             VARCHAR(36) PRIMARY KEY,
    team_id                 VARCHAR(36) REFERENCES teams(team_id),
    case_severity           VARCHAR(4) CHECK (case_severity IN ('P1','P2','P3','P4')),
    expected_response_minutes INT NOT NULL,
    UNIQUE(team_id, case_severity)
);

CREATE TABLE cases (
    case_id         VARCHAR(36) PRIMARY KEY,
    customer_name   VARCHAR(200) NOT NULL,
    severity        VARCHAR(4) CHECK (severity IN ('P1','P2','P3','P4')),
    source_system   VARCHAR(80),          -- e.g. ServiceNow, Zendesk, Jira SM
    opened_at       TIMESTAMP NOT NULL,
    status          VARCHAR(20) DEFAULT 'Open'
);

CREATE TABLE commitments (
    commitment_id   VARCHAR(36) PRIMARY KEY,
    case_id         VARCHAR(36) REFERENCES cases(case_id),
    owner_id        VARCHAR(36) REFERENCES owners(owner_id),
    promised_text   TEXT NOT NULL,
    committed_at    TIMESTAMP NOT NULL,
    expected_by     TIMESTAMP NOT NULL,
    last_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stall_score     NUMERIC(5,2) DEFAULT 0.00,
    status          VARCHAR(20) DEFAULT 'Committed'
        CHECK (status IN ('Committed','OnTrack','AtRisk','Stalled','Nudged','Escalated','Resolved'))
);

CREATE TABLE status_history (
    history_id      VARCHAR(36) PRIMARY KEY,
    commitment_id   VARCHAR(36) REFERENCES commitments(commitment_id),
    old_status      VARCHAR(20),
    new_status      VARCHAR(20),
    changed_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE nudges (
    nudge_id            VARCHAR(36) PRIMARY KEY,
    commitment_id       VARCHAR(36) REFERENCES commitments(commitment_id),
    channel             VARCHAR(20) CHECK (channel IN ('teams','slack','email')),
    message_text        TEXT NOT NULL,
    sent_at             TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    response_status      VARCHAR(20) DEFAULT 'Pending'
        CHECK (response_status IN ('Pending','Acknowledged','Resolved','Ignored'))
);

CREATE TABLE owner_response_history (
    record_id           VARCHAR(36) PRIMARY KEY,
    owner_id             VARCHAR(36) REFERENCES owners(owner_id),
    commitment_id         VARCHAR(36) REFERENCES commitments(commitment_id),
    commitment_date        DATE NOT NULL,
    was_on_time            BOOLEAN NOT NULL
);

CREATE TABLE action_briefs (
    brief_id             VARCHAR(36) PRIMARY KEY,
    generated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pod_id                VARCHAR(36),
    critical_count        INT,
    stalled_count         INT,
    watchlist_count        INT,
    payload_json           JSONB
);

-- =========================================================
-- Indexes for performance
-- =========================================================
CREATE INDEX idx_commitments_status ON commitments(status);
CREATE INDEX idx_commitments_owner ON commitments(owner_id);
CREATE INDEX idx_commitments_stall_score ON commitments(stall_score DESC);
CREATE INDEX idx_nudges_commitment ON nudges(commitment_id);
CREATE INDEX idx_status_history_commitment ON status_history(commitment_id);
```

### Table Reference Guide

| Table | Purpose |
|---|---|
| `teams` | Master list of internal teams that can be commitment owners (Platform, Infra, Finance Ops, etc.) |
| `owners` | Individual people or team-level owners, with their Teams/Slack identity mappings and reliability score |
| `sla_baselines` | Configurable expected-response-time table, per team per severity — this is what makes the Stall Score tunable without code changes |
| `cases` | Source-of-truth case records, synced from the ticketing system |
| `commitments` | The core ledger — every promise made, its owner, its deadline, and its live Stall Score |
| `status_history` | Full audit trail of every state transition for compliance/reporting |
| `nudges` | Every automated message ever sent, with delivery channel and response status |
| `owner_response_history` | Rolling record used to compute each owner's `on_time_rate`, feeding the reliability adjustment |
| `action_briefs` | Archive of every daily brief generated, for historical trend analysis |

---

## 🧰 Tech Stack

| Layer | Technology | Why |
|---|---|---|
| **Core Language** | Python 3.11+ | Rapid development, strong ecosystem for data processing and API integration |
| **Data Processing** | Pandas | Efficient batch scoring, aggregation, and Action Brief compilation across large commitment sets |
| **Database** | SQL (PostgreSQL recommended, SQL Server compatible) | Relational integrity is essential — commitments, owners, and status history are inherently relational |
| **Scheduling** | Cron / APScheduler | Drives the periodic Stall Score recalculation cycle and daily Action Brief generation |
| **Messaging Integration** | Microsoft Graph API (Teams), Slack Web API | Meets users where they already work — no new tool to check |
| **Templating** | Jinja2 (recommended) | Powers the Nudge Tone Engine's message generation |
| **Config Management** | `.env` + YAML | Keeps SLA baselines, thresholds, and secrets cleanly separated from code |
| **Testing** | Pytest | Unit and integration test coverage for the scoring engine and integrations |
| **Optional Dashboard** | Streamlit / Grafana | For visualizing live Stall Scores and historical trend reporting |

---

## 📁 Repository Structure

```
EiChaser/
│
├── README.md                          # You are here
├── LICENSE
├── .env.example                       # Template for required environment variables
├── requirements.txt                   # Python dependencies
├── pyproject.toml                     # Project metadata & tooling config
├── docker-compose.yml                 # Local DB + app spin-up (optional)
│
├── config/
│   ├── sla_baselines.yaml             # Per-team, per-severity expected response times
│   ├── escalation_bands.yaml          # Configurable Stall Score thresholds
│   └── nudge_templates.yaml           # Polite-but-firm message templates by tier
│
├── db/
│   ├── schema.sql                     # Full DDL (see Data Model section above)
│   ├── migrations/                    # Versioned schema migrations
│   │   ├── 0001_init.sql
│   │   ├── 0002_add_owner_reliability.sql
│   │   └── 0003_add_action_briefs.sql
│   └── seed_data/
│       ├── teams_seed.sql
│       └── sla_baselines_seed.sql
│
├── eichaser/                          # Main application package
│   ├── __init__.py
│   ├── config.py                      # Loads and validates config/env
│   ├── db/
│   │   ├── __init__.py
│   │   ├── connection.py              # SQL connection/session management
│   │   ├── models.py                  # ORM-style data models
│   │   └── queries.py                 # Reusable parameterized queries
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── ticketing_connector.py     # Pulls new cases/commitments from ticketing system
│   │   ├── manual_entry.py            # CLI/API path for manually logged commitments
│   │   └── normalizer.py              # Normalizes incoming data to unified schema
│   │
│   ├── scoring/
│   │   ├── __init__.py
│   │   ├── stall_score.py             # Core Stall Score calculation engine
│   │   ├── reliability.py             # Owner reliability adjustment logic
│   │   └── severity_weights.py        # Severity multiplier config/logic
│   │
│   ├── escalation/
│   │   ├── __init__.py
│   │   ├── rules_engine.py            # Threshold-based escalation band logic
│   │   └── band_config.py
│   │
│   ├── nudging/
│   │   ├── __init__.py
│   │   ├── tone_engine.py             # Generates polite-but-firm nudge text
│   │   ├── templates/
│   │   │   ├── watchlist_template.j2
│   │   │   ├── stalled_template.j2
│   │   │   └── critical_template.j2
│   │   └── dispatcher.py              # Routes nudges to Teams/Slack
│   │
│   ├── briefs/
│   │   ├── __init__.py
│   │   ├── compiler.py                # Builds the daily Pod Action Brief
│   │   └── brief_template.j2
│   │
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── teams_client.py            # Microsoft Graph API wrapper
│   │   ├── slack_client.py            # Slack Web API wrapper
│   │   └── email_client.py            # Optional email digest fallback
│   │
│   ├── scheduler/
│   │   ├── __init__.py
│   │   └── jobs.py                    # Cron/APScheduler job definitions
│   │
│   └── cli/
│       ├── __init__.py
│       └── main.py                    # CLI entry point (see CLI Usage section)
│
├── dashboard/                         # Optional Streamlit dashboard
│   └── app.py
│
├── tests/
│   ├── unit/
│   │   ├── test_stall_score.py
│   │   ├── test_reliability.py
│   │   └── test_escalation_rules.py
│   ├── integration/
│   │   ├── test_teams_integration.py
│   │   └── test_slack_integration.py
│   └── fixtures/
│       └── sample_commitments.json
│
├── scripts/
│   ├── run_scoring_cycle.py           # Manual trigger for the scoring cycle
│   ├── generate_action_brief.py       # Manual trigger for brief generation
│   └── seed_demo_data.py              # Populates DB with demo/test data
│
└── docs/
    ├── architecture.md
    ├── stall_score_methodology.md
    └── api_reference.md
```

---

## ⚙️ Installation & Setup Guide

### Prerequisites

| Requirement | Minimum Version |
|---|---|
| Python | 3.11+ |
| PostgreSQL (or SQL Server) | 13+ |
| pip / poetry | Latest |
| Microsoft Teams app registration (for Teams integration) | — |
| Slack app with Bot Token (for Slack integration) | — |

### Step-by-Step Setup

```bash
# 1. Clone the repository
git clone https://github.com/GaneshEiGo/EiChaser.git
cd EiChaser

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy and configure environment variables
cp .env.example .env
# then edit .env with your DB credentials, Teams/Slack tokens, etc.

# 5. Initialize the database schema
psql -U your_user -d eichaser_db -f db/schema.sql

# 6. (Optional) Seed demo data to explore the tool immediately
python scripts/seed_demo_data.py

# 7. Run the scoring engine once, manually, to verify everything works
python scripts/run_scoring_cycle.py

# 8. Start the scheduler (runs scoring cycles + daily briefs automatically)
python -m eichaser.scheduler.jobs
```

### Environment Variables (`.env.example`)

```env
# ---------- Database ----------
DB_HOST=localhost
DB_PORT=5432
DB_NAME=eichaser_db
DB_USER=eichaser_service
DB_PASSWORD=changeme

# ---------- Microsoft Teams ----------
TEAMS_TENANT_ID=your-tenant-id
TEAMS_CLIENT_ID=your-client-id
TEAMS_CLIENT_SECRET=your-client-secret
TEAMS_WEBHOOK_URL=https://outlook.office.com/webhook/your-webhook

# ---------- Slack ----------
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_DEFAULT_CHANNEL=#pod-action-briefs

# ---------- Scheduling ----------
SCORING_CYCLE_MINUTES=30
ACTION_BRIEF_TIME=08:00

# ---------- Ticketing Integration ----------
TICKETING_SYSTEM=servicenow          # or zendesk, jira_sm, etc.
TICKETING_API_BASE_URL=https://your-instance.service-now.com
TICKETING_API_TOKEN=your-api-token
```

---

## 🔧 Configuration Reference

### `config/sla_baselines.yaml`

```yaml
teams:
  platform_team:
    P1: 60      # minutes
    P2: 240
    P3: 480
    P4: 1440

  infra_pod:
    P1: 45
    P2: 180
    P3: 360
    P4: 1440

  finance_ops:
    P1: 120
    P2: 480
    P3: 960
    P4: 2880
```

### `config/escalation_bands.yaml`

```yaml
bands:
  on_track:
    min_score: 0
    max_score: 39
    action: log_silent

  at_risk:
    min_score: 40
    max_score: 64
    action: add_to_watchlist

  stalled:
    min_score: 65
    max_score: 84
    action: send_nudge

  critical:
    min_score: 85
    max_score: 100
    action: send_nudge_and_flag_manager
```

### `config/nudge_templates.yaml`

```yaml
stalled:
  - "Hi {owner_name}, quick nudge — the update on {case_id} ({promised_text}) was expected around {expected_by}. Could you share a status when you get a moment? Thanks for keeping this moving!"
  - "Hey {owner_name}, following up on {case_id} — we're a little past the expected window for {promised_text}. An update, even a brief one, would really help us keep the customer informed."

critical:
  - "⚠️ {owner_name}, this one's turning urgent: {case_id} ({promised_text}) is now significantly past its expected window ({expected_by}). Could you prioritize a response today? Flagging so we can support if you're blocked."
```

---

## 🔌 API Reference

> EiChaser exposes a lightweight internal REST API for logging commitments, querying stall status, and pulling briefs programmatically (e.g., from a ticketing system webhook).

### `POST /api/v1/commitments`
Logs a new commitment.

**Request body:**
```json
{
  "case_id": "CASE-10234",
  "owner_id": "OWNER-platform-01",
  "promised_text": "Will confirm root cause window by EOD",
  "committed_at": "2026-08-08T10:22:00Z",
  "expected_by": "2026-08-08T18:00:00Z",
  "severity": "P2"
}
```

**Response:**
```json
{
  "commitment_id": "CMT-88213",
  "status": "Committed",
  "stall_score": 0.0
}
```

### `GET /api/v1/commitments/{commitment_id}`
Returns full detail and live Stall Score for a single commitment.

### `GET /api/v1/commitments?status=Stalled`
Returns all commitments currently in a given status (`Committed`, `OnTrack`, `AtRisk`, `Stalled`, `Nudged`, `Escalated`, `Resolved`).

### `PATCH /api/v1/commitments/{commitment_id}/resolve`
Marks a commitment as resolved, closing out its lifecycle.

### `GET /api/v1/owners/{owner_id}/reliability`
Returns an owner's rolling on-time response rate and reliability adjustment factor.

### `GET /api/v1/briefs/latest`
Returns the most recently generated Pod Action Brief as structured JSON.

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/v1/commitments` | POST | Log a new commitment |
| `/api/v1/commitments/{id}` | GET | Get commitment detail + live score |
| `/api/v1/commitments` | GET | List/filter commitments |
| `/api/v1/commitments/{id}/resolve` | PATCH | Mark commitment resolved |
| `/api/v1/owners/{id}/reliability` | GET | Get owner reliability stats |
| `/api/v1/briefs/latest` | GET | Get the latest Action Brief |
| `/api/v1/briefs/{date}` | GET | Get a historical Action Brief by date |

---

## 💬 Teams / Slack Integration Details

EiChaser integrates natively with both Microsoft Teams and Slack, so nudges and briefs land exactly where teams already communicate — no new tool adoption required.

**Microsoft Teams** — uses the Microsoft Graph API (or Incoming Webhooks for simpler setups) to post:
- Direct 1:1 nudges to the stalled owner's Teams chat.
- The daily Pod Action Brief as an Adaptive Card in the pod's designated channel.

**Slack** — uses the Slack Web API (`chat.postMessage`) to post:
- Direct DMs to stalled owners.
- The daily Action Brief as a richly formatted Block Kit message in `#pod-action-briefs` (or a configurable channel).

Both integrations respect per-owner channel preference (some owners live in Teams, others in Slack) via the `owners.teams_user_id` / `owners.slack_user_id` mapping in the schema.

---

## 📋 Sample Action Brief Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 EICHASER — DAILY POD ACTION BRIEF
📅 Thursday, August 08, 2026 — 8:00 AM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 CRITICAL STALLS (2)
─────────────────────────────────────────────────
1. CASE-10234 — Platform Team (Owner: R. Mehta)
   Promised: "Root cause window by EOD yesterday"
   Stall Score: 96 | 18h overdue
   → Nudge sent 2x, no response

2. CASE-10298 — Infra Pod (Owner: A. Fernandes)
   Promised: "Re-verify patch by Wed 3PM"
   Stall Score: 91 | 6h overdue
   → Nudge sent 1x

🟠 STALLED (4)
─────────────────────────────────────────────────
3. CASE-10301 — Finance Ops (Owner: S. Kapoor) | Score: 78
4. CASE-10307 — Platform Team (Owner: R. Mehta) | Score: 71
5. CASE-10312 — Network Ops (Owner: D. Singh)  | Score: 69
6. CASE-10315 — Infra Pod (Owner: A. Fernandes) | Score: 66

🟡 WATCH LIST (3)
─────────────────────────────────────────────────
7. CASE-10320 — Score: 52   8. CASE-10322 — Score: 47   9. CASE-10325 — Score: 41

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Pattern flagged: R. Mehta appears on 2 of today's
   Critical/Stalled items — 3rd consecutive day.
   Recommend a direct check-in.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🖥 CLI Usage

```bash
# Log a commitment manually
eichaser commit --case CASE-10234 --owner OWNER-platform-01 \
    --text "Will confirm root cause window by EOD" \
    --expected-by "2026-08-08T18:00:00"

# Trigger a scoring cycle immediately
eichaser score --run-now

# View current stalled items
eichaser list --status stalled

# Generate today's Action Brief on demand
eichaser brief --generate --send

# Mark a commitment resolved
eichaser resolve --commitment CMT-88213
```

---

## 🧪 Testing Strategy

| Test Type | Coverage |
|---|---|
| **Unit — Stall Score** | Formula correctness across severity/reliability combinations, edge cases (0 elapsed time, score capping at 100) |
| **Unit — Escalation Rules** | Correct band assignment at every threshold boundary |
| **Unit — Reliability Adjustment** | Correct multiplier assignment across on-time-rate ranges |
| **Integration — Teams/Slack** | Mocked API calls verifying correct payload structure and delivery routing |
| **Integration — Ingestion** | Ticketing system connector correctly normalizes varied source schemas |
| **End-to-End** | Full lifecycle simulation: commitment logged → score rises → nudge fires → resolution closes the loop |

```bash
# Run full test suite
pytest tests/ -v

# Run only the scoring engine tests
pytest tests/unit/test_stall_score.py -v
```

---

## 🔐 Security & Compliance

- **No customer PII stored beyond what's necessary** — `customer_name` is the only customer-identifying field; all detail lives in the source ticketing system.
- **Secrets management** — all API tokens and credentials live in `.env` / a secrets manager, never committed to source control.
- **Audit trail** — the `status_history` and `nudges` tables provide a complete, immutable audit log of every commitment's lifecycle, useful for internal SLA compliance reviews.
- **Least-privilege API tokens** — Teams and Slack integration tokens are scoped to messaging-only permissions, not broader tenant access.

---

## 📈 Performance & Scalability

- **Batch scoring via Pandas** allows the Stall Score engine to recalculate thousands of open commitments per cycle in seconds, not minutes.
- **Indexed queries** (`stall_score DESC`, `status`, `owner_id`) keep dashboard and brief-generation queries fast even as the commitment ledger grows into the tens of thousands of historical records.
- **Stateless scoring workers** — the scoring cycle can be horizontally scaled (sharded by team or pod) if commitment volume grows significantly.

---

## 👁 Monitoring & Observability

Recommended metrics to track once deployed:

| Metric | Why It Matters |
|---|---|
| **Nudges sent per day** | Overall internal SLA discipline trend |
| **Average time-to-resolution after nudge** | How effective automated chasing actually is |
| **Repeat-offender rate** | Owners appearing in Critical/Stalled 3+ days running |
| **Escalation rate** | % of stalls that require manager intervention vs. self-resolve after nudge |
| **Scoring cycle latency** | Engine health — should stay well under the scheduled interval |

---

## 🎯 Impact & Metrics

> EiChaser standardized the unglamorous but critical process of internal follow-through, ensuring **zero customer-facing commitments breached their SLAs due to internal communication gaps.**

| Before EiChaser | After EiChaser |
|---|---|
| Commitments tracked in scattered chat threads | Centralized, queryable ledger of every promise made |
| Managers discover stalls only after customer escalation | Managers see risk proactively, every morning, before it becomes a problem |
| Chasing depends on individual memory & discipline | Chasing is automated, consistent, and never forgotten |
| No visibility into repeat-offender patterns | Reliability trends surfaced automatically for coaching |
| SLA breaches attributed vaguely to "communication gaps" | Every breach traceable to a specific, timestamped commitment and owner |

---

## ❓ Frequently Asked Questions

**Q: Does EiChaser replace the ticketing system?**
No. EiChaser is a layer *on top of* existing ticketing/case management systems — it tracks the internal commitment layer that ticketing systems typically don't model well.

**Q: Will people feel like they're being "watched" by a bot?**
The design principle here is transparency and psychological safety — nudges are polite, and visibility is framed as a shared team tool, not individual surveillance. The goal is proactive support, not blame.

**Q: What happens if an owner is out of office?**
Recommended extension: an out-of-office flag on the `owners` table that pauses Stall Score accrual and reroutes nudges to a designated backup owner.

**Q: Can thresholds be customized per team?**
Yes — see `config/sla_baselines.yaml` and `config/escalation_bands.yaml`, both fully configurable without code changes.

**Q: What ticketing systems does it integrate with?**
The ingestion layer is built to be source-agnostic via `ingestion/normalizer.py` — any system with an API or exportable case data can be connected.

---

## 🗺 Roadmap

- [ ] **Predictive stall forecasting** — flag commitments likely to stall *before* they even cross the At-Risk threshold, using historical owner/team patterns.
- [ ] **Self-serve web dashboard** — real-time view of all commitments, filterable by team, owner, severity, and score.
- [ ] **Grafana/metrics export** — plug scoring and nudge data into existing observability stacks.
- [ ] **Out-of-office aware routing** — automatic backup-owner reassignment when a primary owner is unavailable.
- [ ] **Natural-language commitment parsing** — auto-detect commitments directly from Teams/Slack thread text using lightweight NLP, reducing manual logging entirely.
- [ ] **Multi-language nudge templates** — for globally distributed support pods.
- [ ] **Weekly executive rollup** — trend view across pods for senior leadership, separate from the daily operational brief.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to update tests as appropriate, and run `pytest tests/` before submitting.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author & Contact

**Kaduri Ganesh**
Graduate Engineer | Silicon Architecture • Autonomous Robotics • AI Memory Systems • Financial Systems

- 🔗 GitHub: [github.com/GaneshEiGo](https://github.com/GaneshEiGo)
- 💼 LinkedIn: [linkedin.com/in/kaduri-ganesh-bbb327360](https://www.linkedin.com/in/kaduri-ganesh-bbb327360)
- 📧 Email: kaduriganesh7@gmail.com

---

## 🙏 Acknowledgments

- Every Support Engineer, Incident Manager, and Service Manager who has ever silently absorbed the mental load of "did I follow up on that?" — this project exists because that burden shouldn't fall on memory alone.
- The broader philosophy that **the most valuable engineering work is often the least glamorous** — building the boring, reliable infrastructure that quietly prevents problems no one ever hears about, because they never happened.

---

<div align="center">

### ⭐ If EiChaser's approach to internal SLA discipline resonates with you, consider starring the repo!

**Built with the belief that no customer promise should ever break because a human simply forgot.**

</div>
