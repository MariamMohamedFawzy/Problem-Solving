

# def run():
#     n = eval(input())
#     s1 = input()
#     s2 = input()

#     num_diffs = 0
#     diffs = [] # 0, 1-> a up, 2->a down
#     for i in range(n):
#         if s1[i] != s2[i]:
#             num_diffs += 1
#             if s1[i] == 'a':
#                 diffs.append(1)
#             else:
#                 diffs.append(2)
#         else:
#             diffs.append(0)

#     if num_diffs % 2 == 1:
#         print(-1)
#         return

#     result = []
#     c = 0
#     for j in range(1, 3, 1):
#         while diffs.count(j) > 1:
#             one_index = diffs.index(j)
#             diffs[one_index] = 0

#             one_index_2 = diffs.index(j)
#             diffs[one_index_2] = 0
#             c+= 1
#             result.append(str(one_index+1) + " " + str(one_index_2+1))
#             # print(str(one_index+1), str(one_index_2+1))

#     while diffs.count(0) < len(diffs):
#         one_index = diffs.index(1)
#         diffs[one_index] = 0

#         one_index_2 = diffs.index(2)
#         diffs[one_index_2] = 0
#         c+= 2
#         result.append(str(one_index+1) + " " + str(one_index+1))
#         result.append(str(one_index+1) + " " + str(one_index_2+1))
#         # print(str(one_index+1), str(one_index+1))
#         # print(str(one_index+1), str(one_index_2+1))

#     print(c)
#     for i in result:
#         print(i)



def run():
    n = eval(input())
    s1 = input()
    s2 = input()

    num_diffs = 0
    # diffs = [] # 0, 1-> a up, 2->a down
    one_ind = []
    two_ind = []
    for i in range(n):
        if s1[i] != s2[i]:
            # num_diffs += 1
            if s1[i] == 'a':
                # diffs.append(1)
                one_ind.append(i)
            else:
                # diffs.append(2)
                two_ind.append(i)
        # else:
            # diffs.append(0)

    if (len(one_ind) + len(two_ind)) % 2 == 1:
        print(-1)
        return

    result = []
    c = 0
    last_one = None
    last_two = None

    i = 0
    while i < len(one_ind):
        if i == len(one_ind)-1:
            break
        result.append(str(one_ind[i]+1) + " " + str(one_ind[i+1]+1))
        i += 2

    if i == len(one_ind) - 1:
        one_ind = one_ind[i:]
    else:
        one_ind = []

    j = 0
    while j < len(two_ind):
        if j == len(two_ind)-1:
            break
        result.append(str(two_ind[j]+1) + " " + str(two_ind[j+1]+1))
        j += 2

    if j == len(two_ind) - 1:
        two_ind = two_ind[j:]
    else:
        two_ind = []
    ##########
    
    if len(two_ind) > 0:
        result.append(str(one_ind[-1]+1) + " " + str(one_ind[-1]+1))
        result.append(str(one_ind[-1]+1) + " " + str(two_ind[-1]+1))
    
    c = len(result)
    # if len(two_ind) > 0:
    #     c += 2

    print(c)
    for i in result:
        print(i)
        



if __name__ == '__main__':
    run()
