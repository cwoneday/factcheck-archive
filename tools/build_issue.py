#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""issue.json → issues/<slug>/index.html (데이터 인라인 주입; file://로도 열림)

사용:
  python tools/build_issue.py issues/seed-sample      # 한 이슈
  python tools/build_issue.py --all                   # 전체 이슈
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "tools" / "issue_template.html").read_text(encoding="utf-8")


def build_one(issue_dir: Path) -> str:
    data_path = issue_dir / "issue.json"
    data = json.loads(data_path.read_text(encoding="utf-8"))
    # 인라인 주입: </script> 깨짐 방지를 위해 < 를 이스케이프
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.replace("__ISSUE_DATA__", payload).replace("__TITLE__", data.get("title", ""))
    (issue_dir / "index.html").write_text(html, encoding="utf-8")
    return data.get("slug", issue_dir.name)


def main(argv):
    if not argv:
        print("usage: build_issue.py <issue_dir> | --all"); return 1
    if argv[0] == "--all":
        dirs = [p.parent for p in (ROOT / "issues").glob("*/issue.json")]
    else:
        dirs = [ROOT / argv[0]]
    for d in dirs:
        slug = build_one(d)
        print("built:", slug, "->", (d / "index.html").relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
