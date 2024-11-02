n = int(input('Enter number: '))
sum = 0
temp = n
while (temp > 0):
    a = temp % 10
    sum = sum + (a*a*a)
    temp = temp / 10
print(sum)
#if n == sum:
 #   print('Armstrong number')
#else:
 #   print('Not an armstrong')