import random
ans = random.randint(1,100)

for i in range(6):
    if i == 5:
        print('你沒猜中!謎底為:%d'%ans)
        break
    n = input('請輸入一個1到100的數字:')
    n = int(n)
    times = 4-i
    if n == ans:
        print('恭喜你猜對了!謎底就是%d'%ans)
        break
    elif n > ans:
        print('猜大了，請再猜!還有%d次機會'%times)
    elif n < ans:
        print('猜小了，請再猜!還有%d次機會'%times)


