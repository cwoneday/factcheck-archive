# 사회 이슈 팩트체크 아카이브

검증된 사실을 전면에 두고 검색하는 정적 팩트체크 플랫폼. 각 사회 이슈를 다중 에이전트 하네스로 수집·교차검증해 자기완결 정적 페이지로 발행하고, 키워드·날짜로 검색한다.

- **원칙:** 출처 추적성 · 날조 0 · 정직한 한계 · 중립 · 데이터 밖 단정 금지.
- **기술:** 순수 HTML/CSS/vanilla JS (외부 라이브러리 0). `file://`로도 열린다. GitHub Pages 배포.

## 구조
- `index.html` — 허브 (검색 + 정렬 + 이슈 카드)
- `issues/<slug>/` — 이슈별 페이지(`index.html`)와 데이터(`issue.json`)
- `index.json` — 검색 매니페스트 (`python tools/build_index.py`로 생성)
- `.claude/` — 리서치·팩트체크·빌드 하네스
- `SPEC.md` / `CLAUDE.md` / `LOOP_factcheck.md` — 설계·거버넌스

## 새 이슈 추가
1. 하네스 실행으로 `issues/<slug>/issue.json` + `index.html` 생성
2. `python tools/build_index.py` 로 `index.json` 재생성
3. 커밋·푸시
