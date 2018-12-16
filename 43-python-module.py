import time
import mylib

print('5초간 정지합니다')
time.sleep(5)
print('정지해제')

ret1 = mylib.add_txt('5', '4')
ret2 = mylib.reverse(1, 2, 3)

print(ret1)
print(ret2)