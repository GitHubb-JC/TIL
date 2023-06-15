# 01.04

# 중앙처리장치(CPU) 개념정리

## 개념
Central Processing Unit (CPU)

- 컴퓨터의 4대 주요 기능인 기억, 해석, 연산, 제어를 관장하는 장치(칩)
- 중앙처리장치는 외부에서 정보를 입출력 받고(제어), 기억하고(기억), 프로그램의 명령어를 해석(해석)하고, 연산(연산)하는 역할을 한다.



## 구조

<img src="C:\Users\JC\AppData\Roaming\Typora\typora-user-images\image-20230104104829425.png" alt="image-20230104104829425" style="zoom:50%;" align="left" />

- 프로세서 유닛
  - 산술 논리 장치 (Arithmetic Logic Unit, ALU)
    - 비교, 판단, 연산을 담당
  - 제어 장치 (Control Unit, CU)
    - 명령어의 해석과 올바른 실행을 위해 내부를 제어

- 메모리 유닛
  - 읽기 전용 기억 장치(Read-Only Memory, ROM)
  - 임의 기억 장치(Random-Access Memory, RAM)
  - 캐시 메모리(Cache Memory)



## 성능

CPU의 성능은 크게 클럭(Clock)과 클럭당 명령어 처리 횟수(IPC) 그리고 코어(Core)의 수에 의해 정해진다.

- 클럭(Clock)
  - 중앙처리장치 내부에서 일정한 주파수를 가지는 신호로 이 신호에 동기화되어 중앙처리장치의 모든 명령어가 동작한다. 예를 들어 3.0GHz 라면 초당 30억번의 연산이 가능하다는 뜻이다.
- 클럭당 명령어 처리 횟수(Instructions Per Cycle, IPC)
  - 한번의 클럭 사이클 당 명령어 처리 횟수를 이야기 하는 지표, 같은 클럭을 가지고 있더라도 IPC가 높으면 더 좋은 성능을 보여준다.
  - 하지만 제조사에서 명확하게 제공하는 지표가 아니라 벤치마크를 돌려보던가 여러 프로그램들을 돌려보면서 실 사용수치를 바탕으로 추척할 뿐이다.
- 코어(Core)
  - 중앙 처리 장치의 역할을 하는 블록
  - 중앙 처리 장치를 병렬적으로 연결한다고 볼 수 있다.
  - 프로그램에서 멀티코어를 활용할 수 있도록 코딩해줘야 한다.



## 제조사

- 인텔
  - i 시리즈
- AMD
  - 라이젠 시리즈





## 참고

- https://namu.wiki/w/CPU
- https://ko.wikipedia.org/wiki/%EC%A4%91%EC%95%99_%EC%B2%98%EB%A6%AC_%EC%9E%A5%EC%B9%98#%EC%84%A4%EA%B3%84%EC%99%80_%EA%B5%AC%ED%98%84
- https://babytiger.netlify.app/posts/cpu/












# 도메인 개념정리

## 도메인 관리 체계

ICANN - 레지스트리 - 레지스트라 - 레지스트란트 의 구조를 가진다.

- (국제)인터넷 주소 관리 기구 (Internet Corporation for Assigned Names and Nunbers, ICANN)
  - 



## 개념

Domain : 영도, 분야, 영역, 범위 등을 뜻하는 단어, 인터넷 주소, 전문 분야를 이야기 할때 '해당 도메인(분야)에 대한 ~~' 등으로도 사용된다.



 

