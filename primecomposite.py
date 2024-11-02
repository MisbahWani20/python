n = int(input('Enter number: '))
flag = 0
if n > 1:
    for i in range(1, n):
        if (n % 1) == 0:
            flag += 1
            break
if flag==1:
        print('Prime number')
else:
        print('Composite number')