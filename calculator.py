def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("This number can not be divided by 0.")
    else:
        return x / y


def calculator():
    while True:
        print('\n Simple Calculator.')
        print('Select the operation needed')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Exit')

        choice = input('Please enter the operation you want: ')

        if choice == '5':
            print('Thank you for using the calculator.')
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input('Please enter the first number: '))
                num2 = float(input('Please enter the second number: '))

                if choice == '1':
                    print(f'{num1} + {num2} = {add(num1, num2)}')

                elif choice == '2':
                    print(f'{num1} + {num2} = {subtract(num1, num2)}')

                elif choice == '3':
                    print(f'{num1} * {num2} = {multiply(num1, num2)}')

                elif choice == '4':
                    print(f'{num1} / {num2} = {divide(num1, num2)}')

            except ValueError:
                print('Please enter NUMBERS only!!')

        else:
            print('Please a number between 1 and 5 only.')

if __name__ == "__main__":
    calculator()
