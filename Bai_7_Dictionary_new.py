'''
**Lưu ý: 
- Khi demo thì nên theo từng thao tác
  1. Tạo Dic và Tạo dict mới từ list đã có
  2. Truy xuất
  3. Cập nhật giá trị của p.tử / Thêm p.tử vào cuôi
  4. Xóa p.tử  (xóa cuối, vị trí bất kỳ, xóa theo 1 giá trị cụ thể)
  5. Duyệt Dict
'''
#1. Tạo Dict
dict_hoa = {1:"Đào", 2:"Lys", 3:"Mộc Lan", 4:"Pensée", 5:"Mẫu Đơn"}
dict_new = dict_hoa.copy()
# print("Dictionary mới: ", type(dict_new))
# print("Dictionary mới: ", type(str(dict_new)))  #in dict dưới dạng chuỗi

# print("Dictionary mới: ", dict_new)
# print("Dictionary mới: ", str(dict_new))  #in dict dưới dạng chuỗi


#2. truy xuất
# print("Truy xuất: ")
# print(dict_hoa[1])    #Bị lỗi nếu không có giá trị trong key 
# print(dict_hoa.get(100))   #trả về none nếu không có giá trị trong key ==> dùng trong bài toán tìm kiếm

# print(dict_hoa.items())  #truy xuất bộ cặp key và value
# print("Keys: ", dict_hoa.keys())  #truy xuất bộ key
# print("Values: ", dict_hoa.values())  #truy xuất bộ value


#4. Xóa phần tử
# del dict_hoa[1] #xóa 1 p,.tử
# print(dict_hoa)
# dict_hoa.clear()  #Xóa hết các p.tử
# print(dict_hoa)
# del dict_hoa        #xóa luôn dict_hoa
# print(dict_hoa) #lỗi

#5. Duyệt
for key, value in dict_hoa.items():
    print("Key: ",key, '\t', "Value: ", value)

