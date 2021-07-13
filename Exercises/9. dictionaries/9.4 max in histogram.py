
fhand = input('Enter file name:')
fhand = open(fhand)
#fhand = open('mbox-short.txt')
mails = dict()
for lines in fhand:
    words = lines.split()
    if len(words) < 3 or words[0] != 'From': continue
    else:
        mails[words[1]] = mails.get(words[1], 0) + 1

maxcount = None
maxword = None
for word,count in mails.items():
    if maxcount is None or maxcount < count:
        maxcount = count
        maxword = word

print(maxword, maxcount)