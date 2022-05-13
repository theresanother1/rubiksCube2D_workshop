import tensorflow as tf


def rotate_cube_bottom_90_degrees_left(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[1])  # save color of backside before assigning new values
    save_bottom = tf.Variable(rubiks_cube_tensor[0])  # save color of bottom to rotate the values
    for pages in range(0, 6):
        if pages == 2:  # top will not be moved
            continue

        if pages == 0:  # bottom page needs to be rotated
            positional_cnt1 = 2
            positional_cnt2 = 1
            positional_cnt3 = 0
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 0:
                    rubiks_cube_tensor[pages, position, 0].assign(save_bottom[positional_cnt1][0])
                    positional_cnt1 = positional_cnt1 + 3
                elif rubiks_cube_tensor[pages][position][2] == 1:
                    rubiks_cube_tensor[pages, position, 0].assign(save_bottom[positional_cnt2][0])  #
                    positional_cnt2 = positional_cnt2 + 3
                elif rubiks_cube_tensor[pages][position][2] == 2:
                    rubiks_cube_tensor[pages, position, 0].assign(save_bottom[positional_cnt3][0])
                    positional_cnt3 = positional_cnt3 + 3

        elif pages == 1:  # back side, values need to be reversed
            x = 8
            for position2 in range(0, 3):
                rubiks_cube_tensor[pages, position2, 0].assign(rubiks_cube_tensor[pages + 2][x][0])
                x = x - 1

        elif pages == 3 or pages == 4:
            for position1 in range(6, 9):
                rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages + 1][position1][0])

        elif pages == 5:  # right side needs the values from back reversed
            x = 2
            for position3 in range(6, 9):
                rubiks_cube_tensor[pages, position3, 0].assign(save_color[x][0])
                x -= 1


def rotate_cube_bottom_90_degrees_right(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[5])
    save_bottom = tf.Variable(rubiks_cube_tensor[0])
    for pages in range(5, -1, -1):
        if pages == 2:  # top will not be moved
            continue

        if pages == 0:  # bottom page needs to be rotated
            positional_cnt1 = 6
            positional_cnt2 = 7
            positional_cnt3 = 8
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 0:
                    rubiks_cube_tensor[pages, position, 0].assign(save_bottom[positional_cnt1][0])
                    positional_cnt1 = positional_cnt1 - 3

                elif rubiks_cube_tensor[pages][position][2] == 1:
                    rubiks_cube_tensor[pages, position, 0].assign(save_bottom[positional_cnt2][0])  #
                    positional_cnt2 = positional_cnt2 - 3

                elif rubiks_cube_tensor[pages][position][2] == 2:
                    rubiks_cube_tensor[pages, position, 0].assign(save_bottom[positional_cnt3][0])
                    positional_cnt3 = positional_cnt3 - 3

        elif pages == 1:  # backside needs the saved colors reversed
            x = 8
            for position2 in range(0, 3):
                rubiks_cube_tensor[pages, position2, 0].assign(save_color[x][0])
                x = x - 1

        elif pages == 5 or pages == 4:
            for position1 in range(6, 9):
                rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages - 1][position1][0])

        elif pages == 3:  # page 3 gets reversed value from back side
            x = 2
            for position3 in range(6, 9):
                rubiks_cube_tensor[pages, position3, 0].assign(rubiks_cube_tensor[pages - 2][x][0])
                x = x - 1
