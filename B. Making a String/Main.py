


def CallMyFunc():
    n = input()
    data = map(int, raw_input().split())
    data.sort()
    res = 0
    length = len(data)
    last = data[length - 1]
    res += last
    for i in range(1, len(data)):
        current = data[length - 1 - i]
        # if current == last:
        x = min(current, last - 1)
        data[length - 1 - i] = x
        last = x
        if last < 0:
            break
        res += x

    # for i in range(length):
    #     if data[length - 1 - i] < 0:
    #         break
    #     res += data[length - 1 - i]
    print res



if __name__ == '__main__':
    CallMyFunc()
