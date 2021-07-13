fhand = open('mbox-short.txt')


hours = dict()
for lines in fhand:
    words = lines.split()
    if len(words) < 3 or words[0] != "From": continue
    else:
        hours[words[5][0:2]] = hours.get(words[5][0:2], 0) + 1

hours = sorted(hours.items())
print(hours)

for k,v in hours:
    print(k, v)

