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

