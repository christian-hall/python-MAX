print('Welcome to the chapter 5 homework')


def hello_message(name):
    print(f'Welcome to my app, {name}!!')


def how_old_are_you(age):
    print(f'you are {age} years old!')


name = input('What is your name? ')
hello_message(name)
age, age_verification = 0, False
while not age_verification:
    try:
        age = int(input('How old are you? '))
        age_verification = True
        how_old_are_you(age)
    except ValueError:
        print('Enter a valid integer.')
    finally:
        print('Attempt recorded')