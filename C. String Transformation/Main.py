
def run():
    n = input()

    seq = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    pointer_1 = -1
    pointer_2 = -1
    new_seq= ""
    i = 0
    while i < len(n):

        if pointer_1 != -1:
            what_should_remain = 26 - (pointer_2 - pointer_1 + 1)
            remainder = len(n) - i
            if remainder < what_should_remain:
                if pointer_1 == -1:
                    pointer_2 = -1
                    pointer_1 = -1
                    new_seq = ""
                    break
                else:
                    i = pointer_1 + 1
                    pointer_2 = -1
                    pointer_1 = -1
                    new_seq = n[:i]
                    continue



        if pointer_1 == -1 and n[i] == 'a':
            pointer_1 = i
            pointer_2 = i
            new_seq = new_seq + n[i]
            i += 1
        elif pointer_1 != -1 and pointer_2 - pointer_1 < 25 and i < len(n):
            diff = pointer_2 - pointer_1

            if (diff + 1 < len(seq)) and seq[diff+1] == n[i] :
                pointer_2 += 1
                new_seq = new_seq + n[i]
                i += 1
            elif (diff + 1 < len(seq)) and n[i] != 'z' and (seq.index(n[i]) + 1 < len(seq)) and seq[seq.index(n[i]) + 1] == seq[diff+1]:
                pointer_2 += 1
                new_seq = new_seq + seq[seq.index(n[i]) + 1]
                i += 1
            else:
                i += 1
                # pointer_2 = -1
                # pointer_1 = -1
        elif pointer_1 != -1 and pointer_2 - pointer_1 == 25:
            break
        else:
            new_seq = new_seq + n[i]
            i += 1

    if pointer_1 == -1 or seq == "":
        print(-1)
    else:
        print(new_seq)





if __name__ == '__main__':
    run()
