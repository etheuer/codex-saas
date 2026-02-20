# PodHunt Briefs — Micro SaaS MVP

PodHunt Briefs helps B2B founders find high-fit podcasts and generate personalized outreach emails in minutes.

## 1) Niche Research: Why this market

### Target niche
- **ICP:** Bootstrapped B2B SaaS founders with < $20k MRR who use podcasts as a growth channel.
- **Buyer pain:** They spend hours manually searching for podcasts, then send generic pitches with low reply rates.

### Unmet need
Most tools either:
1. only provide podcast directories with no fit scoring, or
2. generate generic AI outreach without host-specific context.

Founders need a tool that converts a short product description into:
- ranked podcast targets,
- explicit match reasons,
- ready-to-send host-personalized emails.

### Initial moat
- **Workflow moat:** fit scoring + outreach generation in one flow.
- **Data moat (compounding):** every accepted/rejected recommendation can improve future ranking.
- **Niche positioning moat:** focused only on B2B founder guesting use case (faster time-to-value than generic media databases).

## 2) Business model

- **Price:** $29/month starter (up to 50 recommendations/month).
- **First-$100 target:** 4 paying customers.
- **Acquisition path:** direct founder outreach + startup communities + partner with podcast booking freelancers.

## 3) What’s implemented in this repo

- Python web app MVP with:
  - niche-aware podcast fit scoring,
  - ranked recommendations,
  - outreach email draft generation.
- Seed dataset of B2B-relevant podcasts.
- Lightweight tests for ranking and email generation.
- A practical 14-day GTM execution plan.

## 4) Run locally

```bash
python app.py
```

Open http://127.0.0.1:5000

## 5) Test

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

## 6) Mission progress toward first $100

- ✅ Selected a clear niche and unmet need.
- ✅ Built a working MVP users can try immediately.
- ✅ Prepared execution-ready GTM assets to start customer acquisition.
- ✅ Added a full GTM strategy document for 90-day execution in `go_to_market/go_to_market_document.md`.
- ⏳ Real-world customer conversion requires external execution (outreach/sales), which is prepared in `go_to_market/`.
