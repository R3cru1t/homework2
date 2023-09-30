# я добавил пару своих функций от скуки
stack = []
check = 0
while True:
    command = input().strip()
    if command.startswith('push_front'):
        number = int(command.split()[1])
        stack.insert(0, number)
        check = 1
        print('Number has been pushed front')
    if command.startswith('push_back'):
        number = int(command.split()[1])
        stack.append(number)
        check = 1
        print('Number has been pushed at the back')
    elif command == 'pop_front':
        if check == 1:
            print(stack.pop(0))
        else:
            print('error')
    elif command == 'pop_back':
        if check == 1:
            print(stack.pop(-1))
        else:
            print('error')
    elif command == 'back':
        if check == 1:
            print(stack[-1])
        else:
            print('error')
    elif command == 'front':
        if check == 1:
            print(stack[0])
        else:
            print("error")
    elif command == 'size':
        print(len(stack))
    elif command == 'clear':
        check = 0
        stack.clear()
        print('ok')
    elif command == 'exit':
        print('bye')
        break
    elif command == 'sort':
        print(*sorted(stack))
    elif command == 'fill':
        from random import randint
        for i in range (5):
            stack.append(randint(1, 1000))
        print("Deck has been filled")
    elif command == 'preview':
        print(*stack)    
    else:
        print('error')