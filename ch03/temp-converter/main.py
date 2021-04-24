print('Welcome to the temperature convertyer')
print()
leave = 'n'
while leave.lower() != 'y':
    fahrenheit = float(input('Enter degrees in Fahrenheit: '))
    celsius = (fahrenheit - 32) * (5 / 9)
    print('Degrees in Celsius: ', round(celsius, 2))
    print()
    leave = input('Quit? (y/n): ')
    print()

print('Goodbye')