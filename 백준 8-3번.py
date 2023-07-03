N = int(input())
a = 2

for i in range(2, N + 1):
    
    if N == 1:
        break
        
    if N % a == 0:
        N = N // a
        print(a)
        
    else:
        a += 1
        
        if N % a == 0:
            N = N // a
            print(a)
            
        else:
            pass
        