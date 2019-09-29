

def run():
    l, r = list(map(int, input().split()))
    if r < l:
        print('-1')
        return
    
    x = l
    while x <= r:
        if len(list(str(x))) == len(set(str(x))):
            print(x)
            return
        x += 1
    
    print('-1')




if __name__ == '__main__':
    run()
