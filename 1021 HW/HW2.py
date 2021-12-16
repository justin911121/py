temp = input('請輸入溫度:　')
temp_num0 = int(temp[0])
temp_num1 = int(temp[1])
temp_total = temp_num0*10 + temp_num1

if temp[2] == 'c' or temp[2] == 'C' :
    ans = (float)(temp_total*(9/5)+32)
    print('轉換後溫度為華氏%.2f度'%ans)
elif temp[2] == 'f' or temp[2] == 'F' :
    ans = (float)((temp_total-32)*5/9)
    print('轉換後溫度為華氏%.2f度'%ans)
