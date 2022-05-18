import tensorflow as tf


class colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BLUEBACKGROUND = '\033[104m'
    REDBACKGROUND = '\033[101m'
    ORANGENOWPINKBACKGROUND = '\033[105m'
    YELLOWBACKGROUND = '\033[103m'
    GREENBACKGROUND = '\033[102m'
    WHITEBACKGROUND = '\033[107m'


rubiks_cube = tf.Variable([
    # orange now pink side
    [[3, 0, 0], [3, 1, 0], [3, 2, 0], [3, 0, 1], [3, 1, 1], [3, 2, 1], [3, 0, 2], [3, 1, 2], [3, 2, 2]],
    # blue side
    [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 0, 2], [0, 1, 2], [0, 2, 2]],
    # red side
    [[1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 0, 2], [1, 1, 2], [1, 2, 2]],
    # white side
    [[5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 0, 1], [5, 1, 1], [5, 2, 1], [5, 0, 2], [5, 1, 2], [5, 2, 2]],
    # green side
    [[2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 0, 1], [2, 1, 1], [2, 2, 1], [2, 0, 2], [2, 1, 2], [2, 2, 2]],
    # yellow side
    [[4, 0, 0], [4, 1, 0], [4, 2, 0], [4, 0, 1], [4, 1, 1], [4, 2, 1], [4, 0, 2], [4, 1, 2], [4, 2, 2]],
])


def rotate_page_values_index_start(rubiks_cube_tensor, save_side, pages):
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


def rotate_page_vals_index_end(rubiks_cube_tensor, save_side, pages):
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
