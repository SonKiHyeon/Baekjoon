N = int(input())

a = list(map(int, input().split()))

b = 0

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
# 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20

for i in range(N):
    if a[i] == 1:
        continue

    if a[i] == 2 or a[i] == 3:
        b += 1
        
    # 소수가 아닐 때 넘기고 소수 일 때 1씩 더해준다
    if a[i] % 2 == 1:
        if a[i] % 2 == 0 or a[i] % 3 == 0:
            pass
            
        else:
            b += 1
        
print(b)
