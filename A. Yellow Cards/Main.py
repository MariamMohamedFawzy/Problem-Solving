

def run():
    a1 = eval(input())
    a2 = eval(input())
    k1 = eval(input())
    k2 = eval(input())
    n = eval(input())
   
    mx_k = max(k1, k2)
    mn_k = min(k1, k2)
    if k1 == mx_k:
        mn_a = a2
        mx_a = a1
    else:
        mn_a = a1
        mx_a = a2
    
    c1 = min(mn_a, n // mn_k)
    remain_n = n - c1 * mn_k
    if remain_n >= 0:
        c1 += min(mx_a, remain_n//mx_k)

    c1 = min(c1, a1 + a2)

    if mx_k > 1:
        c2 = n // (mx_k-1)
        if c2 >= mx_a:
            c2 = mx_a
        else: 
            c2 = 0
            print(c2, c1)
            return
    else: c2 = 0


    remain_n = n - c2 * (mx_k-1)
    if remain_n >= 0 and mn_k>1:
        c2_2 = remain_n//(mn_k-1)
        if c2_2 >= mn_a:
            c2_2 = mn_a
        else:
            c2_2 = 0
            c2 = 0 
            print(c2, c1)
            return
    else: c2_2 = 0


    c2 = n - c2 * (mx_k-1) - c2_2 * (mn_k-1)

    if c2 < 0:
        c2 = 0
    c2 = min(c2, a1 + a2)

    print(c2, c1)


if __name__ == '__main__':
    run()
