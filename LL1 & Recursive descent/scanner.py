import sys
import string


a = sys.stdin.read()

words = a.split()

keyword = ["if", "then", "begin", "end", "procedure", "function"]
operator = ["/", "*", "-", "+"]
alphabet = []
for i in range(ord('a'), ord('z')+1):
    alphabet.append(chr(i))
number = []
for i in range(1, 10):
    number.append(str(i))
ans = []
symbolt = []
for word in words:
    check = 1
    check2 = 1
    if word in keyword:
        ans.append("<keyword,"+word+"> ")
    elif word in operator:
        ans.append("<operator,"+word+"> ")
    else:
        if word[0] in alphabet:
            for i in word[1:]:
                if i not in alphabet and i not in number:
                    check = 0
            if check == 1:
                ans.append("<ID,"+word+"> ")
                symbolt.append(word)
            else:
                ans.append("<Invalid,"+word+"> ")
        elif word[0] in number:
            for i in word[1:]:
                if i not in number and i == ".":
                    for ii in word[word.index(i)+1:]:
                        if ii not in number:
                            check = 0
                    if check == 1:
                        ans.append("<Float,"+word+"> ")
                    else:
                        ans.append("<Invalid," + word + "> ")
                    check2 = 0
                    break
                elif i not in number:
                    check = 0
            if check == 1 and check2:
                ans.append("<Int," + word + "> ")
            elif check2:
                ans.append("<Invalid," + word + "> ")

print(ans)

F = open("output.txt", "w")
S = open("symboltable.txt" , "w")
for item in ans:
    F.write("%s " % item)
for item in symbolt:
    S.write("%s\n" % item)

# abc 123 adf435 + - /
# gfgg 894375 yyyy y77%uu 7,  4398.3 43.5.5 43a. 44.1a 55.6