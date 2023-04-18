'''
**Lưu ý: 
- Đặc điểm của Tuple: 
    - Không được phép cập nhật, do đó không có thao tác CẬP NHẬT, XÓA (xóa hết tuple thì OK)
    - Do đó không có các p.thức: sort, reverse, remove, pop, insert, extend, append
- Khi demo thì nên theo từng thao tác
  1. Tạo tuple và Tạo tuple mới từ một List đã có
  2. Truy xuất
  3. Xóa tuple
  4. Tìm kiếm tuple
  5. Duyệt List
  6. Tìm giá trị lớn, nhỏ nhất, Tính tổng
'''
#1. tạo tuple
print("Tạo tuple")
tuple_nguyen = (3, 4, 15, 56, 9, 1, 3)
tuple_thuc = (3.5, 4.2, 15.5, 56.3, 9.0)
tuple_chuoi = ("Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn")
print(tuple_chuoi)
''' tạo tuple từ List'''
list_mau = ["hồng", "đỏ", "cam", "tím", "xanh"]
tuple_mau = tuple(list_mau)
print(tuple_mau)

#2. truy xuất
# print("Truy xuất tuple")
# print(tuple_chuoi[2])
# print(tuple_chuoi[1:3])   #từ p.tử 1 -> 3-1

#3. xóa tuple
# del(tuple_nguyen)
# print(tuple_nguyen)

#4. Tìm kiếm
print("Index được tìm thấy: " , tuple_nguyen.index(9))

# duyệt
# for x in tuple_chuoi:
#     print(x)

'''
- Ghi chú: Tuple có khả năng chứa giá trị, đối tượng, list, …. 
( [1, 4], (3, 4) )  :  Một tuple chứa 1 list là [1, 4] và 1 tuple là (3, 4)
( 1, ‘t3h’, [1,3] ) :  Một tuple chứa số nguyên, chuỗi và 1 list là [3, 4]

- Lưu ý: khi muốn khởi tạo một Tuple chỉ duy nhất một phần tử, ta phải thêm dấu ',' vào sau giá trị đó, để báo cho Python biết, đây là Tuple.
VD : tup = (9, )  ==> OK
Tup = (9) ==> No OK, lúc đó nó hiểu kiểu số nguyên chứ k phải kiểu tuple

- Kết luận: Khi nào thì chọn Tuple thay cho List?
- Tuple khác List ở chỗ Tuple không cho phép bạn sửa chữa nội dung, còn List thì có. Vì đặc điểm đó, Tuple mạnh hơn List ở những điểm sau:
* Tốc độ truy xuất của Tuple nhanh hơn so với List
* Dung lượng chiếm trong bộ nhớ của Tuple nhỏ hơn so với List
* Bảo vệ dữ liệu của bạn sẽ không bị thay đổi

'''
nn = (9,)
print(type(nn))