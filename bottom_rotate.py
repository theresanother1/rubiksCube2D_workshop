import tensorflow as tf
import globals as glob


def rotate_cube_bottom_90_degrees_left(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[1])  # save color of backside before assigning new values
    save_bottom = tf.Variable(rubiks_cube_tensor[0])  # save color of bottom to rotate the values
    for pages in range(0, 6):
        if pages == 0:  # bottom page needs to be rotated
            glob.rotate_page_values_index_start(rubiks_cube_tensor=rubiks_cube_tensor,
                                                save_side=save_bottom, pages=pages)

        elif pages == 1:  # back side, values need to be reversed
            x = 8
            for position2 in range(0, 3):
                rubiks_cube_tensor[pages, position2, 0].assign(rubiks_cube_tensor[pages + 2][x][0])
                x = x - 1

        elif pages == 2:  # top will not be moved
            continue

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
        if pages == 5 or pages == 4:
            for position1 in range(6, 9):
                rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages - 1][position1][0])

        elif pages == 3:  # page 3 gets reversed value from back side
            x = 2
            for position3 in range(6, 9):
                rubiks_cube_tensor[pages, position3, 0].assign(rubiks_cube_tensor[pages - 2][x][0])
                x = x - 1

        elif pages == 2:  # top will not be moved
            continue

        elif pages == 1:  # backside needs the saved colors reversed
            x = 8
            for position2 in range(0, 3):
                rubiks_cube_tensor[pages, position2, 0].assign(save_color[x][0])
                x = x - 1

        elif pages == 0:  # bottom page needs to be rotated
            glob.rotate_page_vals_index_end(rubiks_cube_tensor=rubiks_cube_tensor, save_side=save_bottom, pages=pages)






