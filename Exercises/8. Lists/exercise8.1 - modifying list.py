# Exercise 1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

letters = ['a','b','c']

def chop(t):
    del t[0]
    del t[-1]

list1 = chop(letters)
print(letters)
print(list1)

numbers = ['1','2','3']
def middle(t):
    new = t[1:]
    del new[-1]
    return new

list2 = middle(numbers)
print(numbers)
print(list2)
