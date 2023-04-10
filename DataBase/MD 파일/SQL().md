# 기본 함수와 연산 

## - 문자열 함수

- SUBSTR(문자열, start, length) : 문자열 자르기
  - 시작 인덱스 1, 마지막 인덱스 -1
- TRIM(문자열), LTRIM(문자열),RTRIM(문자열) : 문자열 공백 제거
- LENGTH(문자열) : 문자열 길이
- REPLACE(문자열, 패턴, 변경값) : 패턴에 일치하는 부분을 변경
- UPPER(문자열), LOWER(문자열) : 대소문자 변경
- || : 문자열 합치기(concatenation)



## - 숫자 함수

- ABS(숫자) : 절댓값
- SIGN(숫자) : 부호 (양수 -> 1, 음수 -> -1, 0 -> 0)
- MOD(숫자1, 숫자2) : 숫자1을 숫자2로 나눈 나머지
- CEIL(숫자), FLOOR(숫자), ROUND(숫자, 자리) : 올림, 내림, 반올림
- POWER(숫자1, 숫자2) : 숫자1의 숫자2 제곱
- SQRT(숫자) : 제곱근



## - 산술 연산자

- +, -, *, / 와 같은 산술 연산자와 우선 순위를 지정하는 () 기호를 연산에 활용할 수 있음

![img](https://blog.kakaocdn.net/dn/cIZVyj/btr7gj01NG7/hpjWX5iFmgA1rscn6bkNwK/img.png)







------

# GROUP BY

## - ALIAS

- 칼럼명이나 테이블명이 너무 길거나 다른 명칭으로 출력하고 싶을 때는 ALIAS를 활용
- AS를 생략하여 공백으로 표현할 수 있음
- 별칭에 공백, 특수문자 등이 있는 경우 따옴표로 묶어서 표기

![img](SQL().assets/img.png)



## - GROUP BY

### - GROUP

- SELECT 문의 optional 절
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만든다
- **문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 한다**
- 집계함수와 함께 활용해야 의미가 있다.
- **지정된 갈럼의 값이 같은 행들로 묶인다.**
- **그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐**

![img](SQL().assets/img-16811038629821.png)

![img](SQL().assets/img-16811038629832.png)

- GROUP BY 절에 명시하지 않은 컬럼은 별도로 지정할 수 없음
  - 그룹마다 하나의 행을 출력하게 되므로 집계 함수 등을 활용해야 한다.
-  GROUP BY 의 결과는 정렬되지 않음
  - 기존의 순서와 바뀌는 모습도 있다.
  - 원칙적으로 관계형 데이터베이스에서는 ORDER BY 를 통해 정렬한다.



### - HAVING

- 집계함수는 WHERE 절의 조건식에서는 사용할 수 없음(실행 순서 때문에)
  -  WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서 있기 때문
- 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING을 활용

![img](SQL().assets/img-16811038629833.png)



### - SELECT문장 실행 순서

![img](SQL().assets/img-16811038629834.png)

- FROM : 테이블에서
- WHERE : 조건에 맞춰 뽑아
- GROUP BY : 그룹화 하고
- HAVING : 그 그룹에서 조건이 맞는 것들을
- SELECT : 조회한 뒤
- ORDER BY : 정렬해서 
- LIMIT / OFFSET : 특정 범위의 값들을 가져와







------

# Alter Table

## - Alter Table

![img](SQL().assets/img-16811038629845.png)