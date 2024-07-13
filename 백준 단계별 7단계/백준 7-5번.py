T = int(input())

a, b, c = list(map(int, input().split()))


g = 0
x = 0
y = 1

for i in range(c):
    g += 1
    if g <= a:
        continue
    else:
        g = 0
        continue
        
        
for j in range(c):
    x += 1
    if x <= a :
        y
    else:
        y+1
        x = 0
        continue
        
print("{}{}{}".format(g+1, 0, y))
        
        
