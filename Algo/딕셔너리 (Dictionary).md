------

# 1. 해시 테이블

- 파이썬에는 딕셔너리가 내장되어 있다.

![img](https://blog.kakaocdn.net/dn/CHqXJ/btsaShD2eMp/9WNkFDotUBkEdgq8rqsK3k/img.png)



- 리스트를 이용해서도 key value를 저장할 수는 있다.

![img](https://blog.kakaocdn.net/dn/BiOJQ/btsaTYD3PFB/sbOe6vdJkWZJxLk8gKSMfK/img.png)



- 딕셔너리는 해시 테이블(hash table)을 이용하여 key : value를 저장한다.

![img](https://blog.kakaocdn.net/dn/oalAe/btsaR1By4w2/st0QE8xLHpwx2vuwRfXh4k/img.png)



- 해시 함수 : 임의의 길이를 가지는 데이터를 고정 길이의 데이터로 맵핑하는 함수
- 해시 : 해시 함수를 통해 얻어진 값
- 파이썬의 딕셔너리는 해시 함수와 해시 테이블을 이용하여 연산 속도가 리스트보다 빠르다.

![img](https://blog.kakaocdn.net/dn/bqBv7V/btsaXmqSHpW/aZlN0nwYk68oQAWQBHrcR0/img.png)







------

# 2. 딕셔너리 기본 문법

- 딕셔너리 선언

![img](https://blog.kakaocdn.net/dn/bmtULZ/btsbma4Uk1O/ofvXyPAgP7HFv642FdY44k/img.png)

- 딕셔너리 삽입/수정

![img](https://blog.kakaocdn.net/dn/Cvgwn/btsbglfuGE3/bNSy5pPTlqiUojLq8Imp7K/img.png)

- 딕셔너리 삭제

![img](https://blog.kakaocdn.net/dn/zTlA8/btsbglGwc3P/0lwEUrxKJKMTRmqUudNotK/img.png)

![img](https://blog.kakaocdn.net/dn/BMxnq/btsa9K0XyOS/vDVoiUKArNxp7koXNPJGU1/img.png)

- 딕셔너리 조회

![img](https://blog.kakaocdn.net/dn/bdKq1C/btsbkFLujRX/jZJTrtzW1ZGlvVJcmlCbNK/img.png)

![img](https://blog.kakaocdn.net/dn/Ikzq5/btsbk27vAqD/baIsuEJFtgr7UMtlcbTJCK/img.png)

- 딕셔너리 문법 정리

![img](https://blog.kakaocdn.net/dn/BeZb9/btsbme0EmjA/2M4tt9aZJlinK3UPxadBU0/img.png)







------

# 3. 딕셔너리 메서드

## 1) .keys()

- 딕셔너리의 key목록이 담긴 dict_keys 객체 반환

![img](https://blog.kakaocdn.net/dn/uOW1M/btsbgls23a5/arSDVhXaVqkJnlFySlopEk/img.png)



## 2) .values()

- 딕셔너리의 value 목록이 담긴 dict_values 객체 반환

![img](https://blog.kakaocdn.net/dn/HPRXc/btsbmQkSwVD/e5TPUbkABnkwkyKCxmYg1k/img.png)



## 3) .items()

- 딕셔너리의 (key, value) 쌍 목록이 담긴 dict_items 객체 반환

![img](https://blog.kakaocdn.net/dn/uSw3M/btsblqm1Rsp/E1KPOM6SoexYJQuqh4pc51/img.png)







---

