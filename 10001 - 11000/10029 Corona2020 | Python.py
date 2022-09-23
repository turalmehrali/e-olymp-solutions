a,b,c=map(int,input().split())
if a+b+c==2020:
    print(a,"+",b,"+",c,sep="")
elif a-b+c==2020:
    print(a,"-",b,"+",c,sep="")
elif a+b-c==2020:
    print(a,"+",b,"-",c,sep="")
elif a-b-c==2020:
    print(a,"-",b,"-",c,sep="")
else:
    print("CORONA")
