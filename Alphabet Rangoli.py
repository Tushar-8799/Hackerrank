import string

def print_rangoli(size):
    abcd = string.ascii_lowercase #string of a to z
    l1=[]
    for i in abcd:
        l1.append(i)
    #l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=int(size)

    l2=l1[0:s]
    l2.reverse()  
    #l2=['z','y',.....,'a']
    
    l3=l1[0:s]

    if s==1:
        print("a")
    else:
        for i in range(s):
            #Left upper Half  
            for j in range(s-1-i):
                print("--",end="")
            for m in range(i+1):
                print(l2[m]+"-",end="") 
                
            #Right Upper Half 
            x=1
            for m in range(s-i,s):
                print(l3[m],end="")
                if x<s-1:
                    print("-",end="")
                x=x+1
    
            for j in range(2*(s-1-i)-1):
                print("-",end="")
            print("")
                
        for k in range(s-1):
            #Left Lower Half       
            for l in range(k+1):
                print("--",end="")
            for p in range(s-k-1):
                print(l2[p]+"-",end="")
                
            #Right Lower half     
            for p in range(k+2,s):
                print(l3[p]+"-",end="")
            for l in range(2*(k+1)-1):
                print("-",end="")
            print("")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
