---

# SQL

## - SQL(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수목적 프로그래밍 언어
- 데이터베이스 스키마 생성및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

![img](https://blog.kakaocdn.net/dn/K1CCw/btr6DKqV7Xx/RPj4espqKMY90t5WWjT42k/img.png)



## - SQL Keywords - Data Manipulation Languege

- INSERT : 새로운 데이터 삽입(추가)
- SELECT : 저장되어 있는 데이터 조회
- UPDATE : 저장되어 있는 데이터 갱신
- DELETE : 저장되어 있는 데이터 삭제







------

# Table 생성, 삭제

## - DB 생성하기

![img](https://blog.kakaocdn.net/dn/CTnYl/btr6GrqZ6U3/KtKbT5fv3bFspSTIjOCK0k/img.png)



## - CSV 파일을 table로 만들기

![img](https://blog.kakaocdn.net/dn/4V5PV/btr6NZf5Vb0/Y5gcGI9DXokfvKn4PCcwM0/img.png)



## - SELECT 확인하기

![img](https://blog.kakaocdn.net/dn/dicLEq/btr6Fg4itBr/JkqgqMg6eAGMPHFlsKWAYK/img.png)



## - 터미널 view 변경하기

![img](https://blog.kakaocdn.net/dn/bgbo8v/btr6GrdtoFh/nka4XrAtXbXG1HPwyLsRt0/img.png)



## - 테이블 생성 및 삭제 statement

#### - CREATE TABLE

- DB에서 테이블 생성

![img](https://blog.kakaocdn.net/dn/bRHZiS/btr6N1SugVy/5SDMM48kuM4T4zpgVYcF80/img.png)

- 테이블 생성 및 확인하기

![img](https://blog.kakaocdn.net/dn/csRFCa/btr6K3wBB4a/4qAGlKAQ0dCz6XXMvubE6k/img.png)

- 테이블의 schema 조회

![img](https://blog.kakaocdn.net/dn/bkNWCk/btr6OYA8oOs/mF6JYbZh5KHy81jddek421/img.png)



#### - DROP TABLE

- DB에서 테이블 제거

![img](https://blog.kakaocdn.net/dn/0hr44/btr6DYJQ8dE/D0pQZ3ml8r00A7I9dlmUR0/img.png)

![img](https://blog.kakaocdn.net/dn/r2mKo/btr6N2xi8ES/203Nh5mIeeAFLBsKMo0z80/img.png)



#### - 필드 제약 조건

- NOT NULL : null 값 입력 금지
- UNIQUE : 중복 값 입력 금지 (null 값은 중복 입력 가능)
- PRIMARY KEY : 테이블에서 반드시 하나는 PK 값이어야 한다. (not null 이면서 unique 해야 한다.)
- FOREIGN KEY : 외래키로 다른 테이블에서 온 key값이다.
- CHECK : 조건에 해당하는 값만 입력을 허용한다.
- DEFAULT : 비어있거나 할 경우 기본으로 설정될 값이다.