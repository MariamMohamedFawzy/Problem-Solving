import math

def handle_case(heads, blows):
    ds = list(map(lambda x: x[0], blows))
    hs = list(map(lambda x: x[1], blows))

    diffs = [ds[i] - hs[i] for i in range(len(ds))]

    max_diff = max(diffs)

    max_d = max(ds)

    if max_diff <= 0 and heads > max_d:
        c = -1
    else:
        heads = heads - max_d
        c= 1
        if heads > 0:
            c += math.ceil(heads / max_diff)
    
    print(c)


    

def run():
    queries = eval(input())
    total_heads = []
    total_blows = []
    for _ in range(queries):
        n, heads = list(map(int, input().split()))
        total_heads.append(heads)
        blows = []
        for _ in range(n):
            d, h = list(map(int, input().split()))
            blows.append((d, h))
        total_blows.append(blows)
    for i in range(len(total_blows)):
        handle_case(total_heads[i], total_blows[i])



if __name__ == "__main__":
    run()