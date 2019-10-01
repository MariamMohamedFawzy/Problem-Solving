

def run():
    n, k = list(map(int, input().split()))
    ids = list(map(int, input().split()))
    
    screen = []
    for i in range(n):
        if ids[i] in screen:
            continue
        else:
            screen.insert(0, ids[i])
            if len(screen) > k:
                screen = screen[:k]

    print(len(screen))
    print(' '.join(list(map(str, screen))))

if __name__ == '__main__':
    run()