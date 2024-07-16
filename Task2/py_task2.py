import math

# calculate and output point status
# c_pos - circle coordinates
# c_r   - circle ratius
# p_pos -  point coordinates


def check_point(c_pos, c_r, p_pos):
    c_p_dist = math.sqrt((p_pos[0] - c_pos[0])**2 + (p_pos[1] - c_pos[1])**2)

    if math.isclose(c_p_dist, c_r):
        print('0')
    elif c_p_dist < c_r:
        print('1')
    else:
        print('2')


with open(str('file1.txt'), 'r') as circle_file:
    temp = circle_file.readline().split(' ')
    circle_pos = [float(temp[0]), float(temp[1])]

    circle_rad = float(circle_file.readline())


with open(str('file2.txt'), 'r') as points_file:
    for line in points_file:
        temp = line.split(' ')
        check_point(circle_pos, circle_rad, [float(temp[0]), float(temp[1])])
