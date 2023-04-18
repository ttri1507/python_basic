import os, sys
#lấy ra đường dẫn đến thư mục module ở trong project hiện hành
#D:\NHUNG\DEMO_PYTHON\Thu_vien
lib_path = os.path.abspath(os.path.join('Thu_vien'))

#thêm thư mục cần load vào trong hệ thống
sys.path.append(lib_path)

print(lib_path)

from Tinh_hai_so import *

x , y = 3, 10
print(Cong(x, y))
print(Tru(x, y))
print(Nhan(x, y))
print(Chia(x, y))

import Tinh_hai_so
print(dir(Tinh_hai_so))
print(dir(Tinh_hai_so)[7])