cheese = ['cheddar', 'stilton', 'cornish yag']
cheese += 'oke' # this splits the string into emelements and adds them to the list
print(cheese)
cheese.append('oke')
print(cheese)
cheese[:0] = 'oke', 'bree'
print(cheese)