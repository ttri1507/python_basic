dtb = float(input("Nhập điểm trung bình: "))

#1. điều kiện
'''
if dtb >=5:
    print("Đậu")
'''
#2. 2 điều kiện
'''
if dtb >=5:
    print("Đậu")
else:
    print("Rớt")
'''
# demo dtb rồi xếp loại học tập
if dtb<1 or dtb>10:
    print("DTB không hợp lệ")
else:
    if dtb<5:
        print("Yếu")
    elif dtb <7:
        print("TB")
    elif dtb<8:
        print("Khá")
    else:
        print("Giỏi")