# 1 나는 숙제 중입니다 10번 출력
for i in range(10):
    print("나는 숙제 중입니다")

i = 30
while i < 41:
    print(i)
    i += 1

# 2 30~40까지 순서대로 출력
for i in range(30, 41):
    print(i)

i = 1
sum = 1
while i < 20:
    i += 1
    if i % 5 == 0:
        sum = +i
    print(sum)

# 3 1~20 사이 5의 배수들의 합계
sum = 0
for i in range(1, 21):
    if i % 5 == 0:
        sum += i
print(sum)

sum = 0
while i < 21:
    i += 1
    if i % 5 == 0:
        sum = +i
    print(sum)

# 4 10~20 사이 3의 배수들의 곱
sum = 1
for i in range(10, 21):
    if i % 3 == 0:
        sum *= i
print(sum)

sum = 0
while i < 21:
    i += 1
    if i % 3 == 0:
        sum = +i
    print(sum)


# 5 100~200 사이 5와 7의 공배수 모두 출력
for i in range(100, 201):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

while i < 201:
    i += 100
    if i % 5 == 0:
        if i % 7 == 0:
            print(sum)
