# 1에서 20중 3의 배수를
# 리스트로 담아서 내림차순으로 출력
민기 = []
for i in range(1, 21):
    if i % 3 == 0:

        민기.append(i)

민기.reverse()
print(민기)
