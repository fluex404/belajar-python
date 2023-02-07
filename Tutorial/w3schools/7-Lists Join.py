list1 = ['a','b','c']
list2 = [1, 2, 3]

list3 = list1+list2
print(list3)

print([3, 4, 3]+[2, 1])

listR = ([3, 4, 3] + [2, 1])
listR.sort()
print(listR)

listR.extend(list3)
print(listR)