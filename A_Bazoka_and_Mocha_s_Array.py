for i in range(int(input())):
    n=int(input())
    lissy=list(map(int,input().split()))
    count=0
    for i in range(0,len(lissy)-1):
        if lissy[i]<=lissy[i+1]:
            count+=1
        else:
            break
    x=lissy[:count+1]
    y=lissy[count+1:]
   
    if y+x==sorted(lissy):
        print("yes")
    else:
        print("no")
    