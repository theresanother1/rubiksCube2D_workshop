import tensorflow as tf
import globals as glob
import right_side_rotate as right
import left_side_rotate as left
import top_rotate as top
import bottom_rotate as bottom

rubiks_cube_tensor = glob.rubiks_cube


def print_complete_rubiks_cube():
    # print page by page
    for page in range(0, 3):
        new_line_marker = 0
        for position in range(0, 9):
            if new_line_marker % 3 == 0:
                print("\r\n")
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

    # from here on, print line by line
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


def print_menu():
    print(glob.colors.OKGREEN + "rotate right side of the cube forward:         1")
    print("rotate right side of the cube backwards:       2")
    print("rotate left side of the cube forwards:         3")
    print("rotate left side of the cube backwards:        4")
    print("rotate top of the cube 90 degrees left:        5")
    print("rotate top of the cube 90 degrees right:       6")
    print("rotate bottom of the cube 90 degrees left:     7")
    print("rotate bottom of the cube 90 degrees right:    8")
    print("print the cube as a 2D net:                    9")
    print("Quit the game:                                 10" + glob.colors.ENDC)


def main():
    # print(rubiks_cube_tensor)
    print("Welcome to Rubiks Cube: ")
    print_complete_rubiks_cube()
    print_menu()
    user_input = input("Please enter a number for your actions: \r\n")

    run = True
    while run:
        if user_input == "1":
            right.rotate_cube_right_side_90_degrees_forwards(rubiks_cube_tensor)
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "2":
            right.rotate_cube_right_side_90_degrees_backwards(rubiks_cube_tensor)
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "3":
            left.rotate_cube_left_side_90_degrees_forwards(rubiks_cube_tensor)
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "4":
            left.rotate_cube_left_side_90_degrees_backwards(rubiks_cube_tensor)
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "5":
            top.rotate_cube_top_90_degrees_left(rubiks_cube_tensor)
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "6":
            top.rotate_cube_top_90_degrees_right(rubiks_cube_tensor)
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "7":
            bottom.rotate_cube_bottom_90_degrees_left(rubiks_cube_tensor)
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "8":
            bottom.rotate_cube_bottom_90_degrees_right(rubiks_cube_tensor)
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "9":
            print_complete_rubiks_cube()
            print_menu()
            user_input = input("Please enter a number for your actions: \r\n")

        elif user_input == "10":
            print(glob.colors.OKBLUE + "THANKS FOR PLAYING - HAVE A PLEASANT REST OF THE DAY" + glob.colors.ENDC)
            run = False

        else:
            user_input = input("Please choose a number shown in the menu (0 - 10) \r\n")


if __name__ == '__main__':
    main()
