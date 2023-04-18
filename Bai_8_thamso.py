''' Có 4 loại tham số
- Required argument (tham số bắt buộc)
- Keyword argument (tham số từ khóa)
- Default argument (tham số mặc định)
- Variable-length argument (tham số thay đổi không xác định)
'''
#tham số bắt buộc: khi gọi hàm phải truyền đầy đủ, không được bỏ qua
#Tham số từ khóa: truyền tham số theo tên, không theo vị trí đả khai báo
def cong_ba_so(a, b, c):
    tong = a+b+c
    return tong

# tg = cong_ba_so(3, 6, 2)
# tg = cong_ba_so(5, c= 9, b = 10)
# print(tg)
# tg = cong_ba_so(c= 9, b = 10, a =4)
# print(tg)

# Default argument (tham số mặc định)
def nhan_hai_so(a, b=5):
    kq = a*b
    return kq
tich = nhan_hai_so(5, 10)
print(tich)
tich = nhan_hai_so(5)
print(tich)

''' Lưu ý:
def nhan_hai_so_2(a=5, b):  #No OK vì tham số mặc định phải đứng sau tham số bắt buộc
    kq = a*b
    return kq
'''
#Variable-length argument (tham số thay đổi không xác định), ts cũng phải nằm cuối
def cong_cac_so(x, *y):
    tg = x
    for n in y:
        tg += n
    return tg

tong = cong_cac_so(3, 6, 8, 9)
print(tong)
tong = cong_cac_so(3, 6, 8, 9, 5)
print(tong)





