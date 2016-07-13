from fractions import Fraction

a = Fraction(input('Enter first fraction : '))
b = Fraction(input('Enter second fraction : '))
op = input('Operation to perform - [A]dd, [S]ubtract, [D]ivide, [M]ultiply : ')

cmd = op.lower()[0]

if cmd == 'a':
    print(a, '+', b, '=', a + b)
elif cmd == 's':
    print(a, '-', b, '=', a - b)
elif cmd == 'd':
    print(a, '/', b, '=', a / b)
elif cmd == 'm':
    print(a, '*', b, '=', a * b)
else:
    print('Invalid Operation')