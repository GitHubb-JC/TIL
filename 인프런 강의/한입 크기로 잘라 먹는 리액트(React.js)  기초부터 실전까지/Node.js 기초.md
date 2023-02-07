# Node.js 기초

# 1. Node.js란?

> 자바스크립트가 너무 좋다는 걸 점점 느끼다 보니 개발자들이 크롬의 V8엔진(자바스크립트 실행 엔진)을 따로 분리하여 브라우저가 아닌 곳에서도 사용할 수 있도록 만든 실행환경





---

# 2. Node.js & VsCode 설치하기

https://nodejs.org/en/ 노드js 다운로드 사이트

- LTS (Long Term Support) 장기 지원 버전		>> 우리는 이거 사용할 것
  - 이 버전은 개발자가 어느 정도 꾸준하고 안정적으로 작동하도록 관리할 버전
- Current 버전
  - 말 그대로 최신 기능들을 바로바로 업데이트 한 버전 조금 불안정 할 수 있음





---

# 3. Node.js Hello World & Common JS

```javascript
//계산 기능을 하는 calc.js 파일

const add = (a, b) => a + b;
const sub = (a, b) => a - b;

module.exports = {
    moduleName: "calc module",
    add: add,
    sub: sub,
};
```

```javascript
//calc를 가져올 index.js파일
const calc = require("./calc");

console.log(calc);
```

<img src="Node.js 기초.assets/image-20230207171818883.png" alt="image-20230207171818883" style="zoom:80%;" align='left' />

```javascript
//calc는 그대로 사용하고 index만 바꿔보자
const calc = require("./calc");

console.log(calc.add(1, 2));
console.log(calc.add(4, 5));
console.log(calc.sub(10, 2));
```

<img src="Node.js 기초.assets/image-20230207172217950.png" alt="image-20230207172217950" style="zoom:80%;" align='left' />





---

# 4. Node.js 패키지 생성 및 위부 패키지 사용하기

>- npm (Node Package Manager) Node.js의 패키지 관리 도구
>
>우리가 노드를 사용하면서 다른 사람들이 만든 모듈들을 내려받아 사용할 수 있게 해주거나 우리가 개발할 프로젝트 관리를 도와주는 도구

> - Package
>
> 누군가 따로 만들어둔 노드 모듈을 이야기 한다. (ex. 로그인 모듈(패키지), 전화인증 모듈(패키지), 메일발송 모듈(패키지))

https://www.npmjs.com/ 공개된 여러가지 모듈(패키지)를 찾을 수 있는 사이드

```javascript
const randomColor = require('randomcolor');
// npm i 를 이용해서 다운받은 모듈을 주소를 명확하게 명시하지 않아도 
// 알아서 node_modules 안에 있겠지 하고 진행해줘

let color1 = randomColor();
let color2 = randomColor();
let color3 = randomColor();

console.log(color1, color2, color3);
```

<img src="Node.js 기초.assets/image-20230207175320775.png" alt="image-20230207175320775" style="zoom:80%;" align='left' />

