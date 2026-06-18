---
name: issue-factcheck
description: "issue-research가 모은 _workspace/<slug>/ 자료에서 검증 가능한 주장(claim)을 추출하고, 교차검증한 뒤, 5단계 판정(사실/대체로 사실/논쟁/대체로 거짓/거짓)을 내린다. '판정해줘', '팩트체크 돌려줘', '<주제> 검증', 수집 완료 후 판정 단계로 넘어갈 때 이 스킬을 사용. 이 플랫폼의 핵심 스킬."
---

# issue-factcheck — 판정 오케스트레이터 ★ 핵심

LOOP의 **작업자↔채점자 분리**를 그대로 구현한다. 작업자(추출·교차검증)가 만들고, 채점자(판정·QA)가 기준으로만 검증한다. 채점자는 반려할 수 있다.

## Phase 0: 전제
- `_workspace/<slug>/03_*.md` 수집물 존재 확인. 없으면 issue-research 먼저.

## Phase 1: 작업자 — 주장 추출 (claim-extractor)
수집물에서 *검증 가능한 사실 주장*만 추출(의견·전망·가치판단은 claim이 아니라 여론으로 분류). 각 claim에 원자료 출처를 첨부 → `_workspace/<slug>/04_claims.md`.

## Phase 2: 작업자 — 교차검증 (cross-verifier)
각 claim을 *독립된 2개 이상 출처*로 대조. 1차 출처(통계청·공공기관·원문) 우선. 출처 충돌·단일출처는 표시 → `_workspace/<slug>/04_verify.md`.

## Phase 3: 채점자 — 판정 (verdict-adjudicator)
교차검증 결과를 기준으로만 5단계 verdict 부여. 근거(evidence)와 출처를 claim마다 명시. **단일 출처·1차 출처 부재·전망/추정은 '사실'로 올리지 않는다.** → `_workspace/<slug>/05_verdicts.md`

## Phase 4: 여론 맥락 (opinion-curator)
사실 판정과 분리해, 대표 인용 2~4개를 출처와 함께 정리(찬반/감성은 중립적으로). → `_workspace/<slug>/05_opinion.md`

## Phase 5: 채점자 게이트 (qa-validator)
`LOOP_factcheck.md` 체크리스트로 항목별 통과/실패 판정. 실패 시 해당 단계로 반려(동일 항목 3회 반려 시 중단하고 사용자에게 묻는다). 전 항목 통과해야 다음.

## Phase 6: 인계
판정·여론·출처가 확정되면 "issue-page-build 로 발행 가능" 보고. 이 스킬은 페이지를 만들지 않는다.

## 하드 규칙
- 검증 안 된 claim 발행 금지. 출처 없는 verdict 금지. 데이터 밖 인과 단정 금지.
- verdict 변경·기준 완화는 위험 결정 → 멈추고 먼저 묻는다.
