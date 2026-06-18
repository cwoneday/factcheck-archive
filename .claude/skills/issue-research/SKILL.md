---
name: issue-research
description: "사회 이슈 하나에 대한 공식·언론·커뮤니티/SNS·학계 자료를 다중 에이전트로 병렬 수집해 _workspace/<slug>/ 에 정리한다. '이슈 조사해줘', '<주제> 자료 모아줘', '<주제> 팩트체크 시작', 새 이슈 추가, 재수집·보완 요청 시 이 스킬을 사용. 수집만 담당하며, 판정은 issue-factcheck가 이어받는다."
---

# issue-research — 수집 오케스트레이터

사회 이슈 1건의 원자료를 4개 수집 에이전트가 병렬로 모은다. 산출물은 _workspace/<slug>/ 의 마크다운. **수집은 출처 URL과 함께만 기록한다 (출처 없는 문장 금지).**

## Phase 0: 컨텍스트
- slug 결정(영문 케밥, 예: `2023-fertility-rate`). 이슈 한 줄 정의·수집 기간을 확정.
- `_workspace/<slug>/` 존재 시: 부분 보완이면 해당 에이전트만 재실행, 전체 재수집이면 `_workspace/<slug>_backup_<날짜>/`로 이동 후 새로.

## Phase 1: 준비
- `_workspace/<slug>/00_config.md` 생성: slug, 이슈 정의, 수집 기간, 실행 시각, 대상 언어.
- `.claude/agents/` 의 수집 에이전트 4종 존재 확인.

## Phase 2: 에이전트 로드
각 에이전트 정의(`official-collector`, `press-collector`, `community-collector`, `academic-collector`)를 Read해 역할·프로토콜 파악.

## Phase 3: 병렬 수집 (서브 에이전트)
4개 에이전트 동시 실행. 공통 컨텍스트: slug·이슈 정의·수집 기간·작업 디렉토리. 각 에이전트는 정의 파일을 먼저 Read하고 Policy대로 실행, 완료 시 `_workspace/<slug>/03_<agent>.md`에 저장.

산출 형식(각 항목): `주장/사실 후보 · 원문 인용(15어 이내) · 출처 URL · 수집일`. 수집 못 한 소스는 파일 끝 "수집 한계" 섹션에 명시(날조 0, 정직한 한계).

## Phase 4: 인계
4개 파일 완료 확인 → "issue-factcheck 로 판정 단계 진행 가능"을 보고하고 멈춘다. (수집 스킬은 판정하지 않는다.)

## 하드 규칙
- 출처 URL 없는 사실 기록 금지. 추정·일반론을 사실로 적지 않는다.
- 위험 결정(_workspace 삭제 등)은 멈추고 먼저 묻는다.
