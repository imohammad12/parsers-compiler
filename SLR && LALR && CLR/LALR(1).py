import time
w = str
w = input()
w += str('$')

LA = 0
rules = [12, ('S`', 1), ('S', 2), ('A', 3), ('A', 0), ('B', 3)]  # 12 is for making rules 1base
stack = ['0']
action = [{'d': ('s', 3), 'a': ('r', 4)},
          {'$': ('accept', 4)},
          {'a': ('s', 6)},
          {'d': ('s', 3), 'a': ('r', 4)},
          {'a': ('s', 5)},
          {'a': ('r', 3), 'b': ('r', 3)},
          {'d': ('s', 3), 'b': ('r', 4)},
          {'$': ('r', 2)},
          {'b': ('s', 9)},
          {'$': ('r', 5)}]

go_to = [{'S': 1, 'A': 2},
        {},
        {'B': 7},
        {'A': 4},
        {},
        {},
        {'A': 8}]
start_time = time.time()
try:
    while(True):
        if action[int(stack[-1])][w[LA]][0] == 'accept':
            print("accept!")
            print("--- %s seconds ---" % (time.time() - start_time))
            exit(0)
        if action[int(stack[-1])][w[LA]][0] == 's':
            stack.append(w[LA])
            stack.append(action[int(stack[-2])][w[LA]][1])
            LA += 1
        elif action[int(stack[-1])][w[LA]][0] == 'r':
            variable = rules[action[int(stack[-1])][w[LA]][1]][0]
            num_ter = rules[action[int(stack[-1])][w[LA]][1]][1]
            for i in range(0, 2*num_ter):
                stack.pop()
            stack.append(variable)
            stack.append(go_to[int(stack[-2])][variable])

except KeyError:
    print("error")
    print("--- %s seconds ---" % (time.time() - start_time))

except IndexError:
    print("error")



    # ddddaaaaadddddaaaaab