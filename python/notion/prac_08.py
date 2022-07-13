## input
from cmath import inf


numbers = [110, 20, 100, 50, -60, 50, 100] # 50
max_num = numbers[0]
sec_num = float(-inf)

for i in numbers:
    if(max_num < i):
        sec_num = max_num
        max_num = i
    elif(sec_num < i < max_num):
        sec_num = i
print('max', max_num)
print('second', sec_num)