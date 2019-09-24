a = float(input())
x = str(input())
b = float(input())
if x == '+':
    print(a + b)
elif x == '-':
    print(a - b)
elif (x == '/') and (b != 0):
    print(a / b)
elif (x == '/') and (b == 0):
    print('Деление на 0!')
elif x == '*':
    print(a * b)
elif (x == 'mod') and (b != 0):
    print(a % b)
elif (x == 'mod') and (b == 0):
    print('Деление на 0!')
elif x == 'pow':
    print(a ** b)
elif (x == 'div') and (b != 0):
    print(a // b)
elif (x == 'div') and (b == 0):
    print('Деление на 0!')
