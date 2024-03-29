# 힙 (Heap), 셋 (Set)

## 1. 힙 (Heap)

- 순서가 아닌 다른 기준으로는??
- 우선순위 큐 (Priority Queue)
  - 우선순위 (중요도, 크기 등 순서 이외의 기준)
    1. 가중치가 있는 데이터
    2. 작업 스케줄링
    3. 네트워크
  - dequeue 맨 앞의 데이터를 가져오는 행위
  - enqueue 맨 뒤의 데이터를 삽입하는 행위
  - 구현하는 방법
    1. 배열 (Array)
    2. 연결 리스트 (Linked List)
    3. 힙 (Heap)
  - 우 큐 구현 별 시간 복잡도
- 힙의 특징
  - 최대값 또는 최소값을 빠르게 찾아내도록 ★
  - 완전 이진 트리의 형태 느슨한 정렬 상태를 유지 ★
    - 가장 작은 요소가 항상 루트인 heap[0] 이다.
  - 중복 값 허용
  - 언제 사용해야 할까?!
    1. 테이터가 지속적으로 정렬되어야 하는 경우
    2. 데이터의 삽입, 삭제가 빈번할 때

- 파이썬의 heapq 모듈
  - Minheap (최소 힙) 으로 구현되어 있음 (가장 작은 값이 먼저 옴)
  - CRUD 연산의 속도가 리스트보다 빠르다.
- 힙과 리스트 비교
- 큐와 힙의 사용법 비교



## 셋 (Set)

- '집합' 을 나타내는 구조
- 셋의 연산
- 언제 사용해야 할까?
  1. 데이터의 중복이 없어야 할때 (고유값들로 이루어진)
  2. 정수가 아닌 데이터의 삽입, 삭제 , 탐색이 빈번히 필요할때 
- 셋 연산의 시간 복잡도/*