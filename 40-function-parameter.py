
def add_txt(t1, t2='파이썬', t3='노드'):
  print(t1 + ' : ' + t2)
  print(t3)

# add_txt('베스트')
add_txt(t2='대한민국', t1='1등', t3='자스')

def func1(*args):
  print(args)

def func2(width, height, **kwargs):
  print(width)
  print(kwargs)

# func1()
# func1(3, 5, 1, 5)
# func2(10, 20)
# func2(10, 20, depth='50', color='blue')
