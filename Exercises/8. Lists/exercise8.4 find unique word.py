fhand = input('Enter file name: ')
fh = open(fhand)
# fh = open('romeo.txt')

list = []

for line in fh:
    # print(line.rstrip())
    # print(line.split())
    words = line.split()
    for word in words:
        if word in list:
            continue
        list.append(word)
list.sort()
print(list)
