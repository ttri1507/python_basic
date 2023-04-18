#2. Sử dụng các standard exception do Python cấp
'''
try:
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    n = x/y
    print("n = ", n)
except ZeroDivisionError as err:
    # print("Lỗi: ", err)
    print("Lỗi: Bạn đã nhập y = 0" )  #thực tế
except ValueError as err:
    print("Lỗi: Bạn phải nhập số" )  #thực tế
'''
#- Khai báo cụ thể mã Exception
'''* Trường hợp: liệt kê từng lỗi cụ thể'''
n = 0
try:
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    #có thể ném lỗi cụ thể 
    # if y==0:
    #     raise ZeroDivisionError("không chấp nhận y=0")
    n = x/y
except NameError as err1:   
    print("Lỗi 1: ", err1)
except ZeroDivisionError as err2:
    print("Lỗi 2 chia 1 số cho 0: ", err2)
except ValueError as err3:   
    print("Lỗi 3: Bạn phải nhập số")
except Exception as err3:     #Lỗi chung luôn nằm sau cùng, nằm sau các lỗi cụ thể
    print("Lỗi: ", err3)
else:    #khi không có exception nào 
    print("n1 = ", n)
finally:   #khi KHÔNG hoặc CÓ exception vẫn thực hiện 
    print("n2 = ", n)
