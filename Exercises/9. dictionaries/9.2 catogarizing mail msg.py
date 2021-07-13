# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).

days_no = dict()
#fhand = input('Enter a file name: ')
fhand = open('mbox-short.txt')
#open(fhand)


for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in days_no:
            days_no[words[2]] = 1
        else:
            days_no[words[2]] = days_no[words[2]] + 1

print(days_no)

