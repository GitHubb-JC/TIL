t = int(input())

#t = 5
n_list = []
for i in range(t):
    n = int(input())
    if n == 0:
        del n_list[-1]
        #print(n_list)
    else:
        n_list.append(n)
        #print(n_list)
n_sum = sum(n_list)
print(n_sum)