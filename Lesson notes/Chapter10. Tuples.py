# Collection, using round bracket
x = ('Glenn', 'Sally', 'Peter')
print(x)

# Tuples are IMMUTABLE
# Cannot sort, append, reverse
# Tuples are more efficient

t = tuple()
print(dir(t))

(x, y) = (4,'Frad')
print(x)
print(y)

# Tuples are comparable
# If the first item is equal, it goes on to the next element, until it finds elements that differ

# Sorting lists of tuples
d = {'a': 10, 'd':1, 'c':22}

print(d.items())
print(sorted(d.items()))

d = {'a': 10, 'd':1, 'c':22}
t = sorted(d.items())
for k,v in t:
    print(k,v)


# Sort by values instead of key
c = {'a': 10, 'd':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

# OR
c = {'a': 10, 'd':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()])) # List comprehension creates a dynamic list

