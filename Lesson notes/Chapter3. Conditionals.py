# Conditional execution
# "If" statement
# <, >, less than more than
# <=,>==, less than or equal to; more than or equal to
# ==, equal to
# !=, not equal to

x = input("Number? ")
if float(x) == 5:
    print('equals 5')
    print('is still 5')
if float(x) > 5:
    print('more than 5')
if float(x) < 5:
    print('less than 5')

# Two-way decisions, 'If' 'then'
y = 1
if y > 2:
    print('Larger')
else:
    print('Smaller')
print('Done')

# Multi-way branches
# 'elif'
z = float(input('Number: '))
if z < 2:
    print('small')
elif z < 10:
    print('medium')
else:
    print('large')
print('All Done')

# Try/ except structure
# Take a code that might "blow up" then protecting it, ensuring whole program is executed rather than stopping

astr = "hello bob"
try:
    istr = int(astr)
except:
    istr = -1
# Except block is only triggered when the code does not work

print('First', istr)

# try except is useful when a program requires user to key in information
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("Nice work")
else:
    print("Not a number")