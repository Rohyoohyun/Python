# 좋아하는 음식을 공백을 기준으로 입력받아 음식의 개수와 종류를 출력하는 프로그램
food = list(input().split(' '))
print(f'좋아하는 음식의 개수 : {len(food)}')
for i in food:
    print(i)

# 공백을 기준으로 입력받은 수 중 짝수의 개수를 출력하는 프로그램
arr = list(map(int, input().split()))

cnt = 0
for i in arr:
    if ((i + 1)&1):
        cnt += 1
print(cnt)