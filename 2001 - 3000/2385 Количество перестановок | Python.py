n=int(input())
def fak(n):
    if n==1:
        return 1
    return fak (n-1)*n
print (fak(n))
