alpha="a"
lis=[]
for i in range(0,26):
    lis.append(alpha)
    alpha=chr(ord(alpha)+1)
while(1):
    e=""
    print("\n chooose from the following:\n")
    print("\t1.encryption\n \t2.decryption\n \t3.exit\n")
    c=int(input("enter a number:"))
    if(c==1):
        a=input("enter the string to be encripted:").lower()
        b=int(input("enter the addictive integer:"))
        for i in a:
            if i in lis:
                d=lis.index(i)
                f=((d+b)%26)
                e=e+lis[f]
            else:
                e=e+i
        print("\n\n",e)  
    if(c==2):
        a=input("enter the string for decryption:").lower()
        b=int(input("enter the addictive integer:"))
        for i in a:
            if i in lis:
                d=lis.index(i)
                f=((d-b)%26)
                e=e+lis[f]
            else:
                e=e+i
        print("\n\n",e)
    if(c==3):
        exit(0)             
          



