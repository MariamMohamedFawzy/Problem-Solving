

def run():
    n = eval(input())
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))

    values_up = [0] * n
    values_down = [0] * n

    values_up[-1] = up[-1]
    values_down[-1] = down[-1]

    max_up = up[-1]
    max_down = down[-1]
    for i in range(n-2, -1, -1):
        values_up[i] = up[i] + max_down
        values_down[i] = down[i] + max_up

        if max_up < values_up[i]:
            max_up = values_up[i]

        if max_down < values_down[i]:
            max_down = values_down[i]

    print(max(max_up, max_down))



if __name__ == '__main__':
    run()
