L=int(input())
OG=list(input())
DG=list(input())
count=0
for i in range(L):
    a=abs(int(OG[i])-int(DG[i]))
    if a>5:
        count+=10-a
    else:
        count+=a
print(count)