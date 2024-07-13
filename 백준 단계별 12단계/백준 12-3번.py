N = list(map(int, input().split()))
a = N[0] 
b = N[3]
e = N[1]
f = N[4]


N[0] = b * N[0]
N[1] = b * N[1]
N[2] = b * N[2]
N[3] = a * N[3]
N[4] = a * N[4]
N[5] = a * N[5]

c = N[1] - N[4]
d = N[2] - N[5]

for i in range(-999, 999+1):
    if(c * i == d) == True:
        break

y = i

for j in range(-999, 999+1):
    if(N[0] * j + N[1] * y == N[2]) == True:
        break
    
x = j

if (a * x or e == 0) and (b * y or f) == 0:   
    print("해가 없습니다.")

else:
    print(x, y)




