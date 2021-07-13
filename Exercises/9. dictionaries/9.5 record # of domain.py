fhand = open('mbox-short.txt')

schoolcount = dict()
for lines in fhand:
    words = lines.split()
    if len(words) < 2 or words[0] != 'From': continue
    else:
        atpos = words[1].find('@')
        domain = words[1][atpos + 1:]
        schoolcount[domain] = schoolcount.get(domain, 0) + 1

print(schoolcount)