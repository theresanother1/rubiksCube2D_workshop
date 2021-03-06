# ------------------------------------------------------------------
# Filename:    left_side_rotate.py
# Author: Theresa Spiel
# ------------------------------------------------------------------
# File description:
# Provides functions for rotating the left of the Rubik's Cube.
# ------------------------------------------------------------------

# ------------------------------------------------------
# Modules to import
# ------------------------------------------------------

import tensorflow as tf
import globals as glob


# ---------------------------------------------------------------
# def rotate_cube_left_side_90_degrees_forwards(rubiks_cube_tensor)
# ---------------------------------------------------------------
def rotate_cube_left_side_90_degrees_forwards(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[4])
    save_side = tf.Variable(rubiks_cube_tensor[3])
    for pages in range(4, -1, -1):
        if pages == 3:      # rotate left side
            glob.rotate_page_vals_index_end(rubiks_cube_tensor=rubiks_cube_tensor, save_side=save_side, pages=pages)

        elif pages == 2 or pages == 1 or pages == 4:    # reassign values
            for position in range(0, 9, 3):
                if pages - 1 == 3:
                    rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 2][position][0])
                else:
                    rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 1][position][0])

        elif pages == 0:        # reassign saved values
            for position in range(0, 9, 3):
                rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])


# ---------------------------------------------------------------
# def rotate_cube_left_side_90_degrees_backwards(rubiks_cube_tensor)
# ---------------------------------------------------------------
def rotate_cube_left_side_90_degrees_backwards(rubiks_cube_tensor):
    save_color = tf.Variable(rubiks_cube_tensor[0])
    save_side = tf.Variable(rubiks_cube_tensor[3])
    for pages in range(0, 5):
        if pages == 2 or pages == 1 or pages == 0:      # reassign values
            for position in range(0, 9, 3):
                if pages + 1 == 3:
                    rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages + 2][position][0])
                else:
                    rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages + 1][position][0])

        elif pages == 3:        # rotate left side
            glob.rotate_page_values_index_start(rubiks_cube_tensor=rubiks_cube_tensor, save_side=save_side, pages=pages)

        elif pages == 4:        # reassign saved values
            for position in range(0, 9, 3):
                rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])

