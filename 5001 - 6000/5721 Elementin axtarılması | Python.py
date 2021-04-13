def is_sorted(A):
    for i in range (0, len(A)-1):
        if A[i] > A[i+1]:
            return False
    return True
def merge (a, b):
    i,j = 0,0
    c = [] 
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
             c.append(a[i])
             i+=1
        else:
             c.append(b[j])
             j+=1
    if i != len(a): c.extend(a[i:])
    else:   c.extend(b[j:])
    return c

def merge_sort(A):
    if(len(A)<=1):
        return A
    left, right = merge_sort(A[:len(A)//2]),merge_sort(A[len(A)//2:])
    return merge(left, right)


n, k = map(int, input().split())
A = [int(i) for i in input().split()]
if k>n:
    print(-1)
else:
    if is_sorted(A) == True:
        print (A[-k]) 
    else:
        A = merge_sort(A) 
        print(A[-k])
