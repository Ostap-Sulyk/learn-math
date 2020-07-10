import random

operations = ['+', '-', '*', '/']

while True:
    numbers = [random.randint(0, 9), random.randint(0, 9)]
    operator = operations[random.randint(0,3)]
    if operator != '/' and numbers[1] != 0:
        print(f'{numbers[0]} {operator} {numbers[1]}')
        result = float(eval(f'{numbers[0]} {operator} {numbers[1]}'))

        answer = float(input('= '))

        if answer == result:
            print('Correct 😁 !!!')
        elif answer == 'quit':
            break
        else:
            print('Incorect 🙁 try again')
            print('Correct answer is ', result)
    else:
        pass







