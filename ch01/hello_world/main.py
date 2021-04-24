print('Hello World')

# code completion and syntax error detection
# This is a comment
# There are no multi-line comments

# statements don't end in ;
a = 5
# add a backslash at the end of a line for a line break, to continue the line on the next line
result = 4 + 6 + 7 \
    + 8 + 9
print(result)

# you can print data types of objects
print(type(result))
# print always gives a new line at the end)

# end attribute allows you to combine two lines
print('hello', end=' ')
print('world')

# separator
print('a', 'b', 'c', 'd', sep='-')

# formatted print, you must cast types as the same type
days_in_week = 7
print('there are ' + str(days_in_week) + ' days in a week')
print(f'There are {days_in_week} days in a week')
