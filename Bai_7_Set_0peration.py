#1. Tạo set
set_chuoi = set(["Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn"])       #tạo từ 1 list

#5. Tìm kiếm, dùng toán tử in
print("Lys" in set_chuoi)  


#9. các thao tác về Set (Set Operations)
set1 ={1, 2, 6, 3, 7}
set2 ={1, 4, 5, 8, 9}
set_kq = set1 | set2    # set union: trả về tất cả các element không trùng nhau của các set
print(set_kq)

set_kq = set1 & set2    #Set Intersection: trả về các element cùng xuất hiện trong các set
print(set_kq)

set_kq = set1 - set2    #Set Difference: trả về các element chỉ có trong set này mà không có trong set kia
print(set_kq)

set_kq = set1 ^ set2    #Set Symmetric Difference: trả về các element không cùng xuất hiện trong các set
print(set_kq)
