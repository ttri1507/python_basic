#https://www.tutorialspoint.com/python/python_date_time.htm
#import 2 module time và datetime
import time

ticks = time.time()
print("Số ticks tính từ 12:00am, January 1, 1970:", ticks)

print(time.localtime())  #tgian hiện tại của hệ thống, xem ý nghĩa của cấu trúc theo link trên
print("Năm: " ,time.localtime()[0])  #lấy năm

print(time.asctime())    #trả về chuỗi thời gian theo định dạng

from datetime import datetime
print("Ngày giờ hiện tại: ", datetime.now() ) #trả về ngày giờ hiện thời của hệ thống

ngaysinh = datetime(2020,5,25)
print(ngaysinh ) #trả về ngày tháng năm truyền vào

#định dạng cho chuỗi kiểu ngày
date = datetime(1986, 2, 22)
print('Ngày tháng năm:', date.strftime('%d - %m - %Y'))
'''
Với: 
    %d : ngày kiểu số
    %m : tháng kiểu số
    %b : tháng kiểu chữ
    %y : năm với hai số cuối
    %Y : năm đầy đủ (4 số)
'''
