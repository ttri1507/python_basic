#Làm việc với Calendar
from datetime import datetime
import calendar

print(calendar.isleap(2018)) #kiểm tra có phải năm nhuần không?
print(calendar.isleap(datetime.today().year)) #kiểm tra có phải năm nhuần không?

print(calendar.monthcalendar(2020,5)) #trả về danh sách các ngày trong tháng, năm được chọn, chia theo từng tuần, với giá trị 0 là ngày không nằm trong tháng của năm

print(calendar.weekday(2020,5,1)) #trả về thứ của ngày/tháng/năm, với giá trị số 0: Monday, 1: Tuesday…

print(calendar.monthrange(2020,5)) #trả về hai phần tử: phần tử đầu là thứ của ngày đầu tiên trong tháng, phần tử thứ hai là số ngày trong tháng.
print(calendar.monthrange(2020,5)[1]) #lấy tháng

