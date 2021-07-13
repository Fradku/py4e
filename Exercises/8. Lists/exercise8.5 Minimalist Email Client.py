fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

# fname = "mbox.txt"
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From:'):
        continue
    list = line.split()
    count = count + 1
    print(list[1])


print("There were", count, "lines in the file with From as the first word")

