from collections import Counter
#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
X=int(input())
l1=list(map(int,input().split()))
d1=Counter(l1) 
sum=0
N=int(input())
for i in range(N):
    a=input().split()
    if (int(a[0]) in d1.keys()):
        if (d1[int(a[0])]>0):
            sum=sum+int(a[1])
            d1[int(a[0])]-=1          
print(sum)
