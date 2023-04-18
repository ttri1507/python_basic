# x = int(input("Nhập 1 số: "))
# if x==0:
#     pass
# else:
#     print(x)

#Minh họa break: tìm 1 số nguyên lớn nhất trong[1,100] chia hết cho n
'''
n = int(input("Nhập n: "))
max = 1
for i in range(1, 101):
    if i%n==0:
        max= i
print("max = ", max)
'''
#cách sau hay hơn
'''
n = int(input("Nhập n: "))
for i in range(100, 0,-1):
    if i%n==0:
        max= i
        break   #thoát ngang vòng lặp
print("max = ", max)
'''
#** Lưu ý: từ khóa break được sử dụng kèm theo điều kiện

#Minh họa continue 
tong = 0
for x in range(1, 101):
    if x%2==0:
        continue  #Quay lên đầu vòng lặp, bỏ qua các lệnh đứng sau nó
    tong+=x

print("Tổng lẻ: ", tong)

'''Nhận xét:
- break và continue chỉ xuất hiện kèm theo điều kiện
'''