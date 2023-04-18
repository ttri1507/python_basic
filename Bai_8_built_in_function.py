#map(function, iterables)
'''
- function : là hàm do người dùng định nghĩa, do python cấp, hoặc có thể dùng hàm vô danh (anonymous)
- iterables: sequence. Có thể có nhiều sequence
- Hàm map () thực thi một hàm được khai báo ứng với từng p.tử một trong 1 lần lặp. P.tử này được gửi đến hàm dưới dạng parameter
'''
def myfunc(sequence):
  return len(sequence)

x = map(myfunc, ('Táo', 'Cam', 'Quít'))  #tính chiều của mỗi p.tử trong tuple
print(x)
#chuyển kiểu map thành list
print(list(x))

def ham_nhieu_sequence(a, b):   #cộng 2 p.tử tương ứng lại với nhau trong 2 sequence
  return a + b
y = map(ham_nhieu_sequence, ('Trái ', 'Nải ', 'Giỏ '), ('cam', 'chuối', 'cherry')) #nhiều sequence
print(list(y))

''' hoặc dùng hàm do python cấp'''
from operator import add
list_one =[1,2,3,4,5]
list_two =[6,7,8,9,10]
list_tong = map(add, list_one,list_two)
print(list(list_tong))

''' dùng lambda thay thế hàm tường minh '''
list_tong = map(lambda item1 , item2: item1+item2 , list_one, list_two )  
print(list(list_tong))

#filter(function, iterable)
'''
- Dùng để lọc các item trong sequence, tạo ra một sequence mới với các item thỏa điều kiện của function
'''
ages = [5, 18, 17, 12, 24, 32]
def tren_muoi_tam(x):  
  if x < 18:
    return False
  else:
    return True

adults = filter(tren_muoi_tam, ages)   #lọc các p.tử >=18
for x in adults:
  print(x)

list_number= [1, 2, 3, 4, 6, 7, 8, 9, 10] 
list_even_number = list(filter(lambda item: item % 2==0, list_number)) #lọc số chẵn
print('list_even_number', list_even_number)

#reduce(function, sequence[, initial]) -> value
'''
- Trả về kết quả là MỘT giá trị đơn bằng cách áp dụng phương thức cho các item trong sequence
- Trong Python 2, nó là một hàm dựng sẵn. Tuy nhiên, trong Python 3, nó được chuyển sang module funcools.
 Do đó, để sử dụng nó, bạn phải import funcools
'''
from functools import reduce
def do_sum(x1, x2): 
    return x1 + x2
print(reduce(do_sum, [1, 2, 3, 4]))

def mult(x,y):
    print("x=",x," y=",y)
    return x*y

fact=reduce(mult, range(1, 4))
print ('Giai thừa của 3: ', fact)

tong =reduce(lambda x, y: x*y, range(1,4) )
print("Giai thừa của 3: ", tong)

