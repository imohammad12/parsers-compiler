import sys
import time

i = 0
w = str
start_time = time.time()
def mach(c):
    global i
    if w[i] == c:
        i += 1
    else:
        print("error")
        exit(1)
def S():
    if w[i] == 'f':
        mach('f')
    else:
        A()
        C()
        S()
        D()
        E()


def A():
    if w[i] == 'a':
        mach('a')
        A()
    else:
        B()

def B():
    if w[i] == 'b':
        mach('b')
        B()
    else:
        return

def C():
    if w[i] == 'c':
        mach('c')
        C()
    elif w[i] == 'd':
        mach('d')
    else:
        print("error")
        exit(1)

def D():
    if w[i] == 'd':
        mach('d')
        D()
    else:
        B()
        mach('e')
def E():
    if w[i] == 'g':
        mach('g')
        E()
    else:
        return


w = input("enter\n")
w = str(w +'$')

S()

print("--- %s seconds ---" % (time.time() - start_time))

if w[i] == '$':
    print("accept")
    exit(0)
else:
    print("error")
    exit(1)


#aaaabbbcccdabcdfdbegddbbegg