

def FunctionToRunProgram():
    n = input()
    for i in range(n):
        word = raw_input()

        newWord = str(word)
        length = len(newWord)

        if length > 10:

            c1 = newWord[0]
            cLast = newWord[length - 1]
            newStr = c1 + str(length - 2) + cLast
            print(newStr)
        else:
            print(newWord)


if __name__ == "__main__":
    FunctionToRunProgram()


