
# 'while' is similar to 'if', but it allows loops
# The loop is called a 'loop'

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

# 'break' ends a loop, moves onto next block
# 'continue' ends the iteration, go back to the beginning of loop


# Definite loop runs a finite number of times
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')
# i is the iteration


# Loop idioms

# Max. value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 31, 12, 94, 23]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

# Count number of value
zork = 0
print('Before', zork)
for thing in [1, 3, 5, 9]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Sum in a loop
zork = 0
print('Before', zork)
for thing in [1, 3, 5, 9]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Average in a loop
count = 0
sum = 0
print('Before', count, sum)
for thing in [1, 3, 5, 9]:
    count = count + 1
    sum = sum + thing
    print(count, sum, thing)
print('After', count, sum, sum / count)

# Filtering in a loop
for value in [9, 20, 23, 41, 10]:
    if value > 20:
            print('Large number', value)
print('Done')

# Search using Boolean Variable(either TRUE/ FALSE)
found = False
for value in [9, 20, 23, 41, 10]:
    if value == 20:
        found = True
    else:
        found = False
    print(value, found)
print('Done')

# Min. value
# Use None type
smallest= None
print('Before')
for the_num in [9, 31, 12, 94, 1]:
    if smallest is None:
        smallest = the_num
    elif the_num < smallest:
        smallest = the_num
    print(smallest, the_num)
print('After', smallest)

