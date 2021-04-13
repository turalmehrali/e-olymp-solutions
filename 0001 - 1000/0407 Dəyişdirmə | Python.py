t=int(input())
for i in range(0,t):
    k = int(input())
    
    if k % 3 == 1:
        print('VGC')

    elif k % 3 == 2:
        print('CVG')
        
    elif k % 3 == 0:
        print('GCV')
