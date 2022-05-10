import numpy as np

import globals as glob


rubiks_cube = glob.rubiks_cube


def print_complete_rubiks_cube():
    # initial setup rubiks cube

    # top 3 "pages" of the rubiks cube
    for page in range(0, 3):
       # print(rubiks_cube_array[color])
        newLineMarker = 0
        for position in range(0, 9):
           if newLineMarker % 3 == 0 :
            print("\r\n")

            '''pick the right color with extra spacing where needed'''
           if rubiks_cube[page][position][0] == 0:
               if rubiks_cube[page][position][1] == 0:
                   print("                 ", end=" ")
               print(glob.colors.BLUEBACKGROUND + "     " + glob.colors.ENDC, end=" ")
           elif rubiks_cube[page][position][0] == 1:
               if rubiks_cube[page][position][1] == 0:
                   print("                 ", end=" ")
               print(glob.colors.REDBACKGROUND + "     " + glob.colors.ENDC, end=" ")
           elif rubiks_cube[page][position][0] == 3:
               if rubiks_cube[page][position][1] == 0:
                   print("                 ", end=" ")
               print(glob.colors.ORANGENOWPINKBACKGROUND + "     " +glob.colors.ENDC, end=" ")
           elif rubiks_cube[page][position][0] == 2:
               if rubiks_cube[page][position][1] == 0:
                   print("                 ", end=" ")
               print(glob.colors.GREENBACKGROUND + "     " + glob.colors.ENDC, end=" ")
           elif rubiks_cube[page][position][0] == 4:
               if rubiks_cube[page][position][1] == 0:
                   print("                 ", end=" ")
               print(glob.colors.YELLOWBACKGROUND + "     " + glob.colors.ENDC, end=" ")
           elif rubiks_cube[page][position][0] == 5:
               if rubiks_cube[page][position][1] == 0:
                   print("                 ", end=" ")
               print(glob.colors.WHITEBACKGROUND + "     " + glob.colors.ENDC, end=" ")

           newLineMarker += 1


    print("\r\n")

    for page in range(3, 6):
        for position in range(0, 3):
           colorpicking(rubiks_cube[page][position][0])
    print("\r\n")
    for page in range(3,6):
        for position in range(3, 6):
           colorpicking(rubiks_cube[page][position][0])
    print("\r\n")
    for page in range(3, 6):
        for position in range(6, 9):
           colorpicking(rubiks_cube[page][position][0])

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
    save_color = np.array(rubiks_cube[4])
    print("save color array values: ")
    print(save_color)
    for pages in range(4,-1, -1):
        if pages == 3:
            continue
        else:
            
            if pages != 0:
                for position in range(0,9):
                    if (rubiks_cube[pages][position][1] == 2):
                        print("current color ")
                        print(rubiks_cube[pages][position])
                        print(rubiks_cube[pages-1][position])
                        if pages - 1 == 3:
                            number = rubiks_cube[pages-2][position][0]
                        else:
                            number = rubiks_cube[pages-1][position][0]
                        '''if (number == 0):
                            rubiks_cube[pages][position][0] = 3
                        else:'''
                        rubiks_cube[pages][position][0] = number
                       # print(number)
                        #rubiks_cube[pages][3][0] = number - 1
                        print("new color")
                        print(rubiks_cube[pages][position])
            else:
                for position in range(0,9):
                    if (rubiks_cube[pages][position][1] == 2):
                        print("current color ")
                        print(rubiks_cube[pages][position])
                        print(save_color[position])
                        rubiks_cube[pages][position][0] = save_color[position][0]



def main():
    print("Welcome to Rubiks Cube: ")
    print("rotate right side of the cube forward: 1")
    print("end game: 0")
    print_complete_rubiks_cube()
    #user_input = input("Please enter a number for your actions: ")
    user_input =1

    if user_input == 1:
        print_complete_rubiks_cube()
        rotate_cube_right_side_90_degrees_forwards()
        print_complete_rubiks_cube()
        #user_input = input("Please enter a number for your actions: ")


    rotate_cube_right_side_90_degrees_forwards()
    print_complete_rubiks_cube()

  #  print("after rotation 1")
   # print_complete_rubiks_cube()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

