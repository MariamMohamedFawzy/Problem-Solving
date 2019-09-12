
import math


def CallMyFunc():
    a = raw_input()
    b = raw_input()
    index_a = 0
    index_b = 0
    for i in range(len(a)):
        if a[i] == "0":
            index_a += 1
        else:
            break
    for i in range(len(b)):
        if b[i] == "0":
            index_b += 1
        else:
            break
    a = a[index_a: len(a)]
    b = b[index_b: len(b)]
    if len(a) > len(b):
        print ">"
    elif len(b) > len(a):
        print "<"
    else:
        for i in range(len(a)):
            end = i + 5
            if end > len(a):
                end = len(a)
            a_sub = int(a[i: end])
            b_sub = int(b[i: end])
            if a_sub > b_sub:
                print ">"
                return
            elif b_sub > a_sub:
                print "<"
                return
        print "="







if __name__ == '__main__':
    CallMyFunc()
