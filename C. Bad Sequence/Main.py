

def run():
    
    n = eval(input())

    st = input()

    if n % 2 == 1:
        print('No')
        return 

    stack = []
    for i in range(n):
        stack.append(st[i])
        if len(stack) >= 2:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
    if len(stack) == 0 or ''.join(stack) == ')(':
        print('Yes')
    else:
        print('No')

    

if __name__ == "__main__":
    run()