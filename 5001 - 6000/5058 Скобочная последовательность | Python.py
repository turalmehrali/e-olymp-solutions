class stack:
    items=[]
    def push(self,item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    def top(self):
        return self.items[len(self.items)-1]
    def pop(self):
        self.items.pop(len(self.items)-1)
    def empty(self):
        return self.items==[]

s=stack()
moterizeler=input()
flag=False
for simvol in moterizeler:
    if simvol=='(' or simvol=='[' or simvol=='{':
        s.push(simvol)
    
    if simvol==')':
        if s.empty()==False and s.top()=='(':
            s.pop()
        else:
            flag=True
            break
    
    elif simvol==']':
        if s.empty()==False and s.top()=='[':
            s.pop()
        else:
            flag=True
            break

    elif simvol=='}':
        if s.empty()==False and s.top()=='{':
            s.pop()
        else:
            flag=True
            break

if s.empty()==True and flag==False:
    print("yes")
else:
    print("no")
