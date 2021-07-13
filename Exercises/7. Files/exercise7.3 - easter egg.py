
fhand = input('Enther the file name: ')
try:
    file = open(fhand)
except:
    if fhand == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    else:
        print('File cannot be opened:', fhand)
        quit()

number = 0
for line in file:
    if not line.startswith('Subject') : continue
    number = number + 1

final = 'There were {} subjects lines in {}'.format(number, fhand)
print(final)
