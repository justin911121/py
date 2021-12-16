def is_prime(x):
    for i in range(2,x,1):
        counter = 0
        if x % i == 0 :
            print('%d 不是質數 %d 可被 %d 整除'%(x,x,i))
            break
        elif x % i != 0 :
            counter = 1
    if counter == 1:
        print('%d 是質數'%x)

is_prime(101)
is_prime(111)
is_prime(121)
is_prime(131)
is_prime(141)
is_prime(151)
