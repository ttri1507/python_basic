import os
import pathlib
import csv

#Mở đọc file csv
'''
dd = os.getcwd() + "\\danhba.csv"
ttin = pathlib.Path(dd)
print("File: ", ttin)
if ttin.exists():
    f = open(dd,encoding="utf-8")
    for row in csv.reader(f):   #duyệt dòng
        #print(row)  #hoặc đọc từng cột 
        #print(row[0], "\t", row[1])
        chuoi = ""
        for col in range(0,len(row)):       #duyệt cột
            chuoi += row[col] + "\t"
        print(chuoi)
    f.close()
else:
    print("Không có tập tin này")
'''
#Mở ghi file csv
dd = os.getcwd() + "\\danhba.csv"
f = open(dd,'a', newline='', encoding="utf-8")      
listContent = [['Thiên Thanh', '0913 753852'], ['Thúy Huyền', '0989 753951'], ['Tường Vy','0903 123456']]
for item in listContent:        
    csv.writer(f).writerow(item)

f.close() 
print("Đã ghi file thành công")       