
def isVowel(x):
    return {
        'a': True,
        'A': True,
        'O': True,
        'o': True,
        'U': True,
        'u': True,
        'E': True,
        'e': True,
        'I': True,
        'i': True,
        'Y': True,
        'y': True
    }.get(x, False)

def FunctionToRunProgram():
    word = raw_input()
    newWord = ""
    for i in range(len(word)):
        c = word[i]
        if not isVowel(c):
            newWord += "." + c.lower()
    print(newWord)




if __name__ == "__main__":
    FunctionToRunProgram()

