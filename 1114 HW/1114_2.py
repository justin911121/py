def tri_pos(r):
    for i in range(1,r+1):
        if i == r:
            for w in range(i*2-1):
                print('*',end = '')
            break
        for j in range(r-i):
            print(' ',end = '')
        for k in range(i*2+1):
            if k == 1 :
                print("*",end = '')
            elif k > 1 and k < i*2-1:
                print(' ',end = '')
            elif k == i*2 and i != 1:
                print("*",end = '')
        print('\n')        

def tri_neg(r):
    for i in range(1,r+1):
        if i == 1:
            for w in range(r*2-1):
                print('*',end = '')
            print('\n')
            continue
        for j in range(i-1):
                print(' ',end = '')
        for k in range((r-i)*2+2):
            if k == 1 :            
                print("*",end = '')
            elif k > 1 and k < (r-i)*2+1:
                print(' ',end = '')
            elif k == (r-i)*2+1 and i != 1:
                print("*",end = '')
        print('\n')        

x = input('請輸入三角型樓層（正整數）: ')
x = int(x)
p = input('正空心三角型（y），倒空心三角型（n）: ')

if p == 'y':
    tri_pos(x)
elif p == 'n':
    tri_neg(x)
