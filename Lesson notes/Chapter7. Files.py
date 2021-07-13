# open() returns a file handle
# handle = open(filename, mode)
# two modes are r(ead) and w(rite)

# new line, \n
stuff = 'Hello\nWorld!'
print(stuff)
print(len(stuff))
# Newline is one character, not two

# Counting lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count +1
print('Line count:', count)

# Reading the whole file
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# Searching through a file
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
# Newline is considered white space

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# Using 'in' to select lines
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

fhand = input('Enter the file name: ')
fhand = open(fhand)
count = 0
#for line in fhand:
#    if line startswith('Subject'):
#        count = count + 1