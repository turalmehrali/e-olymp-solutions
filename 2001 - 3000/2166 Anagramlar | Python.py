s1=input()
s2=input()

s2list=[]
b=True

for i in s2:
    s2list.append(i)
    
for i in s1:
    if i in s2list:
        s2list.remove(i)
    else:
        b=False
        
if b==True:
    print("YES")
elif b==False:
    print("NO")
