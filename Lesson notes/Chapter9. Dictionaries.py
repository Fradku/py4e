# List is a Linear collection
# Dictionary is a Bag of values, each with its own label
#   Values are labelled, they are called keys

purse = dict()
purse['money'] = 12
purse['candy'] = 3
print(purse)
print(purse['candy'])
purse['money'] = purse['money'] + 2
print(purse)

# Dictionaries are like lists but they use keys instead of number to look up values

# Dictionary is created using curly braces, format: 'key' : value
ddd = {'apple':3,'grape':4}
print(ddd)

# Program blows when we try to print a non-existent key
# This can be overcome using the IN operator

counts = dict()
names = ['John','Jeff','Jeff','Pete']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


if name in counts:
    x = counts[name]
else:
    x= 0
# OR
x = counts.get(name, 0)

print('Break')

counts = dict()
names = ['John','Jeff','Jeff','Pete']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


# Count frequencies of words
counts = dict()
line = input('Enter a line of text: ')
words = line.split()

print('Words: ', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0 ) + 1
print('Counts',counts)


# Obtain Keys or/and values from dictionary
jjj = {'Chunk': 1 , 'fred':42, "Jan" : 100}
print(list(jjj))        # get a list of keys
print(jjj.keys())       # get a list of keys
print(jjj.values())     # get a list of values
print(jjj.items())      # get a list of values AND key


# Listing items one by one
jjj = {'Chunk': 1 , 'fred':42, "Jan" : 100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)

