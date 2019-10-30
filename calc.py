print('Available operators: '
      '\n "+" division,'
      '\n "-" subtraction,'
      '\n "/" division,'
      '\n "*" multiplying,'
      '\n "mod" division with remainder,'
      '\n "pow" exponentiation '
      '\n "div" for integer division')
a = float(input('Enter your first number '))
x = str(input('Enter operator '))
b = float(input('Enter your second number '))
if x == '+':
    print(a + b)
elif x == '-':
    print(a - b)
elif (x == '/') and (b != 0):
    print(a / b)
elif (x == '/') and (b == 0):
    print('Division by 0!')
elif x == '*':
    print(a * b)
elif (x == 'mod') and (b != 0):
    print(a % b)
elif (x == 'mod') and (b == 0):
    print('Division by 0!')
elif x == 'pow':
    print(a ** b)
elif (x == 'div') and (b != 0):
    print(a // b)
elif (x == 'div') and (b == 0):
    print('Division by  0!')
