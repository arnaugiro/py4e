largest = None
smallest = None
while True:
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        inp = int(num)
    except:
        print ('Invalid input')
        continue
    if largest is None or largest < inp:
        largest = inp
    if smallest is None or smallest > inp:
        smallest = inp
print('Maximum is', largest)
print ('Minimum is', smallest)
