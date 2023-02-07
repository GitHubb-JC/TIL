const randomColor = require('randomcolor');
// npm i 를 이용해서 다운받은 모듈을 주소를 명확하게 명시하지 않아도 
// 알아서 node_modules 안에 있겠지 하고 진행해줘

let color1 = randomColor();
let color2 = randomColor();
let color3 = randomColor();

console.log(color1, color2, color3);