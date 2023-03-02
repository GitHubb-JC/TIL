import sys
import numpy as np
sys.stdin = open('o_day_o_code.txt')

## 띄어쓰기로 구분되는 값 받기
n, m = map(int, input().split()) 
arr = []

for _ in range(m):
	# m번 loop을 돌면서 input을 arr에 append
	arr.append(list(map(int, input().split())))