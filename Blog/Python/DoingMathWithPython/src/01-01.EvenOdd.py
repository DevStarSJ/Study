def is_odd(val):
    if val % 2 == 0:
        return False
    else:
        return True

if __name__ == '__main__':
    try:
        inputNum = float(input('Enter number: '))
    except:
        print('You must input number')
    if inputNum.is_integer():
        val = int(inputNum)
        print(val, 'is','odd' if is_odd(val) else 'even', ':')
        seq = list(range(val, val + 20, 2))
        print(seq)
    else:
        print('You input invalid number')