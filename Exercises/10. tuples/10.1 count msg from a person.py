fhand = input('Enter a file name:')
fhand = open(fhand)

mail_count = dict()
for lines in fhand:
    words = lines.split()
    if len(words) < 3 or words[0] != 'From': continue
    else:
        mail_count[words[1]] = mail_count.get(words[1],0) + 1

#print(mail_count)

tmp = list()
for k,v in mail_count.items():
    tmp.append((v,k))

mails = list()
tmp = sorted(tmp, reverse=True)

#print(tmp)

for (v,k) in tmp:
    mails.append((k,v))
#print(mails)
print(mails[0])