'''Tạo dict từ 1 list '''
list_nguyen = [6, 8, 15, 3, 5]
list_chuoi = ["Mai", "Lan", "Cúc", "Trúc", "Đào"]

dict_new = dict.fromkeys(list_nguyen)  #gán giá trị mặc định cho key, lúc này value là none
# for i in range(0, len(list_nguyen)):
#     dict_new[list_nguyen[i]] = list_chuoi[i]

# print(list_nguyen.index(8))
# print(list_chuoi[list_nguyen.index(8)])

for ptu in list_nguyen:
    dict_new[ptu] = list_chuoi[list_nguyen.index(ptu)]

print(dict_new)