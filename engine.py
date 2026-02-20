import csv
from dataclasses import dataclass, asdict
from typing import List, Dict


@dataclass
class Podcast:
    name: str
    host: str
    topics: str
    audience: str
    style: str


def load_podcasts(path: str) -> List[Dict]:
    rows: List[Dict] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = Podcast(**row)
            rows.append(asdict(p))
    return rows


def _tokenize(text: str) -> set:
    return {t.strip().lower() for t in text.replace(",", " ").split() if t.strip()}


def score_podcasts(podcasts: List[Dict], product: str, audience: str, angle: str) -> List[Dict]:
    product_tokens = _tokenize(product)
    audience_tokens = _tokenize(audience)
    angle_tokens = _tokenize(angle)

    scored = []
    for p in podcasts:
        topic_tokens = _tokenize(p["topics"])
        aud_tokens = _tokenize(p["audience"])
        style_tokens = _tokenize(p["style"])

        topic_match = len(product_tokens & topic_tokens)
        audience_match = len(audience_tokens & aud_tokens)
        angle_match = len(angle_tokens & style_tokens)

        score = topic_match * 4 + audience_match * 3 + angle_match * 2
        reasons = []
        if topic_match:
            reasons.append(f"Topic overlap ({topic_match})")
        if audience_match:
            reasons.append(f"Audience fit ({audience_match})")
        if angle_match:
            reasons.append(f"Style match ({angle_match})")
        if not reasons:
            reasons.append("Broad B2B relevance")

        scored.append({**p, "score": score, "reasons": reasons})

    return sorted(scored, key=lambda x: x["score"], reverse=True)


def generate_email(podcast: Dict, product: str, audience: str, angle: str) -> str:
    return (
        f"Hi {podcast['host']},\\n\\n"
        f"I’m building {product} for {audience}. I think your audience at {podcast['name']} "
        f"would benefit from a tactical episode around {angle}.\\n\\n"
        "Potential talking points:\\n"
        "- What’s broken in the current workflow\\n"
        "- A step-by-step implementation playbook\\n"
        "- Real outcomes and mistakes to avoid\\n\\n"
        "If useful, I can share a 5-bullet episode outline tailored to your listeners.\\n\\n"
        "Best,\\n"
        "[Your Name]"
    )
