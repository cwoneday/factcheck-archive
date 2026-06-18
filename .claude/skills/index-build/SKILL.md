---
name: index-build
description: "전 이슈를 훑어 검색 매니페스트(index.json + index-data.js)를 재생성하고 무결성을 점검한다. '인덱스 갱신', '검색 다시 빌드', 새 이슈 발행 직후, 이슈 추가/수정 후 이 스킬을 사용."
---

# index-build — 검색 인덱스 갱신

플랫폼 레이어(fable엔 없던 부분). 이슈를 추가·수정한 뒤 검색 인덱스를 맞춘다.

## 절차
1. (페이지가 안 만들어진 이슈가 있으면) `python tools/build_issue.py --all`.
2. `python tools/build_index.py` 실행 → `index.json` + `index-data.js` 재생성.
3. 빌더의 자체 점검 통과 확인:
   - 매니페스트 이슈 수 == `issues/` 디렉토리 수
   - 모든 `url`이 실재 파일을 가리킴 (깨진 링크 0)
   - 빈 verdict 0
4. 실패 메시지가 있으면 그 원인(미렌더 페이지·스키마 누락)을 해결하고 재실행.

## 검증 (작동 확인)
- `index.json` 원소 수가 의도한 이슈 수와 일치.
- 허브를 열어 새 이슈 카드가 검색·정렬에 노출되는지 확인.

## 하드 규칙
- `index.json`·`issue.json` 수기 편집 금지(항상 빌더로 생성).
- 이슈 데이터 삭제는 위험 결정 → 멈추고 먼저 묻는다.
