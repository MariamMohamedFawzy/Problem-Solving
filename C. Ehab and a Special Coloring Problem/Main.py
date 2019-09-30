
def run():
    n = eval(input())
    nums = [0] * (n-1)
    current = 2
    for i in range(2, n+1):
        j = i
        enter = False
        while j < n+1:
            if nums[j-2] == 0:
                enter = True
                nums[j-2] = current
            j += i

        if enter:
            current += 1
    
    for i in range(n-1):
        if nums[i] == current - 1:
            nums[i] = 1  

    print(' '.join(list(map(str, nums))))

if __name__ == '__main__':
    run()