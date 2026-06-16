print('Welcome to calculator ^_^')
try :
    a = int(input('Enter 1st number'))
    b = int(input('Enter 2nd number'))
except:
    print('Only numbers allowed')
    exit()
op = input('Enter the operation you want to perform:')

if b == 0 and op == '/' :
    print('Divison with zero is not possible')
else:
    if op == '+' :
        print(f'{a} + {b} = {a + b}')
    elif op == '-' :
        print(f'{a} - {b} = {a - b}')
    elif op == '*' :
        print(f'{a} * {b} = {a * b}')
    elif op == '/' :
        print(f'{a} / {b} = {a / b}')