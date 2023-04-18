#phải import module math

import math
x = -45
print(abs(x))  #trị tuyệt đối 

print(math.ceil(5.25))  #Giá trị nguyên nhỏ nhất lớn hơn 5.25 
print(math.floor(5.25))  #Giá trị nguyên lớn nhất nhỏ hơn 5.25 
print(max(9, 5, 1, 10, 25, 3))  #Tìm số lớn nhất 
print(min(9, 5, 1, 10, 25, 3))  #Tìm số nhỏ nhất 

import random
n =  random.randrange(0, 20, 1) #tim số ngẫu nhiên trong khoảng 0->20, bước nhảy 1
print(n)
print(random.random())  #tìm số ngẫu nhiên trong khoảng > 0 và <1
print(random.uniform(3, 10))  #tìm số THỰC ngẫu nhiên torng khoảng > 3 và <10

