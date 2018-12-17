
class Add:
  def add(self, n1, n2):
    return n1 + n2

class Multiply:
  def multiply(self, n1, n2):
    return n1 * n2

class Calculator(Add ,Multiply):
  def sub(self, n1, n2):
    return n1 - n2

obj = Calculator()
print(obj.sub(2, 1))
print(obj.multiply(2, 2))
