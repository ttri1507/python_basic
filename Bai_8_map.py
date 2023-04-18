#cú pháp: map(function, iterables)
'''
- function : là hàm do người dùng định nghĩa, do python cấp, hoặc có thể dùng hàm vô danh (anonymous)
- iterables: sequence. Có thể có nhiều sequence
- Hàm map () thực thi một hàm được khai báo ứng với từng p.tử một trong 1 lần lặp. 
P.tử này được gửi đến hàm dưới dạng parameter
'''
def myfunc(element):
  return len(element)

# x = map(myfunc, ('Táo', 'Sầu riêng', 'Quít'))  #tính chiều của mỗi p.tử trong tuple
# print(x)
# print(list(x))  #chuyển kiểu map thành list

def ham_nhieu_sequence(a, b):   #cộng 2 p.tử tương ứng lại với nhau trong 2 sequence
  return a + b

# y = map(ham_nhieu_sequence, ('Trái ', 'Nải ', 'Giỏ ', 'Thùng'), ('cam', 'chuối', 'cherry')) #nhiều sequence
# print(list(y))

''' hoặc dùng hàm do python cấp'''
from operator import add

list_one =[1,2,3,4,5, 100]
list_two =[6,7,8,9,10]
# list_tong = map(add, list_one,list_two)
# print(list(list_tong))

''' dùng lambda thay thế hàm tường minh '''
list_tong = map(lambda item1 , item2: item1+item2 , list_one, list_two )  
print(list(list_tong))