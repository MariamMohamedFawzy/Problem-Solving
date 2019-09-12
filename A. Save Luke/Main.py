


def CallMyFunc():
    data = map(int, raw_input().split())
    t = (data[1] * 1.0 - data[0] * 1.0) / (data[2] * 1.0 + data[3] * 1.0)
    print t



if __name__ == '__main__':
    CallMyFunc()
