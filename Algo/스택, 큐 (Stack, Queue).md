------

# 1. 스택 (Stack)

> Stack 쌓는다. 마치 접시를 쌓고 빼듯이 데이터를 한쪽에서만 넣고 빼는 자료구조, 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 LIFO(Last in First out, 후입선출) 방식이다.

![img](https://blog.kakaocdn.net/dn/b8jOd3/btsa8AYFZIi/tTpR9xGKuYMvNf4HEwBAM0/img.png)

파이썬은 리스트를 이용하여 스택을 편하게 구현할 수 있다.

![img](https://blog.kakaocdn.net/dn/bKletf/btsbmQysc8t/7hoOKIc8vnEX6vbay4TQ90/img.png)



## 1) 스택의 사용 예

- 되돌리기, 되돌아가기 등등

![img](https://blog.kakaocdn.net/dn/zPwo1/btsbmPTQORT/eVnqB19dXXn8iU33RyiaG1/img.png)

뒤로가기 버튼을 누르면

▼

![img](https://blog.kakaocdn.net/dn/du2zB7/btsa9HXzGKk/ki1gY3977wM6xgr8pzjvkk/img.png)











------

# 2. 큐(Queue)

> 한쪽 끝에서 데이터를 넣고, 다른 한쪽에서 데이터를 빼는 자료구조 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First in First out, 선입선출) 방식

![img](스택, 큐 (Stack, Queue).assets/img.png)

- 큐도 파이썬의 리스트로 간편하게 사용할 수 있다.



![img](스택, 큐 (Stack, Queue).assets/img-16818892376531.png)

- 리스트를 이용한 큐 자료구조는 데이터를 뺄때 큐 안에 많은 데이터가 있으면 인덱스가 하나씩 줄어들면서 효율이 떨어지는 단점이 있다.



## 1) 덱 (Deque, Double-Ended Queue) 자료구조

> 양 방향으로 삽입과 삭제가 자유로운 큐

![img](스택, 큐 (Stack, Queue).assets/img-16818892376532.png)

- 양 방향으로 삽입삭제가 가능하여 큐보다 빠르게 연산이 가능하다.