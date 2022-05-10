import tensorflow as tf


def rotate_cube_top_90_degrees_left(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[1])
    print(save_color)
    save_top = tf.Variable(rubiks_cube_tensor[2])
    print("top part of cube")
    print(save_top)
    for pages in range(1, 6):
        # print("for loop at " + str(pages))
        if pages == 2:
            positional_cnt1 = 6
            positional_cnt2 = 7
            positional_cnt3 = 8
            for position in range(0, 9):

                if rubiks_cube_tensor[pages][position][2] == 0:
                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt1][0])
                    positional_cnt1 = positional_cnt1 - 3

                elif rubiks_cube_tensor[pages][position][2] == 1:
                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt2][0])  #
                    positional_cnt2 = positional_cnt2 - 3

                elif rubiks_cube_tensor[pages][position][2] == 2:
                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt3][0])
                    positional_cnt3 = positional_cnt3 - 3
        elif pages == 3 or pages == 4:
            for position1 in range(0, 9):
                if rubiks_cube_tensor[pages][position1][2] == 0:
                    # if pages + 1 == 2:
                    #   rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages + 2][position1][0])
                    # else:
                    # showVal = rubiks_cube_tensor[pages + 1][position1]
                    rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages + 1][position1][0])
        elif pages == 1:
            x = 2
            for position2 in range(0, 9):
                if rubiks_cube_tensor[pages][position2][2] == 2:
                    rubiks_cube_tensor[pages, position2, 0].assign(rubiks_cube_tensor[pages + 2][x][0])
                    x -= 1
        elif pages == 5:
            x = 8
            for position3 in range(0, 9):
                if rubiks_cube_tensor[pages][position3][2] == 0:
                    rubiks_cube_tensor[pages, position3, 0].assign(save_color[x][0])
                    x -= 1


def rotate_cube_top_90_degrees_right(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[5])
    save_top = tf.Variable(rubiks_cube_tensor[2])
    for pages in range(5, 0, -1):
        # top
        if pages == 2:
            positional_cnt1 = 2
            positional_cnt2 = 1
            positional_cnt3 = 0
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 0:
                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt1][0])
                    positional_cnt1 = positional_cnt1 + 3

                elif rubiks_cube_tensor[pages][position][2] == 1:
                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt2][0])  #
                    positional_cnt2 = positional_cnt2 + 3

                elif rubiks_cube_tensor[pages][position][2] == 2:
                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt3][0])
                    positional_cnt3 = positional_cnt3 + 3

        if pages == 4 or pages == 5:
            for position1 in range(0, 9):
                if rubiks_cube_tensor[pages][position1][2] == 0:
                    rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages - 1][position1][0])
                    print("new colorValue")
                    print(rubiks_cube_tensor[pages][position1])
        elif pages == 1:
            x = 2
            for position2 in range(0, 9):
                if rubiks_cube_tensor[pages][position2][2] == 2:
                    rubiks_cube_tensor[pages, position2, 0].assign(save_color[x][0])
                    x -= 1
        elif pages == 3:
            x = 8
            for position3 in range(0, 9):
                if rubiks_cube_tensor[pages][position3][2] == 0:
                    rubiks_cube_tensor[pages, position3, 0].assign(rubiks_cube_tensor[pages - 2][x][0])
                    x -= 1
