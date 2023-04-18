#1. Tạo set
set_nguyen ={2, 3, 45, 20, 7, 15}
set_nhieukieu = {2, 15, "Hoa Hông", ("Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn")}
set_rong = set()
set_chuoi = set(["Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn"])       #tạo từ 1 list

#3. Thêm p.tử vào set
# print(set_nguyen)
# set_nguyen.add(5)
# print(set_nguyen)

#4. Xóa phần tử
set_nguyen.discard(9)
#set_nguyen.remove(9)        #không có giá trị sẽ báo lỗi
print(set_nguyen)
#set_chuoi.clear()  #xóa hết các element
print(set_chuoi)

#del(set_nguyen)     #xóa luôn set
#print(set_nguyen)  #lỗi

#6. Lấy element ra khỏi set
s = set_chuoi.pop()
print("pop phần tử đầu tiên: " , s)
print(set_chuoi)

#7. Duyệt Set: giống như list
#8. sắp xếp: hàm sorted sẽ chuyển về list rồi trả kết quả
# print("sắp xếp tăng")
# print(sorted(set_nguyen))  #tăng

print("sắp xếp giảm")
print(sorted(set_nguyen, reverse=True)) #giảm
