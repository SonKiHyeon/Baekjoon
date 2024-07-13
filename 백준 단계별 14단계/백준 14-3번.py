n = int(input())
lst = []
lst2 = []
lst3 = []

for i in range(n):
    a = input()
    lst.append(a)
    # IO = In Out 
    IO = lst[i][len(lst[i])-5:]
    lst2.append(IO)

for j in range(n):
    answer = ""
    if lst2[j] == "enter":
        answer = lst[j][:len(lst[i])-6]
        lst3.append(answer)
    else:
        wrong = lst[j][:len(lst[i])-6]
        for k in range(len(lst3)):
            if lst3[k] == wrong:
                del lst3[k]
                break

A = lst3.sort(reverse=True)    
print(*lst3, sep="\n")


        
