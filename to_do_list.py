
while True:
    user_input = input('do you want to add a new To-Do item?')
    if user_input.casefold() == 'exit':
        print('thank you for using the To-Do program, come back again soon"')
        break
    if user_input.casefold() == 'y':
        input_into_to_do = input('Type in new To-Do item: ')
        file = open('To_do.txt', 'a').write(f'\n{input_into_to_do}')

    else:
        if input('do you want to list your To-Do items ?').casefold() == 'y':
            file = open('To_do.txt', 'r').read()
            print(f'\n{file}')
        






