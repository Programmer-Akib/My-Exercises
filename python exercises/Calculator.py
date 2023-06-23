import time
from functools import reduce
numb = []

def addition():
    number = float(input('Enter Number : '))
    numl = []
    count = 0
    sum = 0
    numl.append(number)
    while number != 0:
        sum += number
        count += 1  # Keeps count of numbers inputed
        number = float(input('Enter more Numbers (type 0 to stop): '))
        numl.append(number)
    print('-------------------------------------------------------------------')
    print(f'The numbers you inputed are: {[num for num in numl if num != 0]}')
    return [sum, count]  # Returns a list. So, we can do list indexing later.

def subtraction():
    numl = []
    number = float(input('Enter Number: '))
    count = 0
    numl.append(number)
    while number != 0:
        number = float(input('Enter more Numbers ("0" to stop): '))
        count += 1
        numl.append(number)
    print('-------------------------------------------------------------------')
    print(f'The numbers you inputed are: {[num for num in numl if num != 0]}')
    difference = reduce(lambda x,y: x-y, numl)
    return [difference,count]

def muliplication():
    numl = []
    number = float(input('Enter Number: '))
    count = 0
    numl.append(number)
    while number != 0:
        number = float(input('Enter more Numbers ("0" to stop): '))
        count += 1
        numl.append(number)
    print('-------------------------------------------------------------------')
    print(f'The numbers you inputed are: {[num for num in numl if num != 0]}')
    for i in numl:
        if i == 0:
            numl.remove(i)
    product = reduce(lambda x, y: x * y, numl)
    print(product)
    return [product, count]

def division():
    numl = []
    number = float(input('Enter Number: '))
    count = 0
    numl.append(number)
    while number != 0:
        number = float(input('Enter more Numbers ("0" to stop): '))
        count += 1
        numl.append(number)
    print('-------------------------------------------------------------------')
    print(f'The numbers you inputed are: {[num for num in numl if num != 0]}')
    for i in numl:
        if i == 0:
            numl.remove(i)
    quotient = reduce(lambda x, y: x / y, numl)
    print(quotient)
    return [quotient, count]

def average():
    number = float(input('Enter Number : '))
    numl = []
    count = 0
    sum = 0
    numl.append(number)
    while number != 0:
        sum += number
        count += 1
        number = float(input('Enter more Numbers (type 0 to stop): '))
        numl.append(number)
    print('-------------------------------------------------------------------')
    print(f'The numbers you inputed are: {[num for num in numl if num != 0]}')
    mean = sum // count
    return [mean, count]

print('[+] to do addition')
print('[-] to do subtraction')
print('[*] to do multiplication')
print('[/] to do division')
print('[avg] to do average')

while True:
    user_inp = input('(+,-,*,/,avg) : ')
    if user_inp == '+':
        result = addition()
        print(f'Result is: {result[0]} , Number of Numbers given are: {result[1]}')
        print('-------------------------------------------------------------------')
    elif user_inp == '-':
        result = subtraction()
        print(f'Result is: {result[0]} , Number of Numbers given are: {result[1]}')
        print('-------------------------------------------------------------------')
    elif user_inp == '*':
        result = muliplication()
        print(f'Result is: {result[0]} , Number of Numbers given are: {result[1]}')
        print('-------------------------------------------------------------------')
    elif user_inp == "/":
        result = division()
        print(f'Result is: {result[0]} , Number of Numbers given are: {result[1]}')
        print('-------------------------------------------------------------------')
    elif user_inp == 'avg':
        result = average()
        print(f'Result is: {result[0]}, Number of Numbers given are: {result[1]}')
        print('-------------------------------------------------------------------')

    time.sleep(1)