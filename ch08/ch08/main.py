# chapter 8 - lists and dictionaries

# processing strings
name = 'Christian Neal Hall'
print(name)
# print name length
print(len(name))
# get portions of the name by index and slicing
print('first char:', name[0])
# get first name by where the first space is
idx_1 = name.index(' ')
first_name = name[0:idx_1]
print(first_name)
idx_2 = name.index(' ', idx_1 + 1)
middle_name = name[idx_1+1:idx_2]
print(middle_name)
last_name = name[idx_2 + 1: len(name)]
print(last_name)
# add a space between each character
for character in name:
    print(character, end=' ')
    print()

# processing lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('first letter', letters[0])
print('last letter', letters[-1])

# slicing
print('2nd through 4th letters', letters[1:4])

# replacing an element
letters[4] = 'z'
print(letters)
letters.append('h')
print(letters)

# remove using pop and pop
letters.pop(-1)
print(letters)
letters.remove('z')
print(letters)
letters.insert(4, 'e')
print(letters)

# for ____ in ____
for letter in letters:
    print(letter, end=" ")
print()

# count function
letters = ['a', 'b', 'a', 'd', 'd', 'f', 'g']
print(letters)
print('number of As:', letters.count('a'))

# range
print('range:', range(1, 10))
print('range 0 list:', list(range(1, 10)))

# for using index
for i in range(0, len(letters)):
    print(f'letter {i}: {letters[i]}')

# does our letters list contain 'c'?
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
if 'b' in letters:
    print('B has been found')

# use * in a string
str1 = 'a' * 10
print(str1)

letters = letters * 2
print(letters)

# a tuple is an immutable list, uses ( ) instead of [ ]

# dictionaries (key-value pairs). You don't have to keep types consistent. 1 : 'one'
spanish_english = {
    'uno' : 'one',
    'dos' : 'two',
    'tres' : 'three'
}
print(spanish_english)
# get value by key
print(spanish_english['dos'])
print(spanish_english.get('uno'))

# add an element to the dictionary
spanish_english['quarto'] = 'four'
print(spanish_english)

# change an element
# spanish_english[1] = 1111
# print(spanish_english)

# iterate through the dictionary
for key in spanish_english:
    print(key)

# values
for value in spanish_english.values():
    print(value)

# key:value paris
for k, v, in spanish_english.items():
    print(f'key {k} : value {v}')

# does a key exist?
if 'uno' in spanish_english:
    print('uno was found')
if 'dos' in spanish_english:
    print('dos is in there')
if 'cinco' in spanish_english:
    print('yeah right')
else:
    print('cinco doesnt exist')

# pop, popitem
print('popitem', spanish_english.popitem())
print('pop(1)', spanish_english.pop('dos'))
