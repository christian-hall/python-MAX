# Chapter 4, Control Statements

# python doesn't have a switch statement
# simple for loop, range is exclusive, the extra number is an incrementer so you don't have
# to just do 1. You cannot count by non-integers

# count to 10
for i in range(1, 11):
    print('i: ', i)

# count 0 to 30 by 3's
for i in range(0, 31, 3):
    print('i: ', i)

# count 0 to 5 by 0.05
for f in range(.3, .5, .05):
    print('f:', f)