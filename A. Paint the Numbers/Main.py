
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def run():
    n = eval(input())
    nums = list(map(int, input().split()))

    # list_primes = []
    # for i in nums:
    #     if isPrime(i):
    #         list_primes.append(i)

    # list_primes = list(set(list_primes))
    # remaining = []
    # for i in nums:
    #     remain = True
    #     for j in list_primes:
    #         if i % j == 0:
    #             remain = False
    #     if remain:
    #         remaining.append(i)
    # c = len(list_primes)
    c = 0
    remaining = nums
    # print(c, remaining, list_primes)
    while True and len(remaining) > 0:
        mn = min(remaining)
        remaining2 = []
        for i in remaining:
            if i % mn != 0: 
                remaining2.append(i)
        c += 1
        if len(remaining2) > 0:
            remaining = remaining2
        else:
            break

    print(c)

if __name__ == '__main__':
    run()
