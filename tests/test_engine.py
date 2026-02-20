import unittest

from engine import score_podcasts, generate_email


class EngineTests(unittest.TestCase):
    def test_scoring_orders_best_match_first(self):
        podcasts = [
            {
                "name": "A",
                "host": "Host A",
                "topics": "saas churn retention",
                "audience": "b2b founders",
                "style": "tactical framework",
            },
            {
                "name": "B",
                "host": "Host B",
                "topics": "wellness nutrition",
                "audience": "consumers",
                "style": "story",
            },
        ]

        ranked = score_podcasts(
            podcasts,
            product="churn retention saas",
            audience="b2b founders",
            angle="tactical framework",
        )

        self.assertEqual(ranked[0]["name"], "A")
        self.assertGreater(ranked[0]["score"], ranked[1]["score"])

    def test_generate_email_contains_personalization(self):
        podcast = {
            "name": "SaaS Growth Lab",
            "host": "Elena",
        }

        email = generate_email(
            podcast,
            product="PodHunt Briefs",
            audience="B2B founders",
            angle="podcast guest fit scoring",
        )

        self.assertIn("Hi Elena", email)
        self.assertIn("SaaS Growth Lab", email)
        self.assertIn("PodHunt Briefs", email)


if __name__ == "__main__":
    unittest.main()
