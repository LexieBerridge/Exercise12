tup = 'hello' # raw string and no comma, this is not recognised as a tuple its the comma that makes the tuple
print(len(tup)) # so this prints 5 as its the length of the string
tup = 'hello', # comma used now recognised as tuple
print(len(tup))  # as such this prints 1 as there is one item in the tuple
