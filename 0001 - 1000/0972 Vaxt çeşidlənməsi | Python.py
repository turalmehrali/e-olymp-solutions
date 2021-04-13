def partition(A, sol, sag):
    pivot = A[sol][3]
    i = sol+1
    j = sag
    bitdimi = False
    while not bitdimi:
        while i<=j and A[i][3] <= pivot:
                i+=1
        while i<=j and A[j][3] >= pivot:
                j-=1
        if i > j:
            bitdimi = True
        else:
            if(A[i]!=A[j]):A[i], A[j]=A[j], A[i]
    if(A[sol]!=A[j]):A[sol],A[j]=A[j], A[sol]
    return j
def quick_sort(A, sol, sag):
    if sol < sag:
        privot_index = partition(A, sol, sag)
        quick_sort(A, sol, privot_index-1) 
        quick_sort(A, privot_index+1, sag)

n = int(input()) 
A=[]
for i in range(n):
    A.append([int(t) for t in input().split()])
    A[i].extend([A[i][0]*3600+A[i][1]*60+A[i][2]])

quick_sort(A, 0, n-1)

for i in A:
    print(i[0],i[1],i[2])
