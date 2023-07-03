T = int(input())

x = 0

           
for i in range(T):
    
    a, b, c = list(map(int, input().split()))
    
    d = c%a 
       
    if c / a == c // a:
        x = c // a
        
    else:
        x = (c // a) + 1
    
    
    # c를 a로 나눈 나머지가 0이면 => d == 0 이 되기 때문에 d = a를 해준다.
    # x가 10보다 작을때는 '호'수 앞에 0을 붙여준다.         
    if d == 0 and x < 10:
         d = a
         print("{}{}{}".format(d, 0, x))  
         continue
        
    if d == 0 and x >= 10:
        d = a
        print("{}{}".format(d, x))
        continue
        
    if d != 0 and x >= 10:
        print("{}{}".format(d, x))
        continue
    
    else: 
        print("{}{}{}".format(d, 0, x))

        

    
    
    