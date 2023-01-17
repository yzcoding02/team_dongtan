# 1-11 홀수출력
for i in range(1,11):
    if i%2==1:
        print(i)
#1-11 짝수출력
for i in range(1,11):
    if i%2==0:
        print(i)
#20-40 3의배수합
for i in range(20,41):
    if i%3==0:
        print(i)
#10부터 20까지의 수중 3배수 
for i in range(10,21):
    if i%3==0:
        sum+=i
print(sum)
#1부터 100까지의 수중 짝수와 홀수의 차
su=0
sum=0
for i in range(1,101):
    if (i%2==0):
        sum+=i
    elif (i%2==1):
        su+=i
print(sum-su)
#50부터 80 중 3,4 의 공배수
for i in range(50,81):
    if (i%3==0):
        if (i%4==0):
            print(i)
#1부터 20중 5배수 들 곱
sum=1
for i in range(1,21):
    if (i%5==0):
        sum*=i
print(sum)