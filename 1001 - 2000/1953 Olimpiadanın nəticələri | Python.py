def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        L = R = a = 0
        while L < len(left) and R < len(right):
            if left[L][0] >= right[R][0]:
                A[a] = left[L]
                L+=1
            else:
                A[a] = right[R]
                R+=1
            a+=1
        while L < len(left):
            A[a] = left[L]
            a+=1
            L+=1
        while R < len(right):
            A[a] = right[R]
            a+=1
            R+=1
n = int(input())
A=[]
M =[int(i) for i in input().split()]
for i in range(n):
    A.append([0]*2)
for i in range(n):
    A[i][0] = M[i]
    A[i][1] = i+1
merge_sort(A)
for i in range(n):
    print(A[i][1], end=' ')
