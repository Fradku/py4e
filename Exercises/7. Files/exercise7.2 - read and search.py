#file = open('mbox-short.txt')
fhand = input('Enther the file name: ')
try:
    file = open(fhand)
except:
    print("Invalid file name", fhand)
    quit()

count = 0
total = 0

for line in file:
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    pos = line.find('0')
    value = float(line[20:])
#    print(pos)
    count = count + 1
    total = total + value
#print(count, sum)
average = total / count
print('Average spam confidence:',average)





