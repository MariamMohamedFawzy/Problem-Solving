
import math


def CallMyFunc():
    n = input()
    arr = [[0, 0] for i in range(n)]

    for i in range(n):
        arr[i] = map(int, raw_input().split())

    start_x = arr[0][0]
    start_y = arr[0][1]

    set_distances = set()
    map_distances = {}

    for i in range(n):
        current_x = arr[i][0]
        current_y = arr[i][1]
        dist_curr = math.sqrt(math.pow(current_x - start_x, 2) + math.pow(current_y - start_y, 2))
        # print "i : ", i, " dist : ", dist_curr
        set_distances.add(dist_curr)
        # print "set : ", set_distances
        if map_distances.has_key(dist_curr):
            temp = map_distances.get(dist_curr)
            temp.add(i)
        else:
            map_distances[dist_curr] = set([i])
        # print "i : ", i,  " ", map_distances

    sorted_distances = sorted(set_distances)

    # print map_distances
    first = -1
    second = -1
    for i in sorted_distances:
        if i == 0.0:
            continue
        set_points = map_distances[i]
        for j in set_points:
            if first == -1:
                first = j
            elif second == -1:
                first_x = arr[first][0]
                first_y = arr[first][1]
                second_x = arr[j][0]
                second_y = arr[j][1]
                # if second_x - first_x == first_x - start_x and second_y - first_y == first_y - start_y:
                if (start_y - first_y) * (start_x - second_x) == (start_y - second_y) * (start_x - first_x):
                    continue
                else:
                    second = j
                    break
            else:
                break
        if first != -1 and second != -1:
            break


    print 1, " ", first + 1, " ", second + 1





if __name__ == '__main__':
    CallMyFunc()
