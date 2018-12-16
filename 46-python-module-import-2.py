from time import sleep
# from mypackage import mylib
from mypackage.mylib import add_txt
from mypackage.mylib import reverse

sleep(2)
print(add_txt('나는', '자연인이다'))
print(reverse(1, 2, 3))