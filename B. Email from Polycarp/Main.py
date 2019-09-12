import re

def run2():
    a = eval(input())
    inputs = []
    for i in range(2*a):
        inputs.append(input())
    i = 0
    while i < 2*a:
        m = [char for char in inputs[i]]
        pattern = '+'.join(m)
        pattern = '^' + pattern + "+$"
        text = inputs[i+1]
        if re.search(pattern, text):
            print('YES')
        else:
            print('NO')
        i += 2

def run():
    a = eval(input())
    inputs = []
    for i in range(2*a):
        inputs.append(input())
    i = 0
    while i < 2*a:
        text = inputs[i]
        new_text = inputs[i+1]
        c = 0
        j = 0
        flag = True
        while j < len(text) and c < len(new_text):
            if text[j] != new_text[c]:
                flag = False
                break
            if j + 1 < len(text) and c + 1 < len(new_text):
                if text[j+1] == text[j]:
                    j += 1
                    c += 1
                elif text[j] == new_text[c + 1]:
                    c += 1
                else:
                    j += 1
                    c += 1
            elif j < len(text) and c + 1 < len(new_text):
                c += 1
            else:
                j += 1
                c += 1
        if c < len(new_text) or j < len(text):
            flag = False
        if flag:
            print('YES')
        else:
            print('NO')

        i += 2
        


if __name__ == "__main__":
    run()