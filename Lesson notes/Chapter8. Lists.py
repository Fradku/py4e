# List is contained in square brackets

friends = ['John', 'Jenny', 'Jane']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# Looking inside Lists
friends = ['John', 'Jenny', 'Jane']
print(friends[2])

# Lists are Mutable, or can be changed; Strings are non-mutable
lotto = [2,14,23,41]
print(lotto)
lotto[2] = 1        # Index starts with zero
print(lotto)

print(len(lotto))   # len of list gives the number of data

# Range function
friends = ['John', 'Jenny', 'Jane']
for i in range(len(friends)):
    friend = friends[i]
    print('Hello,', friend)

# Concatenating lists using +
a = [1,2,3]
b= [1,2,3]
c = a + b
print(c)

# Lists can be sliced using :
t = [1,2,3,4,5]
print(t[:4])
print(t[1:2])

x = list()
print(type(x))
print(dir(x))

# Creating an empty list
stuff = list()
stuff.append(99)        # .append adds stuff into a list
stuff.append('Book')
print(stuff)

print(9 in stuff)

# Sorting a list
friends = ['Adam', 'Jenny', 'Ben']
friends.sort()  # Items are sorted in ascending order(number), alphabetical(strings)
print(friends)

# Finding average using list
numlist = list()
while True:
    inp = input('Enter a number:')
    if inp =='done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print(average)

# Strings and Lists
abc = ' With three words'
stuff = abc.split()  # The parameter is where the string will be broken, in this case, empty spaces
print(stuff)
print(len(stuff))

# Double split