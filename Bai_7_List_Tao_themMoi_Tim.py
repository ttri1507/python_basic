#Khai báo list
list_nguyen = [3, 4, 15, 56, 9, 1, 3]
list_thuc = [3.5, 4.2, 15.5, 56.3, 9.0]
list_chuoi = ["Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn"]

#Tạo list mới từ list đã có
'''
list_new = list_nguyen + list_chuoi     #dùng toán tử +
print(list_new)
list_new = list_chuoi * 3     #dùng toán tử *
print(list_new)
list_new = list_chuoi[2:]     #copy từ vị trí thứ 2
print(list_new)
list_new = list_chuoi[1:3]     #copy từ vị trí thứ 1 đến thứ 3 nhưng k lấy vi trí thứ 3
print(list_new)
'''

#Thêm p.tử vào cuối
# print("list_chuoi sau khi thêm:")
# list_chuoi.append("Cát Tường")
# print(list_chuoi)

# chèn 1 giá trị vào List
list_chuoi.insert(2, "Tử Đằng")  #chèn vào vị trí chỉ số thứ 2
print(list_chuoi)

#Tìm kiếm: dùng toán tử in, trả về true/false
# tim = "Lys" in list_chuoi
# if tim:
#     print("Có")
# else:
#     print("Không")

#tìm ph.tử, trả về index . Không tìm thấy sẽ báo lỗi (ValueError)
print("Index được tìm thấy: " , list_nguyen.index(9))
print("Index KHONG được tìm thấy: " , list_nguyen.index(-5))  #Lỗi