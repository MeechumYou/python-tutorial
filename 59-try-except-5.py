from time import sleep

count = 1
try:
  while True:
    print(count)
    count += 1
    sleep(0.5)
except KeyboardInterrupt as keyExpt:
  print('사용자에 의해 중지')