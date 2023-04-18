#Duyệt chạy theo số lần xác định
# x = 0
# while x<=5:  #Biểu thức điều kiện
#   print(x)
#   x +=1    

'''
Lưu ý: 
- Phải tồn tại ít nhất 1 dòng lệnh làm thay đổi biểu thức đ.kiện ==> để vòng lặp có đg thoát
- Có thể while không lặp lại 1 lần nào cả
'''
so = int(input("Nhập 1 số cửu chương: "))
i = 1
while i<=10:
    print("{} * {} = {}".format(so,i, so*i))
    i +=1
