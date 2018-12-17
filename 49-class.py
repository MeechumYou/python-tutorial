class MyClass:
  var = '안녕하세요'
  def sayHello(self, *testVal):
    print(self.var)
    if testVal:
      for elem in testVal:
        print(elem)

obj = MyClass()
# print(obj.var)
obj.sayHello('parameter test')

obj.sayHello()
