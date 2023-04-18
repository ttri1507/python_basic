n = 0
try:
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    #có thể ném lỗi cụ thể 
    if y==0:
        raise ZeroDivisionError("không chấp nhận y=0")
    if x%2 !=0:
        raise Exception("Bạn phải nhập số x chẵn")
    n = x/y
except NameError as err1:   
    print("Lỗi 1: ", err1)
except ZeroDivisionError as err2:
    print("Lỗi: ", err2)
except ValueError as err3:   
    print("Lỗi 3: Bạn phải nhập số")
except Exception as err3:     #Lỗi chung luôn nằm sau cùng, nằm sau các lỗi cụ thể
    print("Lỗi: ", err3)

print("n = ", n)