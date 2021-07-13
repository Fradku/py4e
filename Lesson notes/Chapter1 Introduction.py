
# Convert floor in EU to floor in the US
inp = input('Europe floor?')
# The value typed is the input and saved as "inp", the input is treated as STRING, NOT INTEGER

# Convert floor in EU to floor in the US
usf = int(inp) + 1
print('US floor', usf)

#OPERATORS
# ** exponentiation
# for division: / gives value in float, // gives value in integer
width = 17
height = 12.0
print(width//2)
print(width/2)


# Summary
# Type, Reserved Words, Variables, Operators, Operator precedence
# Integer Division, Conversion between types, User input, Comments(#)

# Calculate wage
hours = input('Enter hours: ')
rate = input('Enter rate: ')
Pay = float(hours) * float(rate)
print("Pay: ", (Pay))

# Program to convert fahrenheit to celsius
tempf = input('Temperature in F: ')
tempc = ((float(tempf) - 32) * 5 ) /9
print("Temperature in C= ", (tempc))
