# Chapter 5 - functions and exceptions

# keyword 'def' defines a function
def print_something():
    print('something')


# you can assign default values to arguments being passed
def sum(x, y=0):
    return x + y


# call the function below the method
print_something()
print(sum(5, 9))
print(sum(2))


# variable arguments (*args)
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print('sum function:', add(1, 2, 3, 4))
print('sum function:', add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# keyword arguments (**kwargs) - allows you to pass in arguments in other orders
def print_stuff(name, age, gender):
    print(f'{name}, {age}, {gender}')


print_stuff('Allison', 24, 'female')
print_stuff(age=26, gender='male', name='Christian')

# Access modifiers - more of an afterthought in python
# Public - the default setting (no explicit public keyword)
# Protected - available to that current class and any subclasses, '_'
# Private - available to current class only '__'

# Exceptions - used like Java, syntax is different

