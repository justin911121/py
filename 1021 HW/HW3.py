n = input('請輸入正整數')
n = int(n)
for i in range(0,n):
    for a in range(n-i):
        print(' ',end=' ')
    for j in range(i*2+1):
        print('*',end=' ')
    print('\n')    
