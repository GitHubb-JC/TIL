##input
word = 'apple'

## 슬라이싱으로 편하게
rev = ''

rev = word[::-1]
print(rev)

##for문으로
count = 0
rev = ''

## 이거 len() 으로 바꿔주자
for n in word:
    count += 1
for n in range(count):
    n += 1
    rev += word[-(n)]
print(rev)

## 3. index
word = 'apple'

for i in range(len(word)):
    ## end : print  출력후 뒤에 붙일 값 기본이 \n 이라서 개행
    print()