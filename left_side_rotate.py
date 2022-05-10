import tensorflow as tf


def rotate_cube_left_side_90_degrees_forwards(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[4])
    save_side = tf.Variable(rubiks_cube_tensor[3])
    for pages in range(4, -1, -1):
        '''if pages == 5:
            continue'''
        if pages == 3:
            positional_cnt1 = 6
            positional_cnt2 = 7
            positional_cnt3 = 8
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 0:
                    rubiks_cube_tensor[pages, position, 0].assign(save_side[positional_cnt1][0])
                    positional_cnt1 = positional_cnt1 - 3

                elif rubiks_cube_tensor[pages][position][2] == 1:
                    rubiks_cube_tensor[pages, position, 0].assign(save_side[positional_cnt2][0])  #
                    positional_cnt2 = positional_cnt2 - 3

                elif rubiks_cube_tensor[pages][position][2] == 2:
                    rubiks_cube_tensor[pages, position, 0].assign(save_side[positional_cnt3][0])
                    positional_cnt3 = positional_cnt3 - 3
        elif pages == 2 or pages == 1 or pages == 4:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][1] == 0:
                    if pages - 1 == 3:
                        rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 2][position][0])
                    else:
                        rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 1][position][0])
        elif pages == 0:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][1] == 0:
                    rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])


def rotate_cube_left_side_90_degrees_backwards(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[0])
    save_side = tf.Variable(rubiks_cube_tensor[3])
    for pages in range(0, 6):
        if pages == 2 or pages == 1 or pages == 0:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][1] == 0:
                    # avoid values from page 3, as they are not needed in this angle
                    if pages + 1 == 3:
                        rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages + 2][position][0])
                    else:
                        rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages + 1][position][0])

        elif pages == 3:
            positional_cnt1 = 2
            positional_cnt2 = 1
            positional_cnt3 = 0
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 0:
                    rubiks_cube_tensor[pages, position, 0].assign(save_side[positional_cnt1][0])
                    positional_cnt1 = positional_cnt1 + 3

                elif rubiks_cube_tensor[pages][position][2] == 1:
                    rubiks_cube_tensor[pages, position, 0].assign(save_side[positional_cnt2][0])  #
                    positional_cnt2 = positional_cnt2 + 3

                elif rubiks_cube_tensor[pages][position][2] == 2:
                    rubiks_cube_tensor[pages, position, 0].assign(save_side[positional_cnt3][0])
                    positional_cnt3 = positional_cnt3 + 3

        elif pages == 4:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][1] == 0:
                    rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])
        elif pages == 5:
            continue
