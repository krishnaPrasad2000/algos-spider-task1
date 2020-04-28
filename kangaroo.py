a=list(map(int,input().split()))
x1=a[0]
x2=a[2]
v1=a[1]
v2=a[3]
if (x1!=x2 and v1==v22)
    print("YES")
elif(x2>x1 and v2>v1):
    print("NO")
elif(x1>x2 and v1>v2):
    print("NO")
else:
    
    while(True):
      
        x1=x1+v1
        x2=x2+v2
        if(x1==x2):
          
           print("YES")
           
           break
        elif((x2>x1 and v1<v2) or (x2<x1 and v2<v1)):
            print("NO")
            break
        elif((x1>x2 and v1<v2) or (x2>x1 and v2<v1)):
            continue
       
    
