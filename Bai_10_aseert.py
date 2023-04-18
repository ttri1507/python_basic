'''
1. Sử dụng assert
- Khi gỡ rối lỗi mã. (debugging code) ==> người LT thường dùng để kiểm code
- Từ khóa khẳng định được sử dụng khi gỡ lỗi mã.
- Cho phép kiểm tra xem điều kiện có trả về True không, nếu không, chương trình sẽ phát sinh một AssertsError.
- Có thể viết 1 t.báo cụ thể khi nó trả về false 
'''
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
assert (y!=0), "Số chia y phải khác 0"
n = x/y
print(n)
