a = int(input())
b = int(input())
lst = []

for i in range(a, b+1):
    cnt = 0       
    
    if i > 1:
        for j in range(2, i):
            if i % j == 0: 
                cnt += 1
                break
            
        if cnt == 0:
            lst.append(i)
                
if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
    
else:
    print('-1')
        
# for문 돌리고 그 안에 if문 넣어서 리스트에 for문 돌린 변수값을 넣어주고 sum 해준다