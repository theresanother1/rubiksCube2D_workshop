import numpy as np
import tensorflow as tf
import globals as glob
import right_side_rotate as right
import left_side_rotate as left
import top_rotate as top
import bottom_rotate as bottom
# rubiks_cube = glob.rubiks_cube
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
            color_picking(rubiks_cube_tensor[page][position][0])
    print("\r\n")
    for page in range(3, 6):
        for position in range(3, 6):
            color_picking(rubiks_cube_tensor[page][position][0])
    print("\r\n")
    for page in range(3, 6):
        for position in range(6, 9):
            color_picking(rubiks_cube_tensor[page][position][0])

    print("\r\n")


def color_picking(number):
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


'''def rotate_cube_bottom_90_degrees_left():
    save_color = tf.Variable(rubiks_cube_tensor[1])
    for pages in range(1, 6):
        if pages == 2:
            continue
        # starting at page 0, page 4 will then get the values needed from save_color
        if pages != 5:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 2:
                    # avoid values from page 3, as they are not needed in this angle
                    if pages + 1 == 2:
                        rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages + 2][position])
                    else:
                        rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages + 1][position])
        else:
            # page is 5, meaning, page 5 gets the saved page 1 values
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 2:
                    rubiks_cube_tensor[pages, position].assign(save_color[position])
'''
'''
def rotate_cube_bottom_90_degrees_right():
    save_color = tf.Variable(rubiks_cube_tensor[5])
    for pages in range(5, 0, -1):
        if pages == 2:
            continue
        # starting at page 0, page 4 will then get the values needed from save_color
        if pages != 1:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 2:
                    # avoid values from page 3, as they are not needed in this angle
                    if pages - 1 == 2:
                        rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 2][position])
                    else:
                        rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 1][position])
        else:
            # page is 5, meaning, page 5 gets the saved page 1 values
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 2:
                    rubiks_cube_tensor[pages, position].assign(save_color[position])
'''

def print_menu():
    print("rotate right side of the cube forward:      1")
    print("rotate right side of the cube backwards:    2")
    print("rotate left side of the cube forwards:      3")
    print("rotate left side of the cube backwards:     4")
    print("rotate top of the cube 90 degrees left:     5")
    print("rotate top of the cube 90 degrees right:    6")
    print("rotate bottom of the cube 90 degrees left:  7")
    print("rotate bottom of the cube 90 degrees right: 8")
    print("end game: 0")


def main():
    print(rubiks_cube_tensor)
    # print(rubiks_cube)
    print("Welcome to Rubiks Cube: ")
    print_menu()
    print_complete_rubiks_cube()
    user_input = int(input("Please enter a number for your actions: \r\n"))
    # user_input = 1

    run = True
    while run:
        if user_input < 0 or user_input > 8:
            user_input = int(input("Please choose a number shown in the menu (0 - 8) \r\n"))

        elif user_input == 1:
            # print("BEFORE RIGHTSIDE FORWARDS ROTATION")
            # print_complete_rubiks_cube()
            right.rotate_cube_right_side_90_degrees_forwards(rubiks_cube_tensor)
            print("AFTER RIGHTSIDE FORWARDS ROTATION")
            print_complete_rubiks_cube()
            print_menu()
            user_input = int(input("Please enter a number for your actions: \r\n"))

        # user_input = 2
        elif user_input == 2:
            # print("BEFORE RIGHTSIDE BACKWARDS ROTATION")
            # print_complete_rubiks_cube()
            right.rotate_cube_right_side_90_degrees_backwards(rubiks_cube_tensor)
            print("AFTER RIGHTSIDE BACKWARDS ROTATION")
            print_complete_rubiks_cube()
            print_menu()
            user_input = int(input("Please enter a number for your actions: \r\n"))

        # user_input = 3
        elif user_input == 3:
            # print("BEFORE LEFTSIDE FORWARDS ROTATION")
            # print_complete_rubiks_cube()
            left.rotate_cube_left_side_90_degrees_forwards(rubiks_cube_tensor)
            print("AFTER LEFTSIDE FORWARDS ROTATION")
            print_complete_rubiks_cube()
            print_menu()
            user_input = int(input("Please enter a number for your actions: \r\n"))

        # user_input = 4
        elif user_input == 4:
            # print("BEFORE LEFTSIDE BACKWARDS ROTATION")
            # print_complete_rubiks_cube()
            left.rotate_cube_left_side_90_degrees_backwards(rubiks_cube_tensor)
            print("AFTER LEFTSIDE BACKWARDS ROTATION")
            print_complete_rubiks_cube()
            print_menu()
            user_input = int(input("Please enter a number for your actions: \r\n"))

        # user_input = 5
        elif user_input == 5:
            print("DOING ROTATE TOP LEFT")
            # print_complete_rubiks_cube()
            top.rotate_cube_top_90_degrees_left(rubiks_cube_tensor)
            print("AFTER ROTATE TOP LEFT")
            print_complete_rubiks_cube()
            print_menu()
            user_input = int(input("Please enter a number for your actions: \r\n"))

        # user_input = 6
        elif user_input == 6:
            # print("BEFORE ROTATE TOP RIGHT")
            # print_complete_rubiks_cube()
            top.rotate_cube_top_90_degrees_right(rubiks_cube_tensor)
            print("AFTER ROTATE TOP RIGHT")
            print_complete_rubiks_cube()
            print_menu()
            user_input = int(input("Please enter a number for your actions: \r\n"))

        # user_input = 7
        elif user_input == 7:
            # print("BEFORE ROTATE BOTTOM LEFT")
            # print_complete_rubiks_cube()
            bottom.rotate_cube_bottom_90_degrees_left(rubiks_cube_tensor)
            print("AFTER ROTATE BOTTOM LEFT")
            print_complete_rubiks_cube()
            print_menu()
            user_input = int(input("Please enter a number for your actions: \r\n"))

        # user_input = 8
        elif user_input == 8:
            # print("BEFORE ROTATE BOTTOM RIGHT")
            # print_complete_rubiks_cube()
            bottom.rotate_cube_bottom_90_degrees_right(rubiks_cube_tensor)
            print("AFTER ROTATE BOTTOM RIGHT")
            print_complete_rubiks_cube()
            print_menu()
            user_input = int(input("Please enter a number for your actions: \r\n"))

        elif user_input == 0:
            print_complete_rubiks_cube()
            print(glob.colors.OKBLUE + "THANKS FOR PLAYING - HAVE A PLEASANT REST OF THE DAY" + glob.colors.ENDC)
            run = False


# print_complete_rubiks_cube()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
