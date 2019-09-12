
import math


def CallMyFunc():
    data = map(int, raw_input().split())
    n = data[0]
    m = data[1]
    arr = [[0 for i in range(m)]for j in range(n)]


    arr_min = [0] * n
    for i in range(n):
        arr[i] = map(int, raw_input().split())
        arr_min[i] = min(arr[i])

    print(max(arr_min))
    # max_min = -1
    # index_of_max_min = -1
    # for i in range(n):
    #     if arr_min[i] > max_min:
    #         max_min = arr_min[i]
    #         index_of_max_min = i
    # print max_min


if __name__ == '__main__':
    CallMyFunc()
