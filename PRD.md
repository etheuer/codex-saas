# Product Requirements Document (PRD)
## Product: PodHunt Briefs
## Version: v1.0 (MVP-to-Growth)
## Date: 2026-02-20
## Owner: Product

---

## 1) Purpose
PodHunt Briefs helps early-stage B2B SaaS founders identify high-fit podcasts and generate host-personalized outreach emails quickly. This PRD defines the product requirements for the next iteration from MVP toward repeatable customer value and paid conversion.

## 2) Problem Statement
Bootstrapped B2B founders want podcast guest appearances for distribution, trust, and lead generation. Existing options are either broad directories without relevance ranking or AI writing tools that output generic pitches. The result is a slow manual workflow and low outreach response rates.

## 3) Goals and Success Metrics

### 3.1 Product Goals
1. Reduce time required to build a podcast outreach list from hours to minutes.
2. Improve outreach quality by generating host-contextualized email drafts.
3. Create a reliable, measurable workflow that supports paid subscription conversion.

### 3.2 Business Goals (first phase)
1. Convert at least 4 paying users at $29/month (first $100+ MRR milestone).
2. Reach weekly active usage among trial users by delivering clear first-session value.

### 3.3 KPIs
- **Time-to-first-shortlist (TTFS):** median < 5 minutes.
- **Recommendation acceptance rate:** % of suggested podcasts users mark as relevant.
- **Email send intent rate:** % of generated drafts copied/exported by users.
- **Trial-to-paid conversion rate:** % of users converting within 14 days.
- **Weekly active users (WAU):** users generating at least one list or email per week.

## 4) Target Users

### Primary Persona: Bootstrapped B2B SaaS Founder
- MRR: pre-$20k.
- Team size: solo or small team.
- Constraints: low budget, limited time, no dedicated PR staff.
- Desired outcomes: qualified podcast appearances and pipeline/reputation growth.

### Secondary Persona: Podcast Booking Freelancer
- Uses tool across multiple founder clients.
- Needs repeatable matching and scalable personalization.

## 5) Scope

### 5.1 In Scope (MVP+)
1. Founder inputs product details and target audience.
2. System ranks podcasts by relevance with transparent scoring reasons.
3. System generates personalized outreach emails for selected podcasts.
4. User can copy/export recommendations and email drafts.
5. Basic feedback capture (relevant / not relevant) for future model tuning.

### 5.2 Out of Scope (for now)
1. Automated email sending or inbox integrations.
2. CRM integrations.
3. Large-scale podcast crawling infrastructure.
4. Multi-language localization.
5. Team permissions/roles.

## 6) User Journey
1. User lands on app and submits short company/product description.
2. User adds niche, target audience, and desired podcast themes.
3. System returns ranked podcast list with fit scores and rationale.
4. User selects a podcast and generates a personalized outreach draft.
5. User copies the email and sends via their own email workflow.
6. User marks recommendations as useful/not useful.

## 7) Functional Requirements

### FR-1 Input Capture
- User can provide:
  - product description,
  - customer segment,
  - core topics/expertise,
  - preferred podcast size/tier (optional).
- Input validation prevents empty submissions.

### FR-2 Podcast Recommendation Engine
- System ranks podcasts using niche-fit scoring.
- Each recommendation includes:
  - podcast name,
  - fit score,
  - concise reason(s) for match.
- Results sorted descending by fit score.

### FR-3 Personalized Outreach Draft Generation
- User can generate a draft per recommended podcast.
- Draft must include:
  - host/podcast contextual mention,
  - relevant founder/topic angle,
  - concise call-to-action.
- Output must avoid generic template tone as much as possible.

### FR-4 User Feedback Loop
- User can tag recommendation as relevant / not relevant.
- Feedback is stored for later tuning and analysis.

### FR-5 Usage Limits and Plans
- Starter plan supports up to 50 recommendations per month.
- Clear indication shown when user approaches/exceeds limit.

### FR-6 Basic Analytics Events
Track events:
- `input_submitted`
- `recommendations_generated`
- `recommendation_marked_relevant`
- `email_generated`
- `email_copied`
- `paywall_viewed`

## 8) Non-Functional Requirements
- **Performance:** recommendation response target under 3 seconds for seed-scale dataset.
- **Reliability:** graceful error messaging for failed generations.
- **Usability:** complete end-to-end workflow in <= 6 user actions after input.
- **Security:** no secrets in client-side code; basic request validation.
- **Maintainability:** modular ranking and email generation logic with unit test coverage.

## 9) UX Requirements
- Clear single-page flow with three primary states:
  1. input form,
  2. ranked results,
  3. outreach drafts.
- Fit reasons displayed in plain language.
- Copy-to-clipboard action for email with clear success feedback.
- Empty/error states with actionable guidance.

## 10) Data Requirements

### Inputs
- User profile and product description fields.
- Seed podcast metadata (title, focus, audience, style, host notes).

### Outputs
- Ranked podcast recommendation list with scores and reasons.
- Generated outreach drafts.
- User feedback labels.

### Storage (phase-appropriate)
- Lightweight persistence for:
  - user usage counts,
  - feedback labels,
  - analytics events.

## 11) Dependencies
- Quality and freshness of podcast seed data.
- Prompt/template quality for personalization.
- Basic web app hosting and usage tracking.

## 12) Risks and Mitigations
1. **Risk:** recommendations feel too generic.
   - **Mitigation:** expand niche-specific metadata and scoring weights.
2. **Risk:** generated emails are repetitive.
   - **Mitigation:** diversify templates and incorporate podcast-specific tokens.
3. **Risk:** low conversion from free use to paid.
   - **Mitigation:** strengthen paywalled value (saved lists, higher limits, better personalization).
4. **Risk:** limited data coverage reduces trust.
   - **Mitigation:** add podcast ingestion cadence and visible data recency.

## 13) Milestones

### M1 — Productized MVP (1–2 weeks)
- Stabilize ranking and draft generation flow.
- Instrument core analytics events.
- Add usage limits.

### M2 — Conversion Readiness (2–4 weeks)
- Improve personalization quality.
- Add relevant/not relevant feedback capture.
- Launch pricing + upgrade prompt.

### M3 — Early Retention Loop (4–6 weeks)
- Save previous recommendations.
- Improve reranking using aggregate feedback.
- Add simple weekly usage summary for users.

## 14) Acceptance Criteria (Release Gate)
1. User can submit inputs and receive ranked podcast recommendations with reasons.
2. User can generate at least one host-personalized outreach draft per recommendation.
3. Median TTFS under 5 minutes in internal dogfooding.
4. Analytics events fire for key funnel actions.
5. Unit tests pass for ranking and draft generation core paths.

## 15) Open Questions
1. Should plan limits be recommendation-count-based, draft-count-based, or both?
2. What minimum dataset size ensures perceived recommendation quality?
3. Which personalization dimensions (host tone, recent episodes, audience stage) most impact response rate?
4. Should we prioritize CRM export before automated outreach sending?

---

## Appendix: Initial User Stories
1. As a founder, I want ranked podcast suggestions so I can prioritize outreach quickly.
2. As a founder, I want concrete fit reasons so I can trust recommendations.
3. As a founder, I want personalized email drafts so I can send better pitches faster.
4. As a freelancer, I want repeatable workflows so I can serve multiple clients efficiently.
