list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c']]
list1[0] = 6
print(list1)
def myFunc():
  print('inner Function')
  
list4 = [1, 2, myFunc]
list4[2]()
