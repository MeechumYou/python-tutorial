import mypackage as mp
import mypackage.mylib as ml
from mypackage.mylib import reverse

ret1 = mp.mylib.add_txt('대한민국', '1등')
ret2 = reverse(1, 2, 3)

print(ret1)
print(ret2)
