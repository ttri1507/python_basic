''' 
"a+": Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. 
The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'''
#Mở file ghi vào cuối
f = open("baihat.txt","a+", encoding="utf-8")  #lưu ý quan trọng, phải lưu tập tin chọn chế độ utf-8 (lưu chế độ nào thì mở chế đó, nếu k nó sẽ báo lỗi )
print("Xem thuộc tính: ")
print(f.closed,'\t', f.mode,'\t', f.name)    #xem các thuộc tính

f.seek(0)    #di chuyển con trỏ về đầu
print("Vị trí hiện hành của con trỏ" , f.tell())
str = f.read()   #đọc
print(str) # không có dữ liệu vì mở chế độ này con trỏ này nằm cuối file, nếu muốn đọc từ đầu phải dùng lệnh f.seek(0)

noidung = """2. GỢI NHỚ QUÊ HƯƠNG
Quê em hai mùa mưa nắng,
Hai thôn nghèo nối liền bờ đê,
Từng lũy tre xanh nghiêng nghiêng chiều hè,
Như bức tranh gợi tình quê đậm đà.
Lời ru con tiếng võng đong đưa.
Ai chờ ai thương giòng nước u buồn.
"""
f.write(noidung)    #Ghi vào cuối file
f.close()

