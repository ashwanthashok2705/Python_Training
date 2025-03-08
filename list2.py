  N = int(input())
    my_list = []
    for _ in range(N):
        command, *line = input().split()
        if command == 'append':
            my_list.append(int(line[0]))
        elif command == 'remove':
            my_list.remove(int(line[0]))
        elif command == 'insert':
            my_list.insert(int(line[0]), int(line[1]))
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
        elif command == 'print':
            print(my_list)
