a = str(input())
b = 3

alpha1 = "ABCDEFGHIJKLMNOPQRSTUV"
alpha2 = "WXYZ"
c = list(alpha1)
d = list(alpha2)

for i in range(len(a)):
    for j in range(1, 7 + 1):
        if a[i] in c[(j * 3) - 3 : (j * 3) - 1] : 
            b += j 
    if a[i] in d:
        b += 9
print(b)