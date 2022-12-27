# 0부터 10까지 홀수
for i in range(10):
    if i % 2 == 1:
        print(i)

# 0부터 10까지 짝수
for i in range(11):
    if i % 2 == 0:
        print(i)

# 10부터 20까지 3의 배수를 더해
sum = 0
for i in range(10, 21):
    if i % 3 == 0:
        sum += i
print(sum)
# 1부터 100까지 짝수의 수를 더한 값과 홀수를 더한 값을 빼라
sum = 0
suii = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
    elif i % 2 == 1:
        suii += i

print(sum - suii)
# 50부터 80까지 3과 4의 공배수
for i in range(50, 81):
    if i % 3 == 0:
        if i % 4 == 0:
            print(i)
# 1부터 20까지 5의배수를 곱한 값을 구해
sum = 1
for i in range(1, 21):
    if i % 5 == 0:
        sum *= i
print(sum)
