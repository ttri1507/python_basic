#https://www.tutorialspoint.com/python/python_functions.htm

'''
Ghi chú:
- Lambda có thể có một hoặc nhiều tham số đầu vào nhưng chỉ trả về một giá trị duy nhất
- Chỉ được phép chứa 1 dòng lệnh 
'''

a= 10
tong = lambda x, y: x+y+a
print(tong(5, 6))

#tính s = (x*x + 1)^n

s = lambda x, n : pow(pow(x, 2)+1, n)
print(s(3, 2))