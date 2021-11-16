l1=list(map(int,input().split())) #l1=[row, column]
r=l1[0] #row
c=l1[1] #column
if r%2 ==0:
    r1=r-1 #converting even row into odd row
    ans=((r1-1)*5)+((c-1)*2)  #I've just generated a simple formula to calculate the value at given location
    print(ans+1)
else:
    ans=((r-1)*5)+((c-1)*2)
    print(ans)
