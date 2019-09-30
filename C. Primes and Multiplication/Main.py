
# gs = dict()
# ps = dict()


def prime(n):
    # global ps
    i = 2
    factors = []
    flag = False
    while i * i <= n:
        # if n in ps:
        #     factors.extend(ps[n])
        #     flag = True
        #     break
        if n % i:
            i += 1
        else:
            factors.append(i)
            while n % i == 0:
                n //= i
            
    if n > 1:
        factors.append(n)
    # ps[n] = list(set(factors))
    return factors


# def g(x, p):
#     c = 0
#     while x >= p and x > 0:
#         if x // p == x / p:
#             c += 1
#             x = x / p
#         else:
#             break
#     return p ** c


# def f(x, y):
#     global gs
#     prime_factors = set(prime(x))

#     c = 1
#     for prime_factor in prime_factors:
#         if y in gs and prime_factor in gs[y]:
#             current_g = gs[y][prime_factor]
#         else:
#             current_g = g(y, prime_factor)
#             if y in gs:
#                 gs[y][prime_factor] = current_g
#             else:
#                 gs[y] = dict()
#                 gs[y][prime_factor] = current_g
#         c *= current_g

#     return c



# def run2():

#     x, n = list(map(int, input().split()))
    
#     c = 1
#     for i in range(1, n+1):
#         # print('f({0}, {1}) = {2}'.format(x, i, f(x, i)))
#         c *= f(x, i)

#     c = c % (10**9 + 7)
#     print(c)


def get_h(n, p, result):

    if n > 0:
        return get_h(n//p, p, result + n//p)
    
    return result




def run():
    x, n = list(map(int, input().split()))

    prime_factors = prime(x)

    c = 1
    mod_val = 10**9 + 7
    for p in prime_factors:
        h = get_h(n, p, 0)
        c *= pow(p, h, mod_val)
        
        
    c = c % mod_val
    print(c)

if __name__ == '__main__':
    run()
    # run2()