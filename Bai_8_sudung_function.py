#import Bai_8_function    ==> khi dùng phải Bai_8_function.cong_hai_so
import Bai_8_function as tv   #đặt bí danh

#from Bai_8_function import tru_hai_so      # ==> khi dùng cong_hai_so

dai = int(input("Nhập chiều dài: "))
rong = int(input("Nhập chiều rộng: "))
dt = tv.dien_tich_hcn(dai,rong)  #gọi hàm trả về giá trị, dùng 1 biến hứng nó
print("Diện tích HCN: ", dt)

tv.dien_tich_hcn_2(dai,rong);  #gọi hàm KHÔNG trả về giá trị, dùng 1 biến hứng nó

#sử dụng biến toàn cục
#print("Biến toàn cục: ", tv.bientoancuc)

#tham trị
'''
x = 5
y = 10
print("x trước khi gọi hàm: ", x)
z = tv.cong_hai_so(x, y)
print("x sau khi gọi hàm: ", x)
print("z = ", z)
'''
#Muốn truyển số nguyên kiểu tham chiếu, phải truyền list (thủ thuật)

x = [5]
y = 10
print("x trước khi gọi hàm: ", x[0])
z =  tv.tru_hai_so(x, y)
print("x sau khi gọi hàm: ", x[0])
print("z = ", z)

#truyền tham chiếu
lst = ["Đào", "Tử Đằng"]
print("Trước: ",lst)
tv.ds_hoa(lst)
print("Sau: ",lst)

#Hàm trả về nhiều giá trị
chuoi, so = tv.fun1()   #trả về tuple
print(chuoi, ' - ', so)

list_ham = tv.fun2()    #trả về list
print(list_ham)

dict_ham = tv.fun3()    #trả về dictionary
print(dict_ham)

