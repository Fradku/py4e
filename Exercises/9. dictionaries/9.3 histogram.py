
fhand = input('Enter file name:')
fhand = open(fhand)

mails = dict()
for lines in fhand:
    words = lines.split()
    if len(words) < 3 or words[0] != 'From': continue
    else:
        if words[1] not in mails:
            mails[words[1]] = 1
        else:
            mails[words[1]] += 1
print(mails)

