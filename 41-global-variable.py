
param = 10
strdata = '전역'

def func1():
  strdata = '지역'
  print(strdata)

def func2(param):
  param = 1

def func3():
  global param
  param = 50

func3()
print(param)