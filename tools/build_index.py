#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""전 이슈 issue.json → index.json (+ index-data.js)

index.json  : 검색 매니페스트 (SPEC §5). 표준 산출물.
index-data.js : 같은 데이터를 window.ISSUES_INDEX 로 노출 (file://에서 fetch 없이 로드).

자체 점검: 매니페스트 수 == issues/ 디렉토리 수, 모든 url이 실재 파일.

사용: python tools/build_index.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISSUES = ROOT / "issues"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def make_entry(data: dict, slug: str) -> dict:
    claims = data.get("claims", [])
    quotes = [q.get("text", "") for q in data.get("opinion", {}).get("quotes", [])]
    blob_parts = [data.get("title", ""), data.get("summary", "")]
    blob_parts += [c.get("text", "") for c in claims]
    blob_parts += quotes
    return {
        "slug": slug,
        "title": data.get("title", ""),
        "summary": data.get("summary", ""),
        "category": data.get("category", ""),
        "date_occurred": data.get("date_occurred", ""),
        "date_updated": data.get("date_updated", ""),
        "claims": [{"text": c.get("text", ""), "verdict": c.get("verdict", "")} for c in claims],
        "quotes": quotes,
        "search_blob": norm(" ".join(blob_parts)),
        "url": "issues/%s/index.html" % slug,
    }


def main():
    issue_dirs = sorted(p.parent for p in ISSUES.glob("*/issue.json"))
    entries = []
    for d in issue_dirs:
        data = json.loads((d / "issue.json").read_text(encoding="utf-8"))
        entries.append(make_entry(data, d.name))

    # 최신순 기본 정렬
    entries.sort(key=lambda e: e.get("date_updated", ""), reverse=True)

    # ── 자체 점검 ──
    errors = []
    if len(entries) != len(issue_dirs):
        errors.append("count mismatch: %d entries vs %d dirs" % (len(entries), len(issue_dirs)))
    for e in entries:
        if not (ROOT / e["url"]).exists():
            errors.append("broken url (no rendered page): %s — build_issue.py 먼저 실행" % e["url"])
        for c in e["claims"]:
            if not c["verdict"]:
                errors.append("empty verdict in %s" % e["slug"])
    if errors:
        print("BUILD FAIL:")
        for x in errors:
            print("  -", x)
        return 1

    (ROOT / "index.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    js = "window.ISSUES_INDEX = " + json.dumps(entries, ensure_ascii=False) + ";\n"
    (ROOT / "index-data.js").write_text(js, encoding="utf-8")

    print("index built: %d issue(s)" % len(entries))
    for e in entries:
        print("  -", e["slug"], "(%s)" % e["date_updated"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
