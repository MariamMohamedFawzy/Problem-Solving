def run():
    a = input()
    b = input()
    n, m = list(map(int, a.split()))
    ts = list(map(int, b.split()))
    waiting = [0]
    for i in range(1, n):
        prev = ts[0:i]
        s = sum(prev) + ts[i]
        if s <= m:
            waiting.append(0)
            continue
        prev.sort()
        temp = 0
        while len(prev) >= 0:
            del prev[-1]
            temp += 1
            if sum(prev) + ts[i] <= m:
                break
        waiting.append(temp)
    print(' '.join(list(map(str, waiting))))



if __name__ == "__main__":
    run()