n = int(input('정수입력>'))

add = 0
for i in range(1, n+1):
    add *= i

print(f'{n}!의 값은 {add}')