

import math

def run():
    n = eval(input())
    vals = []
    for _ in range(n):
        input()
        vals.append(list(map(int, input().split())))

    for arr in vals:
        print(math.ceil(sum(arr) / len(arr)))

if __name__ == '__main__':
    run()