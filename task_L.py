# задачи K нету потому-что я ее забыл отрельно сохранить, это та-же но с защитой от ошибок
stack = []
check = 0
while True:
    command = input().strip()
    if command.startswith('push'):
        number = int(command.split()[1])
        stack.append(number)
        check = 1
        print('ok')
    elif command == 'front':
        if check == 1:
            print(stack[0])
        else:
            print("error")
    elif command == 'pop':
        if check == 1:
            print(stack.pop(0))
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
    else:
        print('error')