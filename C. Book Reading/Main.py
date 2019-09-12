
def get_till_10(m):
    out =  [(m * i)%10 for i  in range(1, 11)]
    return sum(out), out


def handle_case(n, m):
    if n < m:
        print(0)
        return

    k = n // (m*10)
    # print(k)
    sum_till_10, arr_till_10 = get_till_10(m)
    # print(sum_till_10)
    remain = (n - k * m * 10) // m
    # print(remain)
    out = sum_till_10 * k + sum(arr_till_10[:remain])

    print(out)
    


def run():
    num_queries = eval(input())
    queries = []
    for _ in range(num_queries):
        queries.append(list(map(int, input().split())))

    for query in queries:
        n, m = query
        handle_case(n, m)

if __name__ == "__main__":
    run()