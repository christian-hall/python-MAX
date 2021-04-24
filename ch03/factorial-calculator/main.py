print('Welcome to the Factorial Calculator!')
leave = 'n'
while leave.lower() != 'y':
    factorial, response = 1, int(input('Enter an integer greater than 0 and less than 10: '))
    for i in range(1, response + 1):
        factorial *= i
    print(f'The factorial of {response} is {factorial}.')
    print()
    leave = input('Quit? (y/n): ')
    print()

print('Goodbye')
