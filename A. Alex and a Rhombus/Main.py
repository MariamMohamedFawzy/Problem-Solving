def run():
    a = eval(input())
    s = 1
    c = 1
    for _ in range(2, a+1):
        s += 4*c
        c += 1
    print(s)

        


if __name__ == "__main__":
    run()