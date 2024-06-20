R,C=map(int,input().split())
L=[]
flag=True
for i in range(R):
    Lissy=input().split()
    L.append(Lissy)
for i in L:
    for j in i:
        if j in "CMY":
            print("#Color")
            flag =False
            break 
    if flag==False:
        break 
if flag==True:
    print("#Black&White")
    
            
