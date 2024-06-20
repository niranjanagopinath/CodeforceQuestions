
for i in range(int(input())):
    a=int(input())
    if a%3==0:
        print(int(a/3),int(a/3))
    
    else:
        if (int(a//3)+1)+2*(int(a//3))==a:
            print(int(a//3)+1,int(a//3))
        else:
            print(int(a//3),int(a//3)+1)