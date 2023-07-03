A, B, V = map(int, input().split())

X = (V-B) // (A-B)

if  V / (A-B) == V:
    print(X)
    
else:
    print(X+1)