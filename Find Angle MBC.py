import math

ab=int(input())
bc=int(input())

ca=math.hypot(ab,bc)
mc=ca/2
bm=mc #property of median from a right angle i.e.,bm==bc==mc
j=(bm**2+bc**2-mc**2)/(2*bm*bc) #maths formula to find the angles of a triange if the length all sides is known. 
bmc=math.acos(j) 
bmc=round(bmc*180/3.14)
str(bmc)
print(bmc,u'\N{DEGREE SIGN}',sep='') #sep: to add a separator between strings
