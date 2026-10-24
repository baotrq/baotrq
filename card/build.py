"""Draw the neofetch-style profile card (card/dark.svg, card/light.svg).

Run by .github/workflows/card.yml every night. Stats come from the GitHub API with
ACCESS_TOKEN (a read-only personal token, adds private repos) or the Action's GITHUB_TOKEN.
With no token it still draws the card, with the stats left as "-".
"""
import calendar
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.request
from html import escape
from pathlib import Path

USER = "baotrq"
BIRTHDAY = dt.date(2005, 3, 11)  # drives the "Uptime" row
HERE = Path(__file__).parent

# Right-hand column. A str is a section header, None a blank line, (key, value) a row,
# and a pair of rows in one tuple prints side by side.
ROWS = [
    ("OS", "Windows, macOS, Ubuntu Linux, Android"),
    ("Uptime", "{age}"),
    ("Host", "VinRobotics"),
    ("Kernel", "Foundation AI / VLA Research Intern"),
    ("School", "RMIT Vietnam, Robotics & Mechatronics (Hons)"),
    ("IDE", "VS Code, Claude Code, Simplicity Studio"),
    None,
    ("Languages.Programming", "Python, C/C++, Kotlin, TypeScript"),
    ("Languages.Hardware", "ESP32, EFR32, Raspberry Pi"),
    ("Languages.Real", "Vietnamese, English"),
    None,
    ("Hobbies.Court", "Basketball, Wed / Fri / Sun"),
    ("Hobbies.Desk", "3D printing, building gadgets"),
    ("Awards", "2 × FPT IoT Challenge podium, NEO League"),
    "- Contact",
    ("Email", "tdmbao2005@gmail.com"),
    ("Portfolio", "baotrq.github.io/Personal-Portfolio"),
    ("ONBOOTH", "onboothvn.com"),
    "- GitHub Stats",
    (("Repos", "{repos}"), ("Stars", "{stars}")),
    (("Commits", "{commits}"), ("Followers", "{followers}")),
    ("Lines of Code on GitHub", "{loc}"),
]

THEMES = {
    "dark": {"bg": "#161b22", "text": "#c9d1d9", "key": "#ffa657", "value": "#a5d6ff",
             "dots": "#616e7f", "add": "#3fb950", "del": "#f85149"},
    "light": {"bg": "#f6f8fa", "text": "#24292f", "key": "#953800", "value": "#0a3069",
              "dots": "#c2cfde", "add": "#1a7f37", "del": "#cf222e"},
}

WIDTH = 60    # characters in the right-hand column
LINE = 20     # px between lines
TEXT_X = 390  # px where the right-hand column starts
# At 16px, Consolas (+9% size-adjust) and Menlo / DejaVu Sans Mono are all ~9.6px a character:
# 38 columns of art end at ~380px, before TEXT_X, and 60 columns of text end at ~966px of 985.
ART_COLS = 38


def age(today: dt.date, born: dt.date = BIRTHDAY) -> str:
    months = (today.year - born.year) * 12 + today.month - born.month - (today.day < born.day)
    y, m = divmod(born.month - 1 + months, 12)
    year, month = born.year + y, m + 1
    anchor = dt.date(year, month, min(born.day, calendar.monthrange(year, month)[1]))
    plural = lambda n, unit: f"{n} {unit}{'' if n == 1 else 's'}"
    return f"{plural(months // 12, 'year')}, {plural(months % 12, 'month')}, {plural((today - anchor).days, 'day')}"


def gh(token: str, url: str, body: dict | None = None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": f"bearer {token}",
                                          "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read() or b"null")


def graphql(token: str, query: str) -> dict:
    body = gh(token, "https://api.github.com/graphql", {"query": query, "variables": {"login": USER}})[1]
    if body.get("errors"):
        raise RuntimeError(body["errors"])
    return body["data"]["user"]


def lines_of_code(token: str, repo: str) -> tuple[int, int]:
    # GitHub computes contributor stats lazily and answers 202 until they're ready.
    for _ in range(5):
        try:
            status, authors = gh(token, f"https://api.github.com/repos/{repo}/stats/contributors")
        except urllib.error.HTTPError:  # no access with this token, or an empty repo
            return 0, 0
        if status == 200:
            break
        time.sleep(3)
    else:
        return 0, 0
    for author in authors or []:
        if (author.get("author") or {}).get("login", "").lower() == USER.lower():
            return sum(w["a"] for w in author["weeks"]), sum(w["d"] for w in author["weeks"])
    return 0, 0


def stats(token: str) -> dict:
    user = graphql(token, """query($login: String!) { user(login: $login) {
      followers { totalCount }
      contributionsCollection { contributionYears }
      repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
        totalCount nodes { nameWithOwner stargazerCount } } } }""")
    repos = user["repositories"]  # ponytail: first 100 repos only; paginate past 100
    commits = 0
    for year in user["contributionsCollection"]["contributionYears"]:
        cc = graphql(token, f"""query($login: String!) {{ user(login: $login) {{
          contributionsCollection(from: "{year}-01-01T00:00:00Z", to: "{year}-12-31T23:59:59Z") {{
            totalCommitContributions restrictedContributionsCount }} }} }}""")["contributionsCollection"]
        commits += cc["totalCommitContributions"] + cc["restrictedContributionsCount"]
    added = deleted = 0
    for node in repos["nodes"]:
        a, d = lines_of_code(token, node["nameWithOwner"])
        added, deleted = added + a, deleted + d
    return {"repos": f"{repos['totalCount']:,}",
            "stars": f"{sum(n['stargazerCount'] for n in repos['nodes']):,}",
            "commits": f"{commits:,}", "followers": f"{user['followers']['totalCount']:,}",
            "loc": f"{added - deleted:,}", "add": f"{added:,}", "del": f"{deleted:,}"}


def span(cls: str, text: str) -> str:
    return f'<tspan class="{cls}">{escape(text)}</tspan>'


def row(key: str, value: str, width: int, lead: bool = True) -> str:
    """`. Key: ....... value`, padded with dots to exactly `width` characters."""
    keys = ".".join(span("key", k) for k in key.split("."))
    dots = width - len(key) - len(value) - (4 if lead else 2) - 1
    assert dots >= 1, f"row too long for the card: {key}: {value}"
    return (span("dots", ". ") if lead else "") + keys + ":" + span("dots", " " + "." * dots + " ") + span("value", value)


def render(theme: dict, ascii_lines: list[str], data: dict) -> str:
    lines = [span("text", f"{USER}@github ") + span("text", "—" * (WIDTH - len(USER) - 8))]
    for item in ROWS:
        if item is None:
            lines.append(span("dots", ". "))
        elif isinstance(item, str):
            lines.append(span("text", f"{item} " + "—" * (WIDTH - len(item) - 1)))
        elif isinstance(item[0], tuple):
            (k1, v1), (k2, v2) = item
            half = WIDTH // 2
            lines.append(row(k1, v1.format(**data), half - 1) + span("dots", " | ")
                         + row(k2, v2.format(**data), WIDTH - half - 2, lead=False))
        elif item[0].startswith("Lines of Code"):
            tail = f" ( {data['add']}++, {data['del']}-- )"
            lines.append(row(item[0], item[1].format(**data), WIDTH - len(tail))
                         + " ( " + span("add", data["add"] + "++") + ", " + span("del", data["del"] + "--") + " )")
        else:
            lines.append(row(item[0], item[1].format(**data), WIDTH))
    height = max(len(ascii_lines), len(lines)) * LINE + 25
    art = "".join(f'<tspan x="15" y="{30 + i * LINE}">{escape(l)}</tspan>\n' for i, l in enumerate(ascii_lines))
    info = "".join(f'<tspan x="{TEXT_X}" y="{30 + i * LINE}">{l}</tspan>\n' for i, l in enumerate(lines))
    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,'DejaVu Sans Mono',monospace" width="985px" height="{height}px" font-size="16px">
<style>
@font-face {{ src: local('Consolas'), local('Consolas Bold'); font-family: 'ConsolasFallback'; font-display: swap; size-adjust: 109%; }}
.text {{fill: {theme['text']};}} .key {{fill: {theme['key']};}} .value {{fill: {theme['value']};}}
.dots {{fill: {theme['dots']};}} .add {{fill: {theme['add']};}} .del {{fill: {theme['del']};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="985px" height="{height}px" fill="{theme['bg']}" rx="15"/>
<text x="15" y="30" fill="{theme['text']}">
{art}</text>
<text x="{TEXT_X}" y="30" fill="{theme['text']}">
{info}</text>
</svg>
"""


def main() -> None:
    data = {"age": age(dt.date.today()),
            **dict.fromkeys(("repos", "stars", "commits", "followers", "loc", "add", "del"), "-")}
    token = os.environ.get("ACCESS_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        try:
            data.update(stats(token))
        except Exception as e:  # keep drawing the card; the stats just stay "-" this run
            print(f"stats failed: {e}", file=sys.stderr)
    ascii_lines = (HERE / "ascii.txt").read_text(encoding="utf-8").splitlines()
    assert max(map(len, ascii_lines)) <= ART_COLS, f"ascii.txt is wider than {ART_COLS} columns"
    for name, theme in THEMES.items():
        (HERE / f"{name}.svg").write_text(render(theme, ascii_lines, data), encoding="utf-8")


if __name__ == "__main__":
    # self-check: month ends, leap days, the birthday itself
    assert age(dt.date(2026, 1, 31), dt.date(2005, 1, 31)) == "21 years, 0 months, 0 days"
    assert age(dt.date(2026, 3, 1), dt.date(2005, 1, 31)) == "21 years, 1 month, 1 day"
    assert age(dt.date(2027, 2, 28), dt.date(2004, 2, 29)) == "22 years, 11 months, 30 days"
    assert age(dt.date(2026, 10, 24), dt.date(2005, 10, 25)) == "20 years, 11 months, 29 days"
    main()
