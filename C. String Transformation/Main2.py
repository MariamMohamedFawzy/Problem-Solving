
def run():
    n = input()

    seq = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    seq = ''.join(seq)

    not_seen = 0

    new_seq = ""

    for i in range(len(n)):
        if n[i] in seq[:not_seen+1]:
            new_seq += seq[not_seen]
            not_seen += 1
        else:
            new_seq += n[i]

        if not_seen == 26:
            break

    if not_seen < 26:
        print(-1)
    else:
        print(new_seq + n[i+1:])







if __name__ == '__main__':
    run()
