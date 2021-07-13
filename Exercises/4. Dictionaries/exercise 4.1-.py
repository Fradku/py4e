


def computepay(hours, rate):
    if hours > 40:
        print('Overtime')
        rp = 40 * rate
        opt = (hours - 40) * 1.5 * rate
        pay = rp + opt
    else:
        print('Regular')
        pay = hours * rate
    print('Returning',pay)
    return pay

hours = input("Enter Hours:")
hours = float(hours)
rate = float(input("Enter Hourly Rate: "))

pay = computepay(hours, rate)
print(pay)


