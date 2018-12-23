
# for i in range(3, int(1113/2), 2):
#   print(i)

def getPrime(x):
  # 2로 나눠 떨어지면 2가 약수. return.
  if x % 2 == 0:
    return

  # range: start, end, interval
  for i in range(3, int(x/2), 2):
    if x % i == 0:
      break
  else:
    return x

listdata = [117, 119, 1113, 11113, 11119]
# listdata = [119]
ret = filter(getPrime, listdata)
print(list(ret))
