

def run():
    n = eval(input())
    vals = []
    for _ in range(n):
        input()
        row1 = input()
        row2 = input()
        vals.append([row1, row2])


    pipes = dict()
    pipes['left_to_right'] = 1
    pipes['up_to_down'] = 1
    pipes['down_to_up'] = 1
    pipes['left_to_down'] = 6 
    pipes['left_to_up'] = 6
    pipes['right_to_down'] = 6 
    pipes['right_to_up'] = 6
    pipes['down_to_right'] = 6
    pipes['down_to_left'] = 6
    pipes['up_to_right'] = 6
    pipes['up_to_left'] = 6

    directions = dict()
    directions[1] = [1, 2]

    directions[6] = [3, 4, 5, 6]

    for i in range(n):
        row1 = [int(ch) for ch in vals[i][0]]
        row2 = [int(ch) for ch in vals[i][1]]
        rows = [row1, row2]
        
        current_row = 0
        current_col = 0
        current = 'left'
        j = 0
        next_direction = None
        while j <  len(row1):
            current_pipe = rows[current_row][j]
            next_direction = None
            possible_directions = []
            for key in pipes.keys():
                if key.startswith(current) and current_pipe in directions[pipes[key]]:
                    possible_directions.append(key.split('_')[2])


            if 'right' in possible_directions and\
                 ((current_col < len(row1) - 1 and current_row == 0) or (current_col < len(row1) and current_row == 1) ):
                next_direction = 'right'
            elif 'left' in possible_directions and current_col > 0:
                next_direction = 'left'
            elif 'up' in possible_directions and current_row == 1:
                next_direction = 'up'
            elif 'down' in possible_directions and current_row == 0:
                next_direction = 'down'

            if next_direction is None:
                break


            if next_direction != 'right' and current_row == 1 and current_col == len(row1)-1 and j == len(row1) - 1:
                break

            if next_direction == 'right':
                current = 'left'
                j += 1
                current_col += 1
            elif next_direction == 'left':
                current = 'right'
                j -= 1
                current_col -= 1
            elif next_direction == 'up':
                current = 'down' 
                current_row -= 1 
            elif next_direction == 'down':
                current = 'up'
                current_row += 1

                
        if j == len(row1) and current_col == len(row1) and current_row == 1 and next_direction == 'right':
            print('YES')
        else:
            print('NO')
            



if __name__ == '__main__':
    run()