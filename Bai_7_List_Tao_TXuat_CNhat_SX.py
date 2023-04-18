'''
**Lưu ý: 
- Khi demo thì nên theo từng thao tác
  1. Tạo List và Tạo List mới từ List đã có
  2. Truy xuất
  3. Thêm p.tử vào List (vào cuối, chèn ngang)
  4. Xóa p.tử  (xóa cuối, vị trí bất kỳ, xóa theo 1 giá trị cụ thể)
  5. Cập nhật giá trị của p.tử
  6. Tìm kiếm
  7. Duyệt List
  8. Sắp xếp (sort)
  9. Tìm giá trị lớn, nhỏ nhất, Tính tổng
'''
#tạo list
list_nguyen = [3, 4, 15, 56, 9, 1, 3]
list_thuc = [3.5, 4.2, 15.5, 56.3, 9.0]
list_chuoi = ["Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn"]

#truy xuất
print(list_nguyen[2])
print(list_thuc[2])
print(list_chuoi[2])

#cập nhật List
print("Cập nhật")
list_thuc[2] = 10.5
print(list_thuc[2])
print(list_thuc)

#tim giá trị lớn/nhỏ nhất : dùng hàm max, min
ln = max(list_nguyen)
print("Max = ", ln)
print("Min chuỗi = ", min(list_chuoi))

#Đếm số lần xuất hiện của 2 p.tử
print("số lần xuất hiện 3 trong list_nguyen: ", list_nguyen.count(3))

#sắp xếp List
list_chuoi.sort()   #sx tăng
print("Đã sx: ", list_chuoi)
list_chuoi.reverse()  #đảo lại
print("Đảo lại: ", list_chuoi)