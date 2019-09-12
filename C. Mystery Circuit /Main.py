def run():
    a = eval(input())

    def get_bin(num):
        result = ""
        for i in [8, 4, 2, 1]:
            if num >= i:
                result = result + "1"
                num -= i
            else:
                result = result + "0"
        return result

    def get_dec(s):
        result = 0
        for i in range(len(s)):
            if s[i] == '1':
                result += 2 ** (3-i)
        return result

    a = get_bin(a)[::-1]
    a = get_dec(a) - 1
    if a < 0:
        a = get_bin(a)
        temp = ""
        for i in range(len(a)):
            if a[i] == '0':
                temp += '1'
            else:
                temp += '0'
        a = temp
        a = get_dec(a)
        a += 1
        a = get_bin(a)
    else:
        a = get_bin(a)
    a = get_dec(a[::-1])
    print(a)


if __name__ == "__main__":
    run()