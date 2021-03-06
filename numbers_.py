# 1. To check if number starts and ends with same digit
while True:
    number = input('Enter a number: ')
    if number.isdigit():
        print('Number has same first and last digit') if number[0] == number[-1] else print(
            'Number does not have same first and last digit')
    else:
        print('Seems that the entered number is not an integer!')
    if input('Continue (Y/N)? ').lower() == 'n':
        break
