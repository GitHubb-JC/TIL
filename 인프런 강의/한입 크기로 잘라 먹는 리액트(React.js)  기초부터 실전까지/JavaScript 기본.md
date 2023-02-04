# JavaScript 기본

---

# 1. Hello World

## 자바스크립트는 무엇일까?

- 스택오버플로우에서 가장 인기있는 언어 1위



## 자바스크립트의 역할

### HTML

- 요소들의 배치와 내용을 기술하는 언어
- 색이나 크기 등의 디자인 수행 없음



### CSS

- 색, 크기, 애니메이션 등을 정의하는 스타일링을 위한 언어



### Javascript

- 웹사이트에 활력을 부여하는 언어



## 자바스크립트가 실행되는 곳

- 웹 브라우저들 
  - ex) 크롬의 V8 엔진





---

# 2. 변수와 상수

변수는 

- let 으로 만들어 
  - 변수명에 기호는 사용할 수 없어 (예외 _ , $ ) 
  - 숫자로 시작할 수는 없어
  - 예약어는 사용할 수 없어 (if, for 등등)

- var 로는 만들지 말자
  - let과 전혀 다른게 없는거 같지만
  - 같은 변수명으로 선언을 두번 할 수 있어져... (꼬일 확률 높아!!)

상수는 

- const 로 선언 가능해
  - read-only 로 만들어져 한번 선언하면 바꿀 수 없어
  - 선언하면서 값을 줘야해





---

# 3. 자료형과 형 변환

<img src="JavaScript 기본.assets/image-20230203092957509.png" alt="image-20230203092957509" style="zoom:80%;" align='left' />

- Primitive Type (원시 타입)

  - 한번에 하나의 값만 가질 수 있음
  - 하나의 고정된 저장 공간 이용

  - Number
    - 정수, 실수, Infinity, NaN 등등 구별하지 않고 사용
    - 기본적으로 사칙연산 제공
  - String
    - ' ', 혹은 " " 로 선언가능해
    - `(backtick)    ``  으로 감싸서 선언 가능해 
      - ` 으로 감싸면 ${ } 를 이용해서 변수를 사용 가능해 (탬플릿 리터럴)
    - '2' 이런식으로 숫자만 문자열로 선언하면 곱셈과 나눗셈은 자동으로 숫자로 변환해서 수행
    - 덧셈을 하려면 parseInt(String) 으로 의도적으로 명시적 형변환을 해야해
  - Boolean
    - True, False 선언
  - Null
    - 선언하고 따로 넣어줘야해
  - Undefined
    - 선언만 하면 undefined 으로 나와

- Non-Primitive Type (비 원시 타입)

  - 한번에 여러 개의 값을 가질 수 있음
  - 여러 개의 고정되지 않은 동적 공간 사용





---

# 4. 연산자

- 대입 연산자

  - ```javascript
    let a = 1;
    ```

- 산술 연산자

  - ```javascript
    a + b;
    a - b;
    a * b;
    a / b;
    a % b;
    ```

- 연결 연산자

  - ```javascript
    let a = "2";
    let b = 4;
    a + b;
    
    >> 결과는 24
    
    (둘중에 하나만 문자열이면 나머지 하나를 자동 형변환 하여 연산 수행)
    ```

- 복합 연산자

  - 산술 연산자와 대입 연산자를 함께 사용

  - ```javascript
    let a = 5;
    
    a = a + 10;
    a += 10;
    
    >> 결과는 둘다 15
    ```

- 증감 연산자

  - 숫자형에만 사용 가능

  - ```javascript
    let a = 10;
    
    a++;
    
    >> a는 11
    ```

  - 위치에 따라 작용하는 'line'이 달라져

  - ```javascript
    let a = 10;
    
    // 후위 연산
    a++; // 이 줄에서 a는 아직 10이야
    a;   // 이 줄에서 a는 11이야
    
    // 전위 연산
    ++a; // 이 줄에서 a는 바로 12가 되었어
    ```

- 논리 연산자

  - ! (Not)
    - !true  >> false
  - 피연산자 && 피연산자 (and 연산)
    - 피연산자가 둘다 true 여야 결과가 true
  - 피연산자 || 피연산자 (or 연산)
    - 피연산자가 둘중 하나만 true 여도 결과가 true

- 비교 연산자

  - ```javascript
    let compareA = 1 == "1";
    >> true
    // 그냥 값만 비교하는거라 자료형은 고려하지 않아
    
    let compareA = 1 === "1";
    >> false
    // 자료형까지 고려해서 비교해
    // 자료형가지 고려하는거로 주로 사용하자!
    ```

  - ```javascript
    let compareA = 1 != "1"; // 둘이 같지 않지??
    >> false 				 // 아니야! 둘이 같아!!
    // 그냥 값만 비교하는거라 자료형은 고려하지 않아
    
    let compareA = 1 !== "1"; // 둘이 같지 않지??
    >> true					  // 맞아 같이 않아!!
    // 자료형까지 고려해서 비교해
    // 자료형가지 고려하는거로 주로 사용하자!
    ```

  - ```javascript
    let compareA = 1 < 2;
    >> true
    // 대소비교! 1이 2보다 작냐?!
    
    let compareA = 1 <= 2;
    >> false
    // 대소비교! 1이 2보다 작거나 같냐?!
    ```

- 변수의 자료형 찾는 연산자

  - ```javascript
    compare = 1;
    typeof compare;
    
    >> number
    ```

- null 병합 연산자

  - ```javascript
    let a;		 // 선언만 했으니 현재 undefine
    a = a ?? 10; // ?? 는 양쪽 피 연산자중 null 혹은 undefine 이 아닌 연산자를 선택
    // a 값은 10이다.
    
    >> a = 10
    ```





---

# 5. 조건문

- if 문
  - ```javascript
    let a = 3;
    
    if (a > 5){
        console.log("5 초과입니다.")
    } else if(a = 5) { 
        // else if 는 여러번 쓸 수 있어
        console.log("5 입니다.")
    } else {
        // 위의 모든 조건을 만족하지 못하면 여기를 실행
        console.log("5 미만입니다.")
    }
    ```

- switch 문

  - ```javascript
    let country = "ko";
    
    switch(country){	// country 와 밑의 
        case "ko":		// case 와 비교 일치하면 아래를 전부 실행
            console.log("한국");
            break:		// break 가 없다면 쭉 실행해!
        case "cn":
            console.log("중국");
            break:
        case "jp":
            console.log("일본");
            break:
        case "uk":
            console.log("영국");
            break:   
        default:		// 모든 case 와 일치하지 않으면 default를 실행
            console.log("미 분류");
            break:        
    }
    ```





---

# 6. 함수

- 그냥 짜보자

  - ```javascript
    // 직사각형의 면적을 구해보자
    let width1 = 10;
    
    let height1 = 20;
    
    let area1 = width1 * height1;
    console.log(area1);
    >> area1 = 200
    
    let width2 = 30;
    
    let height2 = 15;
    
    let area2 = width2 * height2;
    console.log(area2);
    >> area2 = 450
    
    // 여러 면적을 구한다면 너무 귀찮다
    ```

  

- 함수로 만들어보자

  - ```javascript
    function getArea(){ // 여기서 바로 실행 되는건 아니야
        let width = 10;
        let height = 20;
        
        let area = width * height;
        console.log(area);
    }
    
    getArea();	// 여기서 실행!
    console.log("함수 실행 완료");
    
    >> 200
    >> 함수 실행 완료
    ```

  

- 매개 변수를 활용해 보자

  - ```javascript
    function getArea(width, height){ // ( )안에 들어가는게 매개 변수라 한다
        let area = width * height;
        console.log(area);
    }
    
    getArea(100, 200);	
    // 여기서 매개 변수를 넣어주면 
    // width = 100, height = 200으로 받아서 함수 실행
    
    >> 20000



- return 값을 줘보자

  - ```javascript
    function getArea(width, height){
        let area = width * height;
        return area; // 함수가 실행되면 return 값을 반환한다.
    }
    
    let area1 = getArea(100, 200);	
    // return 값이 area1 에 들어간다.
    
    console.log("area1 : ", area1);
    
    >> area1 : 20000
    ```



- 함수 내부의 변수는 밖에서 접근 할 수 없다.

  - ```javascript
    function getArea(width, height){
        let area = width * height;	// 함수 내에서만 이용하는 '지역변수' 라고 한다.
        return area;
    }
    
    let area1 = getArea(100, 200);	
    
    console.log(area);
    
    >> area is not defined
    ```



- 함수 외부에서 선언한 변수는 내부에서 접근이 가능

  - ```javascript
    let a = 1;
    
    function getArea(width, height){
        let area = width * height;
        console.log(a);
        return area;
    }
    
    let area1 = getArea(100, 200);	// 여기서 함수가 실행 되며 console이 찍힘
    
    >> 1
    ```

  - 

