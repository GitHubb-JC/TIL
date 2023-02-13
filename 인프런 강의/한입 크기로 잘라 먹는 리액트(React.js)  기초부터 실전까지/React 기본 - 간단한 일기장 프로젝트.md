# React 기본 - 간단한 일기장 프로젝트

---

# 1. 프로젝트 소개

## 일기장 작성 사이트를 만든다





---

# 2. React에서 사용자 입력 처리하기

- userState를 이용하여 작성자 입력란을 만들어준다.
  - <img src="C:\Users\JC\AppData\Roaming\Typora\typora-user-images\image-20230210160344838.png" alt="image-20230210160344838" style="zoom:80%;" align='left' />



- onChange 함수로 매개변수 e 를 이용하여 값을 조작 할 수 있다.
  - 빈칸에 값을 입력하려 하면 콘솔창에 onChange 함수가 작동하는 걸 볼 수 있다.
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210162411655.png" alt="image-20230210162411655" style="zoom:80%;" align='left' />
  - 더 상세하게 확인하여 e.target.value 를 보면 
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210163002007.png" alt="image-20230210163002007" style="zoom:80%;" align='left' />
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210163143624.png" alt="image-20230210163143624" style="zoom:80%;" align='left' />

- 위의 과정들로는 수정 하는 거 까지는 못해 setAuthor 함수를 이용해 줘야함
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210163625498.png" alt="image-20230210163625498" style="zoom: 80%;" align='left'/>
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210163526251.png" alt="image-20230210163526251" style="zoom:80%;" align='left'/>



- 하지만 이렇게 바꾸는 거마다 함수를 만들기는 귀찮아
  - 하나로 묶어주자
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210165326686.png" alt="image-20230210165326686" style="zoom: 80%;" align='left'/>



- 그런데 여기서 setState 속 바뀌지 않는 값들이 많아지면 변수들이 너무 많아져
  - 스프레드 연산자를 이용해 바뀌지 않는 값들은 기본값으로 가져올 수 있어 순서는 중요해!! 수정하는 코드를 가장 마지막에!!
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210165653624.png" alt="image-20230210165653624" style="zoom:80%;" align='left'/>



- setState도 너무 반복이 심해져

  - handle을 이용하여 하나의 함수로 관리해줘
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210170656885.png" alt="image-20230210170656885" style="zoom:80%;" align='left' />

  - emotion 이라는 감정 점수도 하나 추가
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210172721787.png" alt="image-20230210172721787" style="zoom:80%;" align='left' />
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210172810481.png" alt="image-20230210172810481" style="zoom:80%;" align='left' />
  - 저장 버튼도 하나 추가
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210173239800.png" alt="image-20230210173239800" style="zoom:80%;" align='left' />
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210173318814.png" alt="image-20230210173318814" style="zoom:80%;" align='left' />





---

# 3. React에서 DOM 조작하기 - useRef

- 사이트의 운영자가 원하는 입력 값의 범위가 있을 것이다. 이러한 제한 요소들을 핸들러로 구현할 수 있다.
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210174839878.png" alt="image-20230210174839878" style="zoom: 80%;" align='left' />
  - <img src="React 기본 - 간단한 일기장 프로젝트.assets/image-20230210174922548.png" alt="image-20230210174922548" style="zoom:80%;" align='left'/>



- 하지만 이렇게 alert 창을 띄우는 건 이제 트랜드에서 좀 동떨어진 구현이다
- 따라서 우리는 focus를 이용할 것이다.