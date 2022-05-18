import tensorflow as tf
import globals as glob


def rotate_cube_top_90_degrees_left(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[1])
    save_top = tf.Variable(rubiks_cube_tensor[2])
    for pages in range(1, 6):
        if pages == 1:
            x = 2
            for position2 in range(6, 9):
                rubiks_cube_tensor[pages, position2, 0].assign(rubiks_cube_tensor[pages + 2][x][0])
                x -= 1

        elif pages == 2:
            glob.rotate_page_vals_index_end(rubiks_cube_tensor=rubiks_cube_tensor, save_side=save_top, pages=pages)

        elif pages == 3 or pages == 4:
            for position1 in range(0, 3):
                rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages + 1][position1][0])

        elif pages == 5:
            x = 8
            for position3 in range(0, 3):
                rubiks_cube_tensor[pages, position3, 0].assign(save_color[x][0])
                x -= 1


def rotate_cube_top_90_degrees_right(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[5])
    save_top = tf.Variable(rubiks_cube_tensor[2])
    for pages in range(5, 0, -1):
        if pages == 4 or pages == 5:
            for position1 in range(0, 3):
                rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages - 1][position1][0])

        elif pages == 3:
            x = 8
            for position3 in range(0, 3):
                rubiks_cube_tensor[pages, position3, 0].assign(rubiks_cube_tensor[pages - 2][x][0])
                x -= 1

        elif pages == 2:
            glob.rotate_page_values_index_start(rubiks_cube_tensor=rubiks_cube_tensor, save_side=save_top, pages=pages)

        elif pages == 1:
            x = 2
            for position2 in range(6, 9):
                rubiks_cube_tensor[pages, position2, 0].assign(save_color[x][0])
                x -= 1


