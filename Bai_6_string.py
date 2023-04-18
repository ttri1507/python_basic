#https://www.tutorialspoint.com/python/python_strings.htm
chuoi = "thiên thanh"

print(chuoi.capitalize())  #Thiên thanh"
print(chuoi.lower())  #thiên thanh"
print(chuoi.upper())  #THIÊN THANH"

print('a' + chuoi.center(21) + 'A')  #mặc định điền khoảng trắng (5 khoảng trắng trước và sau 'thiên thanh' trong TH này)
print('a' + chuoi.center(21,'N')+ 'A') #điền 5 chữ H trước và sau chuỗi 

s2 = """Mẹ, Mẹ là dòng suối dịu hiền Mẹ, Mẹ là bài hát thần tiên là bóng mát trên cao là mắt sáng 
trăng sao là ánh đuốc trong đêm khi lạc lối. Mẹ, Mẹ là lọn mía ngọt ngào.. """
print(s2.count("Mẹ"))    #đếm từ đầu -> cuối chuỗi
print(s2.count("Mẹ", 0, 10))  #đếm từ v.trí 0 --> 10

print("Demo find: ")
print(s2.find("là"))    #mặc định Tìm chuỗi "là" từ vị trí đầu đến vị trí cuối trong chuỗi và trả về vị trí nếu tìm thấy, -1 nếu không tìm thấy
print(s2.find("là", 10, 20)) 

s3 ="123465"
print(s3.isdigit())  #Có chứa tất cả các ký tự số k? (True/False)
s4 = s2.replace("Mẹ","Má")   #thay thế tất cả "Mẹ" bằng "Má"
print(s4)
s4 = s2.replace("Mẹ","Má", 3)  #thay thế 3 lần
print(s4)

s5 = "   Thiên Thanh    "
print(s5.strip() + 'end')   #cắt bỏ khỏang trắng đầu và cuối chuỗi
s6 = "___Thiên Thanh___"
print(s6.strip("_"))   #cát bỏ "_"" đầu và cuối chuỗi

s7 = "Trung Tâm Tin Học - DHKHTN"
ds = s7.split()     #cắt chuỗi dựa trên khoảng trắng
print(ds)
ds2 = s7.split(' ',2)
print(ds2)

print(s7.split(' ',1))