# coding_test
알고리즘 공부 및 코딩테스트 대비를 위하여 정리하는 저장소.


Python 사용. 자동 완성 기능 없이 진행.

코드 검색은 교재 및 공식 사이트에서만


## Commit message
[Prefix][유형] 설명/문제 이름

### Commit message Prefix
풀었으면 Solve

틀린 걸 고쳤으면 Fix


[Solve]: 새로운 문제를 풀어서 코드를 추가함.

[Fix]: 오류 수정/오답 수정 -> 이후 복습할 거리들

[Docs]: 설명용 문서 변경

[Chore]: 잡일/구조 변경


## 복습 방법
1. 유형별 복습: 유형 이름 검색
2. 막혔던 문제 복습: Fix 검색

git log --oneline _깃로그 출력_

git log --oneline --grep=Graph _그래프 유형 깃로그만 출력_

git log --oneline --grep=Fix _막혔던 문제 로그 출력_