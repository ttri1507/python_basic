'''
* MỞ RỘNG:
- Đọc ghi file có kiểm tra file hoặc thư mục có tồn tại hay không?
'''
import os
from os import path

dd = os.getcwd() + "\\baihat2.txt"
print("Thư mục hiện hành: ", dd)
if path.exists(dd):  #Kiểm tra file có tồn tại hay không?
    ff = open(dd, "r", encoding="utf-8")
    str = ff.read()
    print(str)
else:
    print("File này không tồn tại")
