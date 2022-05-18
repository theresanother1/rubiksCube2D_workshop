# ------------------------------------------------------------------
# Filename:    right_side_rotate.py
# ------------------------------------------------------------------
# File description:
# Provides functions for rotating the right side of the Rubik's Cube.
# ------------------------------------------------------------------

# ------------------------------------------------------
# Modules to import
# ------------------------------------------------------

import tensorflow as tf
import globals as glob


# ---------------------------------------------------------------
# def rotate_cube_right_side_90_degrees_forwards(rubiks_cube_tensor)
# ---------------------------------------------------------------
def rotate_cube_right_side_90_degrees_forwards(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[4])
    save_side = tf.Variable(rubiks_cube_tensor[5])
    for pages in range(5, -1, -1):
        if pages == 5:
            glob.rotate_page_values_index_start(rubiks_cube_tensor=rubiks_cube_tensor, save_side=save_side, pages=pages)

        elif pages == 3:
            continue
        if pages == 2 or pages == 1 or pages == 4:
            for position in range(2, 9, 3):
                if pages - 1 == 3:
                    rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 2][position][0])
                else:
                    rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 1][position][0])
        elif pages == 0:
            for position in range(2, 9, 3):
                rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])


# ---------------------------------------------------------------
# def rotate_cube_right_side_90_degrees_backwards(rubiks_cube_tensor)
# ---------------------------------------------------------------
def rotate_cube_right_side_90_degrees_backwards(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[0])
    save_side = tf.Variable(rubiks_cube_tensor[5])
    for pages in range(0, 6):
        if pages == 2 or pages == 1 or pages == 0:
            for position in range(2, 9, 3):
                if pages + 1 == 3:
                    rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages + 2][position][0])
                else:
                    rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages + 1][position][0])

        elif pages == 3:
            continue

        elif pages == 4:
            for position in range(2, 9, 3):
                rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])

        elif pages == 5:
            glob.rotate_page_vals_index_end(rubiks_cube_tensor=rubiks_cube_tensor, save_side=save_side, pages=pages)
