class queue:
    items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def size(self):
        return len(self.items)
    def front(self):
        return self.items[len(self.items)-1]
    def back(self):
        return self.items[0]
    def dequeue(self):
        self.items.pop(len(self.items)-1)
    def isempty(self):
        return self.items==[]

q=queue()
emr=''

while True:
    emr=input()
    if emr=='exit':
        print('bye')
        break
    elif emr=='clear':
        while q.size()>0:
            q.dequeue()
        print('ok')
    elif emr=='front':
        if q.isempty():
            print('error')
        else:
            print(q.front())
    elif emr=='pop':
        if q.isempty():
            print('error')
        else:
            print(q.front())
            q.dequeue()
    elif emr=='size':
        print(q.size())
    else:
        emr,eded=emr.split()
        q.enqueue(eded)
        print('ok')
