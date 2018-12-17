class MyClass:
  def __init__(self, args):
    self.var = '안녕하세요!'
    print('MyClass 생성')
    print('생성자 인자 : ' + args)

obj = MyClass('철수')
print(obj.var)
