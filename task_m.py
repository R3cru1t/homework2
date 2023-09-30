stack = []
while True:
    command = input().strip()
    if command.startswith('push_front'):
        number = int(command.split()[1])
        stack.insert(0, number)
        print('ok')
    if command.startswith('push_back'):
        number = int(command.split()[1])
        stack.append(number)
        print('ok')
    elif command == 'pop_front':
        print(stack.pop(0))
    elif command == 'pop_back':
        print(stack.pop(-1))
    elif command == 'back':
        print(stack[-1])
    elif command == 'size':
        print(len(stack))
    elif command == 'clear':
        stack.clear()
        print('ok')
    elif command == 'exit':
        print('bye')
        break
    else:
        if command != 'push_front':
            print('error')