list1 = []
for i in range(1, 6):
    list1.append(i)
print(list1)

list2 = [1, 2, 3, 4, 5]
removed_item = list2.pop(0)
print(removed_item)
print(list2)

list3 = [1, 2, 3, 4, 5]
list3.remove(2)
print(list3)

list4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
list4.sort()
print(list4)

list5 = [1, 2, 3, 4, 5]
list5.reverse()
print(list5)