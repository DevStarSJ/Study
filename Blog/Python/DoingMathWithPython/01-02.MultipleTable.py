try:
    val = int(input('Enter start number :'))
    num = int(input('Enter number of step :'))
except:
    print('Invalid number entered')

for i in range(1, num + 1):
    print(val, '*', i, '=', val * i)