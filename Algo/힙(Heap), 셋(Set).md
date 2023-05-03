------

------

# 1. 힙(Heap)

## 1) 우선순위 큐(Priority Queue)

> 순서가 아닌 우선순위를 기준으로 가져올 요소를 결정(dequeue)하는 큐

![img](힙(Heap), 셋(Set).assets/img.png)

![img](힙(Heap), 셋(Set).assets/img-16821406186781.png)



## 2) 힙 (Heap)

> 최대값 또는 최소값을 빠르게 찾아내도록 만들어진 데이터구조 완전 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지한다. 힙 트리에서는 중복 값을 허용한다.

### (1) 힙은 언제 사용해야 할까?

1. 데이터가 지속적으로 정렬되야 하는 경우
2. 데이터의 삽입/삭제가 빈번할때









### (2) 파이썬의 heapq 모듈

> Minheap(최소힙)으로 구현되어 있음(가장 작은 값이 먼저 온다.) 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다. (배열, 연결리스트, 힙으로 구현 가능)

![img](힙(Heap), 셋(Set).assets/img-16821406186782.png)

![img](힙(Heap), 셋(Set).assets/img-16821406186783.png)







## 3) 힙 메서드

https://buyandpray.tistory.com/30

### (1) heapq.heapify()

주어진 list를 heap으로 만들 때 사용하는 메서드

시간복잡도 : O(N)

![img](힙(Heap), 셋(Set).assets/img-16821406186794.png)

### (2) heapq.heappush(heap, item)

heap에 값을 넣을때 사용하는 메서드이다. 변수가 들어갈 heap과 들어갈 변수 item을 전달한다.

시간복잡도 : O(logN)

![img](힙(Heap), 셋(Set).assets/img-16821406186795.png)

### (3) heapq.heappop(heap)

heap에서 root값을 빼내고자 할때 사용한다. heap에서 가장 작은 값을 리턴한다.

시간복잡도 : O(logN)

![img](힙(Heap), 셋(Set).assets/img-16821406186796.png)









## 4) 힙 활용

https://www.acmicpc.net/problem/11286

- 힙에 원소를 추가할 때 ( abs(n), n ) 의 형태로 넣어주게 되면 첫번째 원소를 기준으로 힙을 정렬한다. 