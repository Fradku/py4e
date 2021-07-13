
grade = input('Enter score: ')

try:
    x = float(grade)
except:
    print('Error, please enter numeric input')
    exit()

if x < 0 or x > 1:
    print('Bad score')
    exit()

if x < 0.6:
    print('F')
elif x >= 0.6 and x <0.7:
    print('D')
elif x>= 0.7 and x<0.8:
    print('C')
elif x>=0.8 and x<0.9:
    print('B')
else:
    print('A')