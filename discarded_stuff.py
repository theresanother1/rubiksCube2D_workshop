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



#10.05

'''''''''

def rotate_cube_right_side_90_degrees_forwards():
    save_color = tf.Variable(rubiks_cube_tensor[4])
    save_side = tf.Variable(rubiks_cube_tensor[5])
    # print("save color array values: ")
    # print(save_color)
    for pages in range(5, -1, -1):
        if pages == 5:
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

        if pages == 3:
            continue
        if pages == 2 or pages == 1 or pages == 4:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][1] == 2:
                    # print("current color ")
                    # print(rubiks_cube_tensor[pages][position])
                    if pages - 1 == 3:
                        # print(rubiks_cube_tensor[pages-2][position])
                        # rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 2][position])
                        rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 2][position][0])
                        # print("new colors")
                        # print(rubiks_cube_tensor[pages][position])
                    else:
                        # print(rubiks_cube_tensor[pages - 1][position])
                        # rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 1][position])
                        rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 1][position][0])
                        # print("new colors")
                        # print(rubiks_cube_tensor[pages][position])

        elif pages == 0:
            # page is 0, meaning, page 0 gets the saved page 4 values
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][1] == 2:
                    print("current color ")
                    print(rubiks_cube_tensor[pages][position])
                    print(save_color[position])
                    rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])
                    # rubiks_cube_tensor[pages, position].assign(save_color[position])


def rotate_cube_right_side_90_degrees_backwards():
    save_color = tf.Variable(rubiks_cube_tensor[0])
    save_side = tf.Variable(rubiks_cube_tensor[5])
    # print("save color array values: ")
    # print(save_color)
    for pages in range(0, 6):
        if pages == 3:
            continue
        if pages == 5:
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
        if pages == 2 or pages == 1 or pages == 0:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][1] == 2:
                    # print("current color ")
                    # print(rubiks_cube[pages][position])
                    # print(rubiks_cube[pages + 1][position])

                    # avoid values from page 3, as they are not needed in this angle
                    if pages + 1 == 3:
                        rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages + 2][position][0])
                    else:
                        rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages + 1][position][0])
                    # print("new color")
                    # print(rubiks_cube[pages][position])
        elif pages == 4:
                # page is 4, meaning, page 4 gets the saved page 0 values
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 2:
                        # print("current color ")
                        # print(rubiks_cube_tensor[pages][position])
                        # print(save_color[position])
                        rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])


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
                            rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 2][position][0])
                        else:
                            rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 1][position][0])
            else:
                # page is 0, meaning, page 0 gets the saved page 4 values
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 0:
                        rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])

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
                            rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 2][position][0])
                        else:
                            rubiks_cube_tensor[pages, position, 0].assign(rubiks_cube_tensor[pages - 1][position][0])
            else:
                # page is 0, meaning, page 0 gets the saved page 4 values
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 0:
                        rubiks_cube_tensor[pages, position, 0].assign(save_color[position][0])

def rotate_cube_left_side_90_degrees_backwards():
    save_color = tf.Variable(rubiks_cube_tensor[0])
    for pages in range(0, 5):
        if pages == 3:
            continue
        else:
            # starting at page 0, page 4 will then get the values needed from save_color
            if pages != 4:
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 0:
                        # avoid values from page 3, as they are not needed in this angle
                        if pages + 1 == 3:
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages + 2][position])
                        else:
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages + 1][position])
            else:
                # page is 4, meaning, page 4 gets the saved page 0 values
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 0:
                        rubiks_cube_tensor[pages, position].assign(save_color[position])


def rotate_cube_left_side_90_degrees_backwards():
    save_color = tf.Variable(rubiks_cube_tensor[0])
    for pages in range(0, 5):
        if pages == 3:
            continue
        else:
            # starting at page 0, page 4 will then get the values needed from save_color
            if pages != 4:
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 0:
                        # avoid values from page 3, as they are not needed in this angle
                        if pages + 1 == 3:
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages + 2][position])
                        else:
                            rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages + 1][position])
            else:
                # page is 4, meaning, page 4 gets the saved page 0 values
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][1] == 0:
                        rubiks_cube_tensor[pages, position].assign(save_color[position])


def rotate_cube_top_90_degrees_left():
    save_color = tf.Variable(rubiks_cube_tensor[1])
    print(save_color)
    save_top = tf.Variable(rubiks_cube_tensor[2])
    print("top part of cube")
    print(save_top)
    for pages in range(1, 6):
        #print("for loop at " + str(pages))
        if pages == 2:
            positional_cnt1=6
            positional_cnt2=7
            positional_cnt3 = 8
            for position in range(0, 9):
                #print("cur val at position in red")
               #print(rubiks_cube_tensor[pages][position])
                #print("wanted val at position in red")
                #showVal = save_top[positional_cnt1]

                if rubiks_cube_tensor[pages][position][2] == 0:
                    #print(save_top[positional_cnt1])
                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt1][0])
                    positional_cnt1 = positional_cnt1 - 3
                    
                elif rubiks_cube_tensor[pages][position][2] == 1:

                    #print(save_top[positional_cnt2])
                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt2][0])#
                    positional_cnt2 = positional_cnt2 - 3

                elif rubiks_cube_tensor[pages][position][2] == 2:
                    #print(save_top[positional_cnt3])

                    rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt3][0])
                    positional_cnt3 = positional_cnt3 - 3

                #print("achieved val at position in red")
                #print(rubiks_cube_tensor[pages][position])

            #continue

        elif pages == 3 or pages == 4:
            for position1 in range(0, 9):
                if rubiks_cube_tensor[pages][position1][2] == 0:
                    # if pages + 1 == 2:
                    #   rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages + 2][position1][0])
                    # else:
                    # showVal = rubiks_cube_tensor[pages + 1][position1]
                    rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages + 1][position1][0])
        elif pages == 1:
            # print("blue page")
            # print(rubiks_cube_tensor[pages])
            x = 2
            for position2 in range(0, 9):
                if rubiks_cube_tensor[pages][position2][2] == 2:
                    # print("cur val at position in blue")
                    # print(rubiks_cube_tensor[pages][position2])
                    # print("wanted val at position in blue")
                    # showVal = rubiks_cube_tensor[pages + 2][x]
                    # print(showVal)
                    rubiks_cube_tensor[pages, position2, 0].assign(rubiks_cube_tensor[pages + 2][x][0])
                    x -= 1
                    # print("achieved val at position in blue")
                    # print(rubiks_cube_tensor[pages][position2])
                    # rubiks_cube_tensor[pages, position2, 0].assign(rubiks_cube_tensor[pages + 2][position2][0])
        elif pages == 5:
            # page is 5, meaning, page 5 gets the saved page 1 values
            x = 8
            for position3 in range(0, 9):
                # print("doing for loop for page 5 at position " + str(position3))
                # print(rubiks_cube_tensor[pages][position3])
                if rubiks_cube_tensor[pages][position3][2] == 0:  # place where new values need to be
                    # print(x)
                    # save_color[x][2] = 0
                    # show = save_color[x]

                    # print(show)
                    # reverseColor[x].assign()
                    rubiks_cube_tensor[pages, position3, 0].assign(save_color[x][0])
                    x -= 1


def rotate_cube_top_90_degrees_right():
    save_color = tf.Variable(rubiks_cube_tensor[5])
    print(save_color)
    save_top = tf.Variable(rubiks_cube_tensor[2])
    print("top part of cube")
    print(save_top)
    for pages in range(5, 0, -1):
        # top
        if pages == 2:
            if pages == 2:
                positional_cnt1 = 2
                positional_cnt2 = 1
                positional_cnt3 = 0
                for position in range(0, 9):
                    if rubiks_cube_tensor[pages][position][2] == 0:
                        rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt1][0])
                        positional_cnt1 = positional_cnt1 + 3

                    elif rubiks_cube_tensor[pages][position][2] == 1:
                        rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt2][0])  #
                        positional_cnt2 = positional_cnt2 + 3

                    elif rubiks_cube_tensor[pages][position][2] == 2:
                        rubiks_cube_tensor[pages, position, 0].assign(save_top[positional_cnt3][0])
                        positional_cnt3 = positional_cnt3 + 3

        # starting at page 0, page 4 will then get the values needed from save_color
        if pages != 1:
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 0:
                    # avoid values from page 3, as they are not needed in this angle
                    if pages - 1 == 2:
                        rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 2][position])
                    else:
                        rubiks_cube_tensor[pages, position].assign(rubiks_cube_tensor[pages - 1][position])
        else:
            # page is 5, meaning, page 5 gets the saved page 1 values
            for position in range(0, 9):
                if rubiks_cube_tensor[pages][position][2] == 0:
                    rubiks_cube_tensor[pages, position].assign(save_color[position])

        if pages == 4 or pages == 5:
            for position1 in range(0, 9):
                if rubiks_cube_tensor[pages][position1][2] == 0:
                    # if pages + 1 == 2:
                    #   rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages + 2][position1][0])
                    # else:
                    # showVal = rubiks_cube_tensor[pages + 1][position1]
                    rubiks_cube_tensor[pages, position1, 0].assign(rubiks_cube_tensor[pages - 1][position1][0])
                    print("new colorValue")
                    print(rubiks_cube_tensor[pages][position1])
        elif pages == 1:
            # print("blue page")
            # print(rubiks_cube_tensor[pages])
            x = 2
            for position2 in range(0, 9):
                if rubiks_cube_tensor[pages][position2][2] == 2:
                    # print("cur val at position in blue")
                    # print(rubiks_cube_tensor[pages][position2])
                    # print("wanted val at position in blue")
                    # showVal = rubiks_cube_tensor[pages + 2][x]
                    # print(showVal)
                    #rubiks_cube_tensor[pages, position2, 0].assign(rubiks_cube_tensor[pages - 2][x][0])
                    rubiks_cube_tensor[pages, position2, 0].assign(save_color[x][0])
                    x -= 1
                    # print("achieved val at position in blue")
                    # print(rubiks_cube_tensor[pages][position2])
                    # rubiks_cube_tensor[pages, position2, 0].assign(rubiks_cube_tensor[pages + 2][position2][0])
        elif pages == 3:
            # page is 5, meaning, page 5 gets the saved page 1 values
            x = 8
            for position3 in range(0, 9):
                # print("doing for loop for page 5 at position " + str(position3))
                # print(rubiks_cube_tensor[pages][position3])
                if rubiks_cube_tensor[pages][position3][2] == 0:  # place where new values need to be
                    # print(x)
                    # save_color[x][2] = 0
                    # show = save_color[x]

                    # print(show)
                    # reverseColor[x].assign()
                    rubiks_cube_tensor[pages, position3, 0].assign(rubiks_cube_tensor[pages - 2][x][0])
                    #rubiks_cube_tensor[pages, position3, 0].assign(save_color[x][0])
                    x -= 1



def rotate_cube_bottom_90_degrees_left():
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

