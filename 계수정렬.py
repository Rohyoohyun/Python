n, k = map(int, input().split())

arr = list(map(int, input().split()))
count = [0]*(max(arr)+1)

# 방법 1
for i in range(n):
    count[arr[i]] += 1

# 방법2
# sorted(arr, key=setting) # sorted와 .sort() 차이 알기

for i in range(k):
    print(f"{i+1} : {count[i]}")