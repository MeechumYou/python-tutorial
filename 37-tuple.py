tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c'])
# tuple1[0] = 5

def myFunc():
  print('안녕하세요')

tuple4 = (1, 2, myFunc)
tuple4[2]()
