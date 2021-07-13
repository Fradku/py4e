

fhand = input('Enter a file name: ')
try:
    fhand = open(fhand)
except:
    print('Invalid File Name', fhand)
    quit()

for lx in fhand:
    fhand = fhand.read()
    print(fhand.upper())

