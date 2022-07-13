##input
word = 'apple'

## 슬라이싱으로 편하게
rev = ''

rev = word[::-1]
print(rev)

##for문으로
count = 0
rev = ''

for n in word:
    count += 1
for n in range(count):
    n += 1
    rev += word[-(n)]
print(rev)