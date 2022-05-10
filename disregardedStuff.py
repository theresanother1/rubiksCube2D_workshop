def test_rotate_cube_right_side_90_degrees_forwards_as_Tensors():
    #global rubiks_cube_tensor
    save_color = tf.Variable(rubiks_cube_tensor[4])
    print("save color array values: ")
    print(save_color)
    for pages in range(4,-1, -1):
        if pages == 3:
            continue
        else:
            # it only starts at page 4, because in our angle, green is up front = page 4, angle stays the same
            if pages != 0:
                for position in range(0,9):
                    if (rubiks_cube_tensor[pages][position][1] == 2):
                        print("current color ")
                        print(rubiks_cube_tensor[pages][position])
                       # print(rubiks_cube_tensor[pages-1][position])

                        # avoid values from page 3, as they are not needed in this angle
                        if pages - 1 == 3:
                            #print("working within tensor")
                            #number0 = rubiks_cube_tensor[pages - 2][position]
                            #number1 = rubiks_cube_tensor[pages - 2][position + 3]
                            #number2 = rubiks_cube_tensor[pages - 2][position+6]
                            print(rubiks_cube_tensor[pages-2][position])

                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages-2][position])
                            #index = [[pages, position], [pages, position+3], [pages, position+6]]
                            #print(index)
                            #update = [number0, number1, number2]
                            #print(update)
                            #tf.tensor_scatter_nd_update(rubiks_cube_tensor, index, update)
                            print("new colors")
                            print(rubiks_cube_tensor[pages][position])
                            #print(rubiks_cube_tensor)
                            #print("finished working within tensor")
                        else:
                            # print("working within tensor")
                            #number0 = rubiks_cube_tensor[pages - 2][position]
                            #number1 = rubiks_cube_tensor[pages - 2][position + 3]
                            #number2 = rubiks_cube_tensor[pages - 2][position + 6]
                            print(rubiks_cube_tensor[pages - 1][position])

                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 1][position])
                            # index = [[pages, position], [pages, position+3], [pages, position+6]]
                            # print(index)
                            # update = [number0, number1, number2]
                            # print(update)
                            # tf.tensor_scatter_nd_update(rubiks_cube_tensor, index, update)
                            print("new colors")
                            print(rubiks_cube_tensor[pages][position])

                            #number = rubiks_cube_tensor[pages - 1][position][0]
                            #print(rubiks_cube_tensor[pages][position-1][0])
                            #index = [[pages, position, 0]]
                            #update = [number]
                            #tf.tensor_scatter_nd_update(rubiks_cube_tensor, index, update)
                        '''if (number == 0):
                            rubiks_cube[pages][position][0] = 3
                        else:'''
                        #rubiks_cube[pages][position][0] = number
                       # print(number)
                        #rubiks_cube[pages][3][0] = number - 1
                        print("new color")
                        print(rubiks_cube_tensor[pages][position])
            else:
                # page is 0, meaning, page 0 gets the saved page 4 values
                for position in range(0,9):
                    if (rubiks_cube_tensor[pages][position][1] == 2):
                        print("current color ")
                        print(rubiks_cube_tensor[pages][position])
                        print(save_color[position])
                        rubiks_cube_tensor[pages, position].assign(save_color[position])
                       # index = [[pages, position, 0]]
                        #number = save_color[position][0]
                        #update = [number]
                        #tf.tensor_scatter_nd_update(rubiks_cube_tensor, index, update)

    #rubiks_cube_tensor = tf.convert_to_tensor(rubiks_cube)



def rotate_cube_right_side_90_degrees_forwards():
    global rubiks_cube_tensor
    save_color = np.array(rubiks_cube_tensor[4])
    print("save color array values: ")
    print(save_color)
    for pages in range(4,-1, -1):
        if pages == 3:
            continue
        else:
            # it only starts at page 4, because in our angle, green is up front = page 4, angle stays the same
            if pages != 0:
                for position in range(0,9):
                    if (rubiks_cube[pages][position][1] == 2):
                        print("current color ")
                        print(rubiks_cube[pages][position])
                        print(rubiks_cube[pages-1][position])

                        # avoid values from page 3, as they are not needed in this angle
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
                # page is 0, meaning, page 0 gets the saved page 4 values
                for position in range(0,9):
                    if (rubiks_cube[pages][position][1] == 2):
                        print("current color ")
                        print(rubiks_cube[pages][position])
                        print(save_color[position])
                        rubiks_cube[pages][position][0] = save_color[position][0]
    rubiks_cube_tensor = tf.convert_to_tensor(rubiks_cube)


def rotate_cube_right_side_90_degrees_backwards():
    global rubiks_cube_tensor
    save_color = np.array(rubiks_cube[0])
    print("save color array values: ")
    print(save_color)
    for pages in range(0,5):
        if pages == 3:
            continue
        else:
            # starting at page 0, page 4 will then get the values needed from save_color
            if pages != 4:
                for position in range(0, 9):
                    if rubiks_cube[pages][position][1] == 2:
                        print("current color ")
                        print(rubiks_cube[pages][position])
                        print(rubiks_cube[pages + 1][position])

                        # avoid values from page 3, as they are not needed in this angle
                        if pages + 1 == 3:
                            number = rubiks_cube[pages + 2][position][0]
                        else:
                            number = rubiks_cube[pages + 1][position][0]

                        rubiks_cube[pages][position][0] = number
                        # print(number)
                        # rubiks_cube[pages][3][0] = number - 1
                        print("new color")
                        print(rubiks_cube[pages][position])
            else:
                # page is 4, meaning, page 4 gets the saved page 0 values
                for position in range(0, 9):
                    if (rubiks_cube[pages][position][1] == 2):
                        print("current color ")
                        print(rubiks_cube[pages][position])
                        print(save_color[position])
                        rubiks_cube[pages][position][0] = save_color[position][0]
    rubiks_cube_tensor = tf.convert_to_tensor(rubiks_cube)

def rotate_cube_left_side_90_degrees_forwards():
    global rubiks_cube_tensor
    save_color = np.array(rubiks_cube[4])
    print("save color array values: ")
    print(save_color)
    for pages in range(4,-1, -1):
        if pages == 3:
            continue
        else:
            # it only starts at page 4, because in our angle, green is up front = page 4, angle stays the same
            if pages != 0:
                for position in range(0,9):
                    if (rubiks_cube[pages][position][1] == 0):
                        print("current color ")
                        print(rubiks_cube[pages][position])
                        print(rubiks_cube[pages-1][position])

                        # avoid values from page 3, as they are not needed in this angle
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
                # page is 0, meaning, page 0 gets the saved page 4 values
                for position in range(0,9):
                    if (rubiks_cube[pages][position][1] == 0):
                        print("current color ")
                        print(rubiks_cube[pages][position])
                        print(save_color[position])
                        rubiks_cube[pages][position][0] = save_color[position][0]
    rubiks_cube_tensor = tf.convert_to_tensor(rubiks_cube)



