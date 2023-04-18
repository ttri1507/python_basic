'''
3. Định nghĩa 1 Exception riêng
- Bằng cách kế thừa các lớp nằm trong standard built-in exception
'''
class bay_loi(Exception):
    def __init__(self, thong_bao):
        self.thong_bao = thong_bao
n = 0
try:
    #x = int(input("Nhập 1 số: "))   #nhập chuỗi ==> gọi Exception
    x = input("Nhập 1 số: ")        #nhập bật cứ ... ==> gọi bay_loi vì input là nhập chuỗi
    print(type(x))
    if type(x)!=int:
        raise bay_loi("Phải nhập số nguyên")
except bay_loi as err1:   
    print("Lỗi : ", err1)
except Exception as err:
    print("Lỗi chung : ", err)
else:
    print(x)