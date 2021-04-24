print('Welcome to the Area and Perimeter Calculator')
print()
choice = 'n'
while choice.lower() != 'y':
    length = int(input('enter length:\t'))
    width = int(input('enter width:\t'))
    area = length * width
    perimeter = length * 2 + width * 2
    print(f'Area:\t\t{area}')
    print(f'Perimeter:\t{perimeter}')
    print()
    choice = input('Quit? (y/n): ')
    print()

print('Goodbye')
