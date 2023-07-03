# 한 자리 시작: 9 -> 0+9 = 9 -> 99 -> 9+9 = 18 -> 98 -> 9+8 = 17 -> 87
# 두 자리 시작: 26 -> 2+6 = 8 -> 68 -> 6+8 = 14 -> 84 -> 8+4 = 12 -> 42 -> 4 + 2 = 6 -> 26

N1 = int(input())
cnt = 1
N = N1


while True:   
    
    if len(str(N)) == 1:
        N = str(N)
        N = "0" + N
        
    N = int(N)

    a = N // 10 + N % 10
    
    b = str(N % 10)
    
    c = str(a % 10)
    
    d = b + c
    
    d = int(d)
        
    if N1 == d:
        break
    
    else:
        cnt += 1
        N = d
           
print(cnt)