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
def hesabla(a,b,i):
    if i=='+':
        return a+b
    elif i=='-':
        return a-b
    elif i=='*':
        return a*b
    elif i=='/':
        return a/b

s=stack()
emeliyyatlar='+-*/'
postfix=input()
for simvol in postfix:
    if simvol.isdigit():
        s.push(int(simvol))
    elif simvol in emeliyyatlar:
        b=s.top()
        s.pop()
        a=s.top()
        s.pop()
        s.push(hesabla(a,b,simvol))
print(hesabla(a,b,simvol))
