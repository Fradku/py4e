# Stored and reused Steps

big = max('Hello world')
print(big)

# We've been using 'built-in functions'
# def function is used to create our own function
def print_lyrics():
    print('Im a lumberjack, and Im okay.')

print_lyrics()

# Argument

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')
greet('es')
greet('fr')

# Return statement is the residual value