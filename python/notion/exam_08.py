word = "HappyHacking"

count = 0

for char in word:
    if char in ['a', 'e', 'o', 'u', 'i']:
        count += 1

print(count)