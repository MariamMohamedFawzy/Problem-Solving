

def run():
    n = eval(input())
    nums = list(map(int, input().split()))

    pos = 0
    neg = 0
    # for i in range(n):
    #     num = nums[i]
    #     pos_so_far = 0
    #     neg_so_far = 0
    #     for j in range(i, n, 1):
    #         if nums[j] > 0:
    #             pos_so_far += 1
    #         else:
    #             neg_so_far += 1
            
    #         if (neg_so_far) % 2 == 0:
    #             pos += 1
    #         else:
    #             neg += 1

    all_pos = [0] * n
    all_neg = [0] * n
    for i in range(n-1, -1, -1):
        num = nums[i]
        if i == n-1:
            if num > 0:
                all_pos[i] = 1
            else:
                all_neg[i] = 1
        else:
            if num > 0:
                all_pos[i] = 1
            else:
                all_neg[i] = 1

            if nums[i] > 0:
                if nums[i+1] > 0:
                    all_pos[i] = all_pos[i] + all_pos[i+1]
                    all_neg[i] = all_neg[i] + all_neg[i+1]
                else:
                    all_pos[i] = all_pos[i] + all_pos[i+1]
                    all_neg[i] = all_neg[i] + all_neg[i+1]
            else:
                if nums[i+1] > 0:
                    all_pos[i] = all_pos[i] + all_neg[i+1]
                    all_neg[i] = all_neg[i] + all_pos[i+1]
                else:
                    all_pos[i] = all_pos[i] + all_neg[i+1]
                    all_neg[i] = all_neg[i] + all_pos[i+1]


            # if nums[i] * nums[i+1] > 0:
            #     # if nums[i] > 0:
            #     all_pos[i] = all_pos[i] + all_pos[i+1]
            #     all_neg[i] = all_neg[i] + all_neg[i+1]
            # else:
            #     all_pos[i] = all_pos[i] + all_neg[i+1]
            #     all_neg[i] = all_neg[i] + all_pos[i+1]

    neg = sum(all_neg)
    pos = sum(all_pos)
    print(neg, pos)


if __name__ == '__main__':
    run()
