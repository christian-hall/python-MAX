# Chapter 9 - file processing

# read in the file and print
# read method returns content as one string
with open('hobbies.txt') as file:
    contents = file.read()
print(contents)

# read a line using readline()
with open('hobbies.txt') as file:
    line = file.readline()
print('line: ', line)

# readlines returns a list of all lines
print('print all lines)')
with open('hobbies.txt') as file:
    lines = file.readlines()
print('line: ', lines)

# write to a file from a list
family = ['Christian', 'Allison', 'Leslie', 'Planty']
handle = open('family.txt', 'w')
# a is append
for member in family:
    handle.write(member + '\n')
handle.close()
print('family file written')

