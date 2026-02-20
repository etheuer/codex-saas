from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from html import escape

from engine import load_podcasts, score_podcasts, generate_email

PODCASTS = load_podcasts("data/podcasts.csv")


def render_page(results=None, product="", audience="", angle=""):
    results = results or []
    cards = ""
    for r in results:
        reasons = ", ".join(r["reasons"])
        cards += f"""
        <div class=\"card\">
          <h3>{escape(r['name'])} <span class=\"score\">(Score: {r['score']})</span></h3>
          <p><strong>Host:</strong> {escape(r['host'])}</p>
          <p><strong>Why fit:</strong> {escape(reasons)}</p>
          <pre>{escape(r['email'])}</pre>
        </div>
        """

    return f"""<!doctype html>
<html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
<title>PodHunt Briefs</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 2rem auto; max-width: 980px; color: #1c1c1c; }}
h1 {{ margin-bottom: .2rem; }} .muted {{ color: #555; }}
form {{ display: grid; gap: .75rem; margin: 1.25rem 0 2rem; }}
input, textarea {{ padding: .65rem; border: 1px solid #cfcfcf; border-radius: 8px; font-size: 1rem; }}
button {{ width: fit-content; padding: .6rem 1rem; border: 0; border-radius: 8px; background: #0d6efd; color: #fff; font-weight: 600; cursor: pointer; }}
.card {{ border: 1px solid #ddd; border-radius: 12px; padding: 1rem; margin-bottom: 1rem; }}
.score {{ font-weight: 700; }} pre {{ white-space: pre-wrap; background: #fafafa; padding: .75rem; border-radius: 8px; border: 1px dashed #ddd; }}
</style></head><body>
<h1>PodHunt Briefs</h1>
<p class=\"muted\">Find high-fit podcasts for your B2B SaaS and generate personalized outreach drafts.</p>
<form method=\"post\">
<input name=\"product\" placeholder=\"What do you build? (e.g., churn analytics SaaS)\" value=\"{escape(product)}\" required />
<input name=\"audience\" placeholder=\"Who do you serve? (e.g., B2B SaaS founders)\" value=\"{escape(audience)}\" required />
<textarea name=\"angle\" rows=\"3\" placeholder=\"Episode angle to pitch\" required>{escape(angle)}</textarea>
<button type=\"submit\">Find podcast targets</button></form>
{cards}
</body></html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(render_page().encode("utf-8"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        data = parse_qs(body)

        product = data.get("product", [""])[0].strip()
        audience = data.get("audience", [""])[0].strip()
        angle = data.get("angle", [""])[0].strip()

        ranked = score_podcasts(PODCASTS, product, audience, angle)
        top = ranked[:8]
        results = [{**item, "email": generate_email(item, product, audience, angle)} for item in top]

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(render_page(results, product, audience, angle).encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), Handler)
    print("Running on http://127.0.0.1:5000")
    server.serve_forever()
