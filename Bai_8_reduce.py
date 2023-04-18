#reduce(function, sequence[, initial]) -> value
'''
- Trả về kết quả là MỘT giá trị đơn bằng cách áp dụng phương thức cho các item trong sequence
- Trong Python 2, nó là một hàm dựng sẵn. Tuy nhiên, trong Python 3, nó được chuyển sang module functools.
 Do đó, để sử dụng nó, bạn phải import functools
'''
from functools import reduce

def do_sum(x1, x2): 
    print("x1=",x1," x2=", x2)
    return x1 + x2

print(reduce(do_sum, [1, 5, 3, 4]))

def mult(x,y):
    print("x=",x," y=",y)
    return x*y

fact=reduce(mult, range(1, 4))
print ('Giai thừa của 3: ', fact)

tong =reduce(lambda x, y: x*y, range(1,4) )
print("Giai thừa của 3: ", tong)

