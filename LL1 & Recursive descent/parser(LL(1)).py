import time


w = 'string'

i = 0

terminals = ['a', 'b', 'c', 'd', 'e', 'f', 'g' , '$']

rules = ['', 'ACSDE', 'f', 'aA', 'B', 'bB', '', 'cC', 'd', 'dD', 'Be', 'gE', '']

pt = {'S': {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'f': 2}, 'A': {'a': 3, 'b': 4, 'c': 4, 'd': 4},
      'B': {'b': 5, 'c': 6, 'd': 6, 'e': 6}, 'C': {'c': 7, 'd': 8}, 'D': {'b': 10, 'd': 9, 'e': 10},
      'E': {'b': 12, 'd': 12, 'e': 12, 'g': 11, '$': 12}}
stack = '$S'

w = input("enter w\n")
w = str(w + '$')
start_time = time.time()
while 1:
    if stack == '$' and w.__len__() - 1 == i:
        break;
    if stack[-1] == w[i]:
        i += 1
        stack = stack[0:-1]
        continue
    elif stack[-1] in terminals:
        print("error")
        exit(1)
    else:
        try:
            t = rules[pt[stack[-1]][w[i]]][::-1]
            stack = stack[0:-1]
            stack += t
        except:
            print("error")
            exit(1)

print("--- %s seconds ---" % (time.time() - start_time))
print("accept")
exit(0)

#aaaabbbcccdabcdfdbegddbbegg