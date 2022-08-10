x = list(input('문자열을 입력해주세요 :'))
y = list(input('중복 확인할 문자열을 입력해주세요 :'))
x1 = []
y1 = []
z = str()
n = 0
for i in x:
    n += 1
    if i == ' ':
        x1.append(z)
        z = str()
    elif n == len(x):
        z += i
        x1.append(z)
    else:
        z += i
n = 0
z = str()
for i in y:
    n += 1
    if n == len(y):
        z += i
        y1.append(z)
    else:
        z += i
n = 0
for i in x1:
    if i in y1:
        n += 1
print(n,'번 중복되었습니다.',sep='')