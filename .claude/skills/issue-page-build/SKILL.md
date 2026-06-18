---
name: issue-page-build
description: "issue-factcheck가 확정한 판정·여론·출처를 SPEC §5 스키마의 issue.json으로 조립하고 tools/build_issue.py로 정적 페이지를 렌더한다. '페이지 만들어줘', '발행 준비', '<slug> 빌드', 판정 완료 후 발행 단계에서 이 스킬을 사용."
---

# issue-page-build — 발행 조립

확정된 검증물을 데이터 계약(issue.json)으로 굳히고 정적 페이지를 만든다. **스키마는 SPEC §5 단일 출처를 따른다 (임의 필드 추가·변경 금지).**

## Phase 1: issue.json 조립
`_workspace/<slug>/05_verdicts.md`·`05_opinion.md`·`00_config.md`를 근거로 `issues/<slug>/issue.json` 작성. 필드:
- `slug, title, summary, category, date_occurred, date_updated`
- `claims[]`: `{text, verdict, evidence, sources[{title,url}]}` — verdict는 5단계 중 하나, sources 최소 1개
- `timeline[]`: `{date, event}`
- `opinion`: `{note, quotes[{text, source, url}]}`
- `sources[]`: `{title, url}` (전체 출처)
- `method`: 수집 범위·한계(수집 못 한 소스 명시)

기존 시드 `issues/seed-sample/issue.json`을 모양 레퍼런스로 참고.

## Phase 2: 계약 검증
`python tools/build_issue.py issues/<slug>` 실행 → `issues/<slug>/index.html` 생성. JSON 파싱 오류·빈 verdict·빈 sources면 Phase 1로 반려.

## Phase 3: 인계
"index-build 로 인덱스 갱신 필요" 보고.

## 하드 규칙
- 스키마 변경은 위험 결정 → 멈추고 먼저 묻는다.
- 검증되지 않은 내용을 issue.json에 채우지 않는다(_workspace 근거 없는 문장 금지).
