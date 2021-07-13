# Exercise  9.1: Write a program that reads the words in words.txt and stores
# them as keys in a dictionary. Download a copy of the file from
# https://www.py4e.com/code3/words.txt. It doesn't matter what the values are.
# Then use the 'in' operator as a fast way to check whether a string is in the dictionary.

my_dict = dict()
fhand = open('words.txt')
for lines in fhand:
    words = lines.strip()
    for word in words:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] = my_dict[word] + 1

print('Python' in my_dict)



count = 0
words = dict()
fhand = open('words.txt')
for lines in fhand:
    words = lines.split()
    for word in words:
        count = count + 1
        if word in words:
            continue
        words[word] = count

print(count)
if 'Python' in  words:
    print('True')
else:
    print('False')