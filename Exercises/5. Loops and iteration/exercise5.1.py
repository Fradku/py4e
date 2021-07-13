

number = 0
tot = 0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    print(fval)
    number = number + 1
    tot = tot + fval

print(tot, number, tot / number)

