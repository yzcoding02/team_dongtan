for i in range(10):
    print("난 숙제 중 입니다.")

i = 30
while i < 41:
    print(i)
    i += 1

# 2
sum = 1
for i in range(1, 20):
    if i % 5 == 0:
        sum += i
        print(i)

# 3
sum = 0
i = 1
while i <= 20:
    if i % 5 == 0:
        sum += i
    i += 1
print(sum)

# 4
num = 1
i = 10
while i <= 20:
    if i % 3 == 0:
        num *= i
    i += 1
print(num)

# 5
i = 100
while i <= 200:
    if i % 35 == 0:
        print(i)
    i += 1
