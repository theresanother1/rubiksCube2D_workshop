import numpy as np
import tensorflow as tf
import globals as glob

rubiks_cube = glob.rubiks_cube
rubiks_cube_tensor = glob.rubiks_cube


def print_complete_rubiks_cube():
    # initial setup rubiks cube
    # top 3 "pages" of the rubiks cube
    for page in range(0, 3):
        # print(rubiks_cube_array[color])
        new_line_marker = 0
        for position in range(0, 9):
            if new_line_marker % 3 == 0:
                print("\r\n")

                '''pick the right color with extra spacing where needed'''
            if rubiks_cube_tensor[page][position][0] == 0:
                if rubiks_cube_tensor[page][position][1] == 0:
                    print("                 ", end=" ")
                print(glob.colors.BLUEBACKGROUND + "     " + glob.colors.ENDC, end=" ")
            elif rubiks_cube_tensor[page][position][0] == 1:
                if rubiks_cube_tensor[page][position][1] == 0:
                    print("                 ", end=" ")
                print(glob.colors.REDBACKGROUND + "     " + glob.colors.ENDC, end=" ")
            elif rubiks_cube_tensor[page][position][0] == 3:
                if rubiks_cube_tensor[page][position][1] == 0:
                    print("                 ", end=" ")
                print(glob.colors.ORANGENOWPINKBACKGROUND + "     " + glob.colors.ENDC, end=" ")
            elif rubiks_cube_tensor[page][position][0] == 2:
                if rubiks_cube_tensor[page][position][1] == 0:
                    print("                 ", end=" ")
                print(glob.colors.GREENBACKGROUND + "     " + glob.colors.ENDC, end=" ")
            elif rubiks_cube_tensor[page][position][0] == 4:
                if rubiks_cube_tensor[page][position][1] == 0:
                    print("                 ", end=" ")
                print(glob.colors.YELLOWBACKGROUND + "     " + glob.colors.ENDC, end=" ")
            elif rubiks_cube_tensor[page][position][0] == 5:
                if rubiks_cube_tensor[page][position][1] == 0:
                    print("                 ", end=" ")
                print(glob.colors.WHITEBACKGROUND + "     " + glob.colors.ENDC, end=" ")

            new_line_marker += 1

    print("\r\n")

    for page in range(3, 6):
        for position in range(0, 3):
            colorpicking(rubiks_cube_tensor[page][position][0])
    print("\r\n")
    for page in range(3, 6):
        for position in range(3, 6):
            colorpicking(rubiks_cube_tensor[page][position][0])
    print("\r\n")
    for page in range(3, 6):
        for position in range(6, 9):
            colorpicking(rubiks_cube_tensor[page][position][0])

    print("\r\n")


def colorpicking(number):
    if number == 0:
        print(glob.colors.BLUEBACKGROUND + "     " + glob.colors.ENDC, end=" ")
    elif number == 1:
        print(glob.colors.REDBACKGROUND + "     " + glob.colors.ENDC, end=" ")
    elif number == 3:
        print(glob.colors.ORANGENOWPINKBACKGROUND + "     " + glob.colors.ENDC, end=" ")
    elif number == 2:
        print(glob.colors.GREENBACKGROUND + "     " + glob.colors.ENDC, end=" ")
    elif number == 4:
        print(glob.colors.YELLOWBACKGROUND + "     " + glob.colors.ENDC, end=" ")
    elif number == 5:
        print(glob.colors.WHITEBACKGROUND + "     " + glob.colors.ENDC, end=" ")


def rotate_cube_right_side_90_degrees_forwards():
    save_color = tf.Variable(rubiks_cube_tensor[4])
    # print("save color array values: ")
    # print(save_color)
    for pages in range(4, -1, -1):
        if pages == 3:
            continue
        else:
            # it only starts at page 4, because in our angle, green is up front = page 4, angle stays the same
            if pages != 0:
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 2:
                        # print("current color ")
                        # print(rubiks_cube_tensor[pages][position])

                        # avoid values from page 3, as they are not needed in this angle
                        if pages - 1 == 3:
                            # print(rubiks_cube_tensor[pages-2][position])
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 2][position])
                            # print("new colors")
                            # print(rubiks_cube_tensor[pages][position])
                        else:
                            # print(rubiks_cube_tensor[pages - 1][position])
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 1][position])
                            # print("new colors")
                            # print(rubiks_cube_tensor[pages][position])

            else:
                # page is 0, meaning, page 0 gets the saved page 4 values
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 2:
                        # print("current color ")
                        # print(rubiks_cube_tensor[pages][position])
                        # print(save_color[position])
                        rubiks_cube_tensor[pages, position].assign(save_color[position])


def rotate_cube_right_side_90_degrees_backwards():
    save_color = tf.Variable(rubiks_cube_tensor[0])
    # print("save color array values: ")
    # print(save_color)
    for pages in range(0, 5):
        if pages == 3:
            continue
        else:
            # starting at page 0, page 4 will then get the values needed from save_color
            if pages != 4:
                for position in range(0, 9):
                    if rubiks_cube[pages][position][1] == 2:
                        # print("current color ")
                        # print(rubiks_cube[pages][position])
                        # print(rubiks_cube[pages + 1][position])

                        # avoid values from page 3, as they are not needed in this angle
                        if pages + 1 == 3:
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages + 2][position])
                        else:
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages + 1][position])
                        # print("new color")
                        # print(rubiks_cube[pages][position])
            else:
                # page is 4, meaning, page 4 gets the saved page 0 values
                for position in range(0, 9):
                    if (rubiks_cube[pages][position][1] == 2):
                        # print("current color ")
                        # print(rubiks_cube[pages][position])
                        # print(save_color[position])
                        rubiks_cube_tensor[pages, position].assign(save_color[position])


def rotate_cube_left_side_90_degrees_forwards():
    save_color = tf.Variable(rubiks_cube_tensor[4])
    # print("save color array values: ")
    # print(save_color)
    for pages in range(4, -1, -1):
        if pages == 3:
            continue
        else:
            # it only starts at page 4, because in our angle, green is up front = page 4, angle stays the same
            if pages != 0:
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 0:
                        # print("current color ")
                        # print(rubiks_cube_tensor[pages][position])
                        # print(rubiks_cube_tensor[pages-1][position])

                        # avoid values from page 3, as they are not needed in this angle
                        if pages - 1 == 3:
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 2][position])
                        else:
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 1][position])
            else:
                # page is 0, meaning, page 0 gets the saved page 4 values
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 0:
                        rubiks_cube_tensor[pages, position].assign(save_color[position])


def main():
    print(rubiks_cube_tensor)
    print(rubiks_cube)
    print("Welcome to Rubiks Cube: ")
    print("rotate right side of the cube forward: 1")
    print("rotate right side of the cube backwards: 2")
    print("rotate left side of the cube forwards: 3")
    print("end game: 0")
    print_complete_rubiks_cube()
    # user_input = input("Please enter a number for your actions: ")
    user_input = 1

    if user_input == 1:
        print("BEFORE RIGHTSIDE FORWARDS ROTATION")
        print_complete_rubiks_cube()
        rotate_cube_right_side_90_degrees_forwards()
        print("AFTER RIGHTSIDE FORWARDS ROTATION")
        print_complete_rubiks_cube()
        # user_input = input("Please enter a number for your actions: ")

    user_input = 2
    if user_input == 2:
        print("BEFORE RIGHTSIDE BACKWARDS ROTATION")
        print_complete_rubiks_cube()
        rotate_cube_right_side_90_degrees_backwards()
        print("AFTER RIGHTSIDE BACKWARDS ROTATION")
        print_complete_rubiks_cube()
        rotate_cube_right_side_90_degrees_backwards()
        # user_input = input("Please enter a number for your actions: ")

    user_input = 3
    if user_input == 3:
        print("BEFORE LEFTSIDE FORWARDS ROTATION")
        print_complete_rubiks_cube()
        rotate_cube_left_side_90_degrees_forwards()
        print("AFTER LEFTSIDE FORWARDS ROTATION")
        print_complete_rubiks_cube()
        # user_input = input("Please enter a number for your actions: ")


# print_complete_rubiks_cube()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
