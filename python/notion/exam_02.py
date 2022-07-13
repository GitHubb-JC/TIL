## input
a = 20
b = 30

def rectangle(a, b):
    area = a * b
    leng = 2 * (a + b)
    return(f'({area}, {leng})')

print(rectangle(a, b))
