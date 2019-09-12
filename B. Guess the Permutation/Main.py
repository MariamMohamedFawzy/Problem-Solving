


def getTheNumOfCol(arr, x):
    n = len(arr)
    for i in range(n):
        found = True
        found_num = False
        for j in range(n):
            if arr[i][j] > x:
                found = False
                break
            if arr[i][j] == x:
                found_num = True
        if found and found_num:
            return i + 1
    return -1






def CallMyFunc():
    n = input()
    arr = [[0 for x in range(n)]for i in range(n) ]
    all_nums = set()

    for i in range(n):
        arr[i] = map(int, raw_input().split())

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            all_nums.add(arr[i][j])
    min_num = min(all_nums) - 1
    res = [min_num] * n

    for i in range(len(all_nums)):
        curr = getTheNumOfCol(arr, i + 1)
        res[curr - 1] = i + 1

    for i in range(n):
        if res[i] == min_num:
            res[i] = max(all_nums) + 1
            break

    str_res = ""
    for i in range(n):
        str_res += str(res[i]) + " "
    print str_res[0: len(str_res) - 1]



if __name__ == '__main__':
    CallMyFunc()
