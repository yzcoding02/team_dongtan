# 1 (1~10 까지 프린트 하기)
for i in range(10):
    print(i + 1)

# 2 (1~10 까지의 수 중에서 짝수, 홀수 구하기)
for i in range(1, 11):
    if i % 2 == 1:
        print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 3 (10~20 의 수 중에서 3의 배수인 수들의 덧셈)
sum = 0
for i in range(10, 21):
    if i % 3 == 0:
        sum += i
print(sum)

# 4 (1~100 까지의 수 중 홀수와 짝수의 덧셈)
sum1 = 0
sum2 = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum1 += i
    elif i % 2 == 1:
        sum2 += i
print(sum1 - sum2)

# 5 (50~81 까지의 수 중 3 과 4의 공배수)
for i in range(50, 81):
    if i % 3 == 0:
        if i % 4 == 0:
            print(i)

# 6 (1~20 까지의 수 중 5의 배수들의 곱)
sum = 1
for i in range(1, 21):
    if i % 5 == 0:
        sum *= i
print(sum)
