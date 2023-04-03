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