# print(divmod(11, 3))
# print(divmod(11, 3)[0])

a = 11113
b = 23
# ret1, ret2, ret3 = (1, 2, 3)
# print(ret1)
# print(ret2)
# print(ret3)
# ret3, ret4 = (1, 5)
# print(ret3)
# print(ret4)
ret1, ret2 = divmod(a, b)
print('%d / %d의 몫은 %d, 나머지는 %d입니다.' %(a, b, ret1, ret2))
