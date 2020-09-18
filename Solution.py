try:
    t=int(input())
    for i in range(t):
        s=input()
        a=0
        b=0
        for i in s:
            if(i=='a'):
                a+=1;
            else:
                b+=1;
        if(a==len(s) or b==len(s)):
            print("0")
        else:
            print(min(a,b))
except:
    pass;
    
