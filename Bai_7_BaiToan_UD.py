list_hoa=[]
tl = 1
while tl==1:
    hoa = input("Nhập tên hoa: ")
    list_hoa.append(hoa)
    tl = int(input("Bạn có muốn nhập tiếp(1/0): "))

print(list_hoa)
print("Tổng số hoa= ", len(list_hoa))
