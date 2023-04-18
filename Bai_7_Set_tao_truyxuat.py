''' 
https://www.programiz.com/python-programming/set
**Lưu ý: 
- Set có thể chứa nhiều kiểu DL khác nhau
  Các phần tử trong set không theo thứ tự thêm vào, không sử dụng index
  Giá trị không được trùng, không dược thay đổi
- Khi demo thì nên theo từng thao tác
  1. Tạo Set
  2. Truy xuất
  3. Thêm p.tử vào set
  4. Xóa p.tử 
  5. Tìm kiếm
  6. Lấy element ra khỏi set
  7. Duyệt Set
  8. Sắp sếp
  9. Các thao tác về set
'''
#1. Tạo set
set_nguyen ={2, 3, 45, 20, 7, 15}
set_nhieukieu = {2, 15, "Hoa Hông", ("Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn")}
set_rong = set()
set_chuoi = set(["Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn"])       #tạo từ 1 list
print("Set nguyên: ", set_nguyen)
print("Set nhiều kiểu: ", set_nhieukieu)
print("Set rỗng: ", set_rong, ', Kiểu: ', type(set_rong))
print("Set chuỗi: ", set_chuoi)

set_copy = set_chuoi.copy() #tạo bản sao

#set_phuc = {3, 5, "Lys", [2, 5, 6]}  #No OK vì list chứa các item có thể thay đổi, trong khi set là không thể thay đổi (unmutable)

#2. Truy xuất; vì set không có index nên không có truy xuất, tuy nhiên  ta sẽ dùng thủ thuật
n = list(set_nguyen)[2] #chuyển về list rồi truy xuất  
print(set_nguyen)
print(n)