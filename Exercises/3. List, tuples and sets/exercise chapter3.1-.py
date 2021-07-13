

hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Hourly Rate: "))

if h > 40:
    print('Overtime')
    rp = 40 * rate
    opt = (h - 40) * 1.5 * rate
    pay = rp + opt
else:
    print('Regular')
    pay = h * rate

print(pay)