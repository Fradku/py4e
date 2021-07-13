
# Each chracter is a string has separate index, starting from 0

fruit = 'Banana'
letter = fruit[1]
print(letter)

# Function len gives us the length of string
print(len(fruit))

fruit = 'Banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1

    print(count)

# Slicing strings: pulling chunks of a string
# The square bracket, is up to but not including
s = 'Monty Python'
print(s[0:4])
print(s[6:20])


greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(type(greet))


# Searching string, find() function
fruit = "banana"
pos = fruit.find('na')
print(pos)

# Convert everything to upper case
print('wewew'.upper())

# Search and replace, old, new
greet = "Hello Bob"
nstr = greet.replace('Bob','Jane')
print(nstr)

# Remove spaces, lstrip() and rstrip() for space at the left or right, strip() for both sides
greet = '     Hello Bob'
print(greet)
print(greet.lstrip())

data = 'From stephen.marquard@uct.ac.za Sat Jan 5  09:14:15 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1: sppos]
print(host)