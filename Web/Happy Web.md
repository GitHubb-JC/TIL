# Happy Web

## HTML

### 웹 사이트의 구성 요소

- HTML -- 구조
- CSS -- 표현
- Javascript -- 동작

### 웹 사이트와 브라우져

- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음 (파편화)
- 해결책으로 웹 표준이 등작

## HTML & CSS

### 웹 표준

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함 (크로스 브라우징)

### Can I use?

- 브라우저 별 호환성을 체크하는 사이트!

# 개발 환경 설정

## Text editor

### Visual Studio Code

- HTML/CSS 코드 작성을 위한 Visual Studio Code 추천 확장 프로그램
  - Open in browser
  - Auto Rename Tag
  - Auto Close Tag
  - Intellisense for CSS class names in HTML
  - HTML CSS Support

## Chrome

### 크롬 개발자 도구

- 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공
- 주요기능
  - Elements - DOM 탐색 및 CSS 확인 및 변경
    - Styles - 요소에 적용된 CSS 확인
    - Computed - 스타일이 계산된 최종 결과
    - Event Listeners - 해당 요소에 적용된 이벤트 (JS)
  - Sources, Network, Performance, Application, Security, Audits 등

# HTML 기초

## HTML 기초

### HTML( Hyper Text Markup Language )?

- Naver 사이트에 접속해서 개발자 도구를 활용해 CSS를 삭제 한다면?
  - HTML만 남은 웹 사이트를 확인할 수 있음

### Hyper Text란?

- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

### Markup Language

- 태그 등을 이요하여 문서나 데이터의 구조를 명시하는 언어
  - 대표적인 예 - HTML, Markdown

### 결국 HTML 이란?

- 웹 페이지를 작성(구조화)하기 위한 언어

# HTML 기본 구조

## HTML 기초

### HTML 기본 구조

- html : 문서의 최상위 (root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

### head 예시 (꺽쇠 속에 들어가)

- title : 브라우저 상단 타이틀
- meta : 문서 레벨 메타데이터 요소
- link : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- script : 스크립트 요소 (JavaScript 파일/코드)
- style : CSS 직접 작성