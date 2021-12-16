import random

def lotto():  
    for i in range(6):
        #print('%d'%i)
        n = random.randint(1,49)        
        if n not in number:
            number.append(n)
        
        

print('大樂透開獎，中獎號碼：')
number = []
lotto()
special = random.randint(1,49)

print('開出順序:',end='')
for i in range(0,6):
    #print('%d'%i)
    print('%d '%number[i],end='') 
print('特別號: %d'%special)

number.sort()

print('大小順序:',end='')
for i in range(0,6):
    print('%d '%number[i],end='')
print('特別號: %d'%special)
