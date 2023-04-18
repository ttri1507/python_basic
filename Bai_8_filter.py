#filter(function, iterable)
'''
- Dùng để lọc các item trong sequence, tạo ra một sequence mới với các item thỏa điều kiện của function
'''
ages = [5, 18, 17, 12, 24, 32]
def tren_muoi_tam(x):  
  if x < 18:
    return False
  else:
    return True

adults = filter(tren_muoi_tam, ages)   #lọc các p.tử >=18
for x in adults:
  print(x)

list_number= [1, 2, 3, 4, 6, 7, 8, 9, 10] 
list_even_number = list(filter(lambda item: item % 2==0, list_number)) #lọc số chẵn
print('list_even_number', list_even_number)