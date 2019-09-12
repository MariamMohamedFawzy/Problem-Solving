

def run():
    n, k = map(int, input().split())
    s = input()
    s_sorted = sorted(set(s))
    big = s_sorted[-1]
    small = s_sorted[0]
    if k > n:
        t = s + ''.join([small] * (k - n))
    else:
        if len(s) == 1:
            t = s
        else:

            to_replace = big
            ind_replace = 0
            for i in range(k-1, -1, -1):
                if s[i] == big:
                    continue
                else:
                    to_replace = s[i]
                    ind_replace = i
                    break

            ind = s_sorted.index(to_replace)
            ind += 1


            t = s[:ind_replace] + s_sorted[ind] + ''.join([small]*(k - ind_replace - 1))


    print(t)



if __name__ == '__main__':
    run()
