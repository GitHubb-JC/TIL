참고 : https://mangkyu.tistory.com/98

------

# 1. HTTP란?

## HTTP(Hyper Text Transfer Protocol)란?

http란 서버/클라이언트 모델을 따라 데이터를 주고 받기 위한 프로토콜이다.

즉, http는 인터넷에서 하이퍼텍스트를 교환하기 위한 통신 규약으로, 80번 포트를 사용하고 있다. 따라서 http 서버가 80번 포트에서 요청을 기다리고 있으며, 클라이언트는 80번 포트로 요청을 보내게 된다.

## HTTP의 구조

http는 애플리케이션 레벨의 프로토콜로 TCP/IP 위에서 작동한다. http는 상태를 가지고 있지 않는 Stateless 프로토콜이며 Method, Path, Version, Headers, Body 등으로 구성된다.

![img](https://blog.kakaocdn.net/dn/bSS06I/btsg3W2rnWe/E5Aa6qL5TdWJCNeFZnhgsk/img.png)

하지만 http는 암호화가 되지 않은 평문 데이터를 전송하는 프로토콜이였기 때문에, http로 비밀번호나 주민등록번호 등을 주고 받으면 제 3자가 정보를 조회할 수 있었다. 이러한 허점을 해결하기 위해 https가 등장하게 되었다.





------



# 2. HTTPS란?

## HTTPS(Hyper Text Transfer Protocol Secure)란?

HyperText Transfer Protocol over Secure Socket Layer, HTTP over TLS, HTTP over SSL, HTTP Secure 등으로 불리는 https는 http에 데이터 암호화가 추가된 프로토콜이다. https는 http와 다르게 443번 포트를 사용하고, 네트워크 상에서 중간에 제3자가 정보를 볼 수 없도록 암호화를 지원하고 있다.

## 대칭키 암호화와 비대칭키 암호화

https는 대칭키 암호화 방식과 비대칭키 암호화 방식을 모두 사용하고 있다. 각각의 암호화 방식은 다음과 같다.

- 대칭키 암호화
  - 클라이언트와 서버가 동일한 키를 사용해 암호화/복호화를 진행함
  - 키가 노출되면 매우 위험하지만 연산 속도가 빠름
- 비대칭키 암호화
  - 1개의 쌍으로 구성된 공개키와 개인키를 암호화/복호화 하는데 사용함
  - 키가 노출되어도 비교적 안전하지만 연산 속도가 느림

대칭키는 비교적 쉬운 개념이므로, 비대칭키 암호화에 대해 살펴보도록 하자.

비대칭키 암호화는 공개키 / 개인키 암호화 방식을 이용하여 데이터를 암호화하고 있다. 공개키와 개인키는 서로를 위한 1쌍의 키이다.

- 공개키 : 모두에게 공개가능한 키
- 개인키 : 나만 가지고 알고 있어야 하는 키

암호화를 공개키로 하느냐 개인키로 하느냐에 따라 얻는 효과가 다른데, 공개키와 개인키로 암호화하면 각각 다음과 같은 효과를 얻을 수 있다.

- 공개키 함호화 : 공개키로 암호화를 하면 개인키로만 복호화 할 수 있다.
  - 개인키는 나만 가지고 있으므로, 나만 볼 수 있다.
- 개인키 암호화 : 개인키로 암호화하면 공개키로만 복호화 할 수 있다.
  - 공개키는 모두에게 공개되어 있으므로, 내가 인증한 정보임을 알려 신뢰성을 보장 할 수 있다.

![img](https://blog.kakaocdn.net/dn/bn6TN3/btsg9uqkbs9/WdKeJcViEPX6X5RbQ6FlKk/img.png)


