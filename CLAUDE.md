# CLAUDE.md — 사회 이슈 팩트체크 아카이브

## 정체성
"검증된 사실을 전면에 두고 검색하는 정적 플랫폼." 각 사회 이슈를 fable식으로 1건씩 수집·교차검증해 정적 페이지로 발행하고, 그 위에 검색 가능한 인덱스를 둔다. PolitiFact·스놉스 계열이되 여론 지형을 맥락으로 함께 보여준다.

## 절대 원칙 (생존 조건)
- **출처 추적성** — 모든 claim·판정·인용은 원본 URL로 추적 가능.
- **날조 0** — 검증 안 된 것은 발행하지 않는다.
- **정직한 한계** — 수집 못 한 소스는 각 이슈 메서드에 명시.
- **중립** — 사실 검증이지 입장 표명이 아니다.
- **데이터 밖 단정 금지.**

## 거버넌스 우선순위
`LOOP_factcheck.md`(도메인 체크리스트)를 LOOP 기본 체크리스트보다 우선 적용한다.

## 레포 구조
- `index.html` / `search.js` / `style.css` — 허브(검색·정렬·카드 그리드)
- `index.json` — 검색 매니페스트 (`tools/build_index.py`가 자동 생성)
- `issues/<slug>/issue.json` — 이슈 데이터 (계약), `issues/<slug>/index.html` — 이슈 페이지
- `_workspace/` — 하네스 수집·분석 원본(.md)
- `.claude/` — 리서치·팩트체크·빌드 하네스
- `SPEC.md` — 설계 스펙 v1.0.0

## 데이터 계약
`issue.json`/`index.json` 스키마는 SPEC §5를 단일 출처로 따른다. 스키마 변경은 위험 결정 → 멈추고 먼저 묻는다.

## 빌드
이슈를 추가/수정한 뒤에는 `python tools/build_index.py` 를 돌려 `index.json`을 재생성한다. 사이트 자체는 외부 라이브러리 0 (build_index.py는 개발용 도구이지 사이트 런타임 의존이 아니다).

## 환경
Windows PowerShell. 명령 연결은 `;`. 한글 파일 읽기는 `-Encoding UTF8`.
