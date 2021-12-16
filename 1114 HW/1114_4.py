import random

number = []
for i in range(10):
    n = random.randint(0,9)
    number.append(n)

print('1. 目前的List：\n[',end='')
for i in range(10):
    if i == 9:
        print('%d]'%number[9])
    else:
        print('%d,'%number[i],end='')

print('2. List內所有的數值加1：\n[',end='')
for i in range(10):
    number[i]+=1
    if i == 9:
        print('%d]'%number[9])
    else:
        print('%d,'%number[i],end='')

print('3. List由大到小：\n[',end='')
number.sort(reverse = True)
for i in range(10):
    if i == 9:
        print('%d]'%number[9])
    else:
        print('%d,'%number[i],end='')

print('4. List由小到大：\n[',end='')
number.sort()
for i in range(10):
    if i == 9:
        print('%d]'%number[9])
    else:
        print('%d,'%number[i],end='')

print('5. List 偶數在前，奇數在後\n[',end='')
new_lst = []
for k in range(10):
    if number[k] % 2 == 0:
        new_lst.append(number[k])
for k in range(10):
    if number[k] % 2 != 0:
        new_lst.append(number[k])

for i in range(10):
    if i == 9:
        print('%d]'%new_lst[9])
    else:
        print('%d,'%new_lst[i],end='')
