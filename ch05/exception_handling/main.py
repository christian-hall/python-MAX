print("welcome")

# basic exception handling with inputs
x, valid_x = 0, False
while not valid_x:
    try:
        x = int(input('enter a whole number: '))
        valid_x = True
    except ValueError:
        print('Invalid whole number, try again')
    finally:
        print('finally appears no matter what, can be used to close a connection')
print(x, type(x))

# there is no python try with resources, finally releases the resources 


print("Goodbye")
