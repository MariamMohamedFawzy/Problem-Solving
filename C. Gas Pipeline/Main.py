
def handle_case(n, pipe, pillar, s):
    num_pipe = 0.5
    num_pillar = 1
    last = 'down'

    def increase_by(num_pipe, pipe_inc, num_pillar, pillar_inc):
        num_pipe += pipe_inc
        num_pillar += pillar_inc 
        # print(num_pipe, num_pillar)
        return num_pipe, num_pillar

    def is_good_to_down(i):
        # print('enter', i)
        nearest_one_indx = s[i:].find('1')
        if nearest_one_indx == -1:
            return 'down', i, 2, 2
        nearest_minus_2 = nearest_one_indx - 1
        cost_of_down = 4 * pipe + 4 * pillar + nearest_minus_2 * (pipe + pillar)
        cost_of_up = 2 * pipe + 4 * pillar + nearest_minus_2 * (pipe + 2 * pillar)
        if cost_of_down < cost_of_up:
            # print('will go down')
            return 'up', nearest_one_indx + i, 4 + nearest_minus_2, 4 + nearest_minus_2
        else:
            return 'up', nearest_one_indx + i, 2 + nearest_minus_2, 4 + nearest_minus_2 * 2
        
            
    i = 1
    # for i in range(1, len(s)):
    while i < len(s):
        if ''.join([s[i-1:i+1]]) == '11':
            num_pipe, num_pillar = increase_by(num_pipe, 1, num_pillar, 2)
        
        elif ''.join([s[i-1:i+1]]) == '01':
            if last == 'down':
                num_pipe, num_pillar = increase_by(num_pipe, 2, num_pillar, 2)
                last = 'up'
            else:
                num_pipe, num_pillar = increase_by(num_pipe, 1, num_pillar, 2)

        elif ''.join([s[i-1:i+1]]) == '00':
            if last == 'down':
                num_pipe, num_pillar = increase_by(num_pipe, 1, num_pillar, 1)
            else:
                num_pipe, num_pillar = increase_by(num_pipe, 1, num_pillar, 2)

        elif ''.join([s[i-1:i+1]]) == '10':
            last, i, pipe_inc, pillar_inc = is_good_to_down(i)
            num_pipe, num_pillar = increase_by(num_pipe, pipe_inc, num_pillar, pillar_inc)
            # i -= 1
            # print('out', i, last, pipe_inc, pillar_inc)
        # print(last)
        i += 1 
        

    num_pipe += 0.5
    num_pillar += 1

    cost = pipe * num_pipe + pillar * num_pillar

    print(int(cost))

def run():
    T = eval(input())

    queries = []
    for i in range(T):
        n, a, b = list(map(int, input().split()))
        s = input()
        queries.append((n, a, b, s))
    
    # print('........')
    for query in queries:
        n, a, b, s = query
        handle_case(n, a, b, s)

if __name__ == "__main__":
    run()