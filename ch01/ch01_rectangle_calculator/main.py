print('Welcome to the Area and Perimeter Calculator')
print()
choice = 'n'
while choice.lower() != 'y':
    length, width = int(input('enter length: ')),
    width = int(input('enter width:  '))
    area = length * width
    perimeter = length * 2 + width * 2
    print(f'Area:         {area}')
    print(f'Perimeter:    {perimeter}')
    print()
    choice = input('Quit? (y/n): ')
    print()

print('Goodbye')
