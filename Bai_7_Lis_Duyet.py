#tạo list
list_nguyen = [3, 4, 15, 56, 9, 1, 3]
list_thuc = [3.5, 4.2, 15.5, 56.3, 9.0]
list_chuoi = ["Đào", "Lys", "Mộc Lan", "Pensée", "Mẫu Đơn"]

#duyệt List
# tg = 0
# for n in list_nguyen:  #duyệt để tính tổng các giá trị lẻ trong list
#     if n%2 != 0:
#         tg += n
# print("Tổng số lẻ: ", tg)

tong = 0
#Cách 1
# for index in range(0,len(list_nguyen),2):  #duyệt để tính tổng các p.tử ở vị trí lẻ (chỉ số chẳn)
#     tong += list_nguyen[index]

'''cách 2
for index in range(0,len(list_nguyen)):  #duyệt để tính tổng các p.tử ở vị trí lẻ
    if (index+1)%2 !=0:
        tong += list_nguyen[index]
'''
# tong = sum(list_nguyen)
# print(tong)

#bải toán tính trung bình
# tg = 0;
# for n in list_nguyen: 
#     tg += n
# tb = tg/len(list_nguyen)
# print("Trung bình: ", tb)

#tìm max, min
max = max(list_nguyen)
min = min(list_nguyen)
print("Min = ", min)
print("Max = ", max)

