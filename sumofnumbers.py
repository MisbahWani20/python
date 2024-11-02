n = int(input('How many numbers to add: '))
sum = 0
if n < 0:
    print('Enter positive numbers')
else:
    while n > 0:
        sum = sum + n
        n = n - 1
print('Sum of numbers is: ', sum)