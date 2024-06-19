# Bài tập 1: Cho một số nguyên x bất kỳ. Hãy in ra màn hình dòng chữ: "Đây là số chẵn" nếu x là số chẵn, ngược lại hãy in ra màn hình dòng chữ: "Đây là số lẻ"
x = 3
if x %2 == 0:
  print('đây là số chẵn')
else: 
  print('đây là số lẻ')

'''
Bài tập 2: Cho một chuỗi ký tự s = 'Hello world!'. Hãy in ra màn hình các thông tin như sau:
  3 ký tự đầu tiên của chuỗi
  Các ký tự từ index số 3 cho tới index số 7
  Kiểm tra xem có tồn tại ký tự 'w' ở trong chuỗi hay không, nếu có hãy in ra màn hình dòng chữ: "Tồn tại ký tự w ở trong chuỗi"
'''
s = 'Hello world!'
for i in s:
  if i == 'w':
    print(s[0:3], s[3:7], sep = ' | ')
    print('tồn tại ký tự w trong chuỗi')

'''
Bài tập 3: Cho 2 danh sách các số nguyên bất kỳ có từ 5 phần tử: list_1 và list_2
  Thêm vào list_1 phần tử có giá trị 50 vào cuối list
  Cập nhật giá trị phần tử tại index 2 của list_2 với giá trị là: 100
  In ra màn hình tích của phần tử đầu tiên của list_1 với phần tử cuối cùng của list_2
  Trả về kết quả tổng của 2 list con:
    Danh sách con đầu tiên: trích xuất các phần tử của list_1 từ vị trí index 2 cho tới index 4
    Danh sách con thứ hai: trích xuất các phần tử của list_2 từ index 3 cho tới phần tử cuối cùng
'''
list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

list_1.append(50)
print(list_1)

list_2.insert(2,100)

list_1[0] * list_2[-1]

list_1[2:4] + list_2[3:6]

'''
Bài tập 4: Cho một biến có tên là year thể hiện năm. Hãy in ra màn hình dòng chữ: "Năm đó là năm nhuận" nếu year là năm nhuận, ngược lại thì in ra: "Năm đó không phải là năm nhuận".
! Lưu ý: những năm nào chia hết cho 4 được và không chia hết cho 100 được coi là năm nhuận (ví dụ năm 2100 không phải là năm nhuận, 2104 là năm nhuận), nếu kết quả chia hết cho 400 thì năm đó là năm nhuận
'''
year = 2024
if (year %4 == 0) and (year %100 != 0):
  print('Năm đó là năm nhuận')
else:
  print('Năm đó không phải năm nhuận')

year = 2024
if (year %4 == 0 and year %100 != 0) or (year %400 == 0):
  print('Năm đó là năm nhuận')
else:
  print('Năm đó không phải năm nhuận')
  
'''
Bài tập 5: Cho 1 dãy số các số nguyên bất kỳ, in ra số lượng các số chẵn, số lượng các số lẽ xuất hiện trong dãy
'''
for i in range(1,100):
  if i %2 == 0:
    print(i, end = ' ')
    i += 2

for i in range(1,100):
  if i %2 == 1:
    print(i, end = ' ')
    i += 2

s = [1,2,3,5,7,9]
sl_chan = 0
sl_le = 0
for i in s:
  if i %2 == 0:
    sl_chan += 1
  else:
    sl_le += 1
print('số lượng số chẵn: ', sl_chan)
print('số lượng số lẻ: ', sl_le)

'''
Bài tập 6: Cho một chuỗi ký tự bất kỳ (bao gồm: ‘A’->’Z’,’a’-> ‘z’). Đếm trong chuỗi đó có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường?
'''
c = 'HewoABCDXYZ'
sl_lower = 0
sl_upper = 0
for i in c:
  if i.islower():
    sl_lower += 1
  if i.isupper():
    sl_upper += 1
print('upper = ', sl_upper)
print('lower = ', sl_lower)

c = 'HewoABCDXYZ'
sl_lower = 0
sl_upper = 0
for i in c:
  if 'a' <= i <= 'z':
    sl_lower += 1
  if 'A' <= i <= 'Z':
    sl_upper += 1
print('upper = ', sl_upper)
print('lower = ', sl_lower)

'''
Bài tập 7: Cho một số nguyên dương a bất kỳ (a nằm trong đoạn [0,1000]). Liệt kê tất các bội số của a nằm trong đoạn [0,1000]
'''
a = 500
for i in range(0,1001):
  if i % a == 0:
    print(i, end = ' ')

'''
Bài tập 8: Tìm giá trị lớn nhất và giá trị nhỏ nhất xuất hiện trong dãy số bất kỳ
'''
s = range(0,1001)
_max = s[0]
_min = s[0]
for i in s:
  if i > _max:
    _max = i
  if i < _min:
    _min = i
print('max = ', _max)
print('min = ', _min)

'''
Bài tập 9: Xây dựng 1 hàm dùng để kiểm tra 1 số nguyên dương có phải là số nguyên tố hay không. 
Sau đó cho 1 danh sách các số nguyên bất kỳ, hãy tính tổng các số nguyên tố có trong dãy số
'''
def list_check (x):
  if x <= 1:
    return 0
  for i in range(2,x):
    if x % i == 0:
      return 0
  else: return 1

A = [1,2,3,4,5,6,7,8,9,10]
S = 0
for i in A:
  if list_check(i) == 1:
    S += i
print(S)

'''
Bài tập 10: Xây dựng 1 hàm để kiểm tra 1 password có phải là 1 password hợp lệ hay không. Sau đó cho 1 danh sách password bất kỳ, hãy đếm số lượng password hợp lệ có trong dãy số đó.
  Một password hợp lệ khi và chỉ khi thỏa mãn tất cả các điều kiện sau:
      Ít nhất 1 chữ cái nằm trong [a-z]
      Ít nhất 1 số nằm trong [0-9]
      Ít nhất 1 kí tự nằm trong [A-Z]
      Ít nhất 1 ký tự nằm trong [$ # @]
      Độ dài mật khẩu tối thiểu: 6
      Độ dài mật khẩu tối đa: 12
'''
def _password(x):
 
  if len(x)<6 or len(x)>12:
    return 'not legit'

  _upper = 0
  _lower = 0
  _digit = 0
  _special = 0

  for i in x:
    if i.islower(): 
      _lower += 1
    else: 
      _upper += 1
    if i.isdigit(): 
      _digit += 1
    if i in ('#', '$', '@'): 
      _special += 1

  if _lower >= 1 and  _upper >= 1 and _digit >= 1 and _special >= 1:
    return 'legit'
  else: 'not legit'


pass_list = ('hewo', 'Vhh2912!', 'Hh2912@23')
legit_count = 0

for i in pass_list:
  if _password(i) == 'legit':
    legit_count += 1

print(legit_count)












