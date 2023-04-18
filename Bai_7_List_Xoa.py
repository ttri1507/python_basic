#tạo list
list_nguyen = [3, 4, 15, 56, 9, 1, 3]
list_thuc = [3.5, 4.2, 15.5, 56.3, 9.0]
list_chuoi = ["Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn"]

#xóa List
'''
print("Xóa")
print("List trước khi xóa: ", list_chuoi)
del(list_chuoi[1])
print("List sau khi xóa: ", list_chuoi)
print("Số p.tử sau khi xóa: ", len(list_chuoi))
'''
#remove p.tử khỏi vị trí index
# gt = list_chuoi.pop()   #remove p.tử cuối
# gt = list_chuoi.pop(2)   #remove p.tử có index thứ 2, Lưu ý: chỉ số phải nằm[0, len-1]
# print(gt)
# print(list_chuoi)

#xóa p.tử có gia trị cụ thể ra khỏi List, nếu không có phần tử cần xóa sẽ thông báo lỗi
list_chuoi.remove("Mẫu Đơn")
print(list_chuoi)
#Muốn dùng remove để xóa thì nên kiểm tra giá trị có tồn tại không (thao tác tìm kiếm)

