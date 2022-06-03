# rubiksCube2D_workshop
This is a little Rubik's Cube Manipulation Program that was created by me in regards to a workshop for university. The goal was to use the Tensorflow module and operate on tensors. 

# #Translating the Cube into 2D
The most important part was the translation of the 3D cube into the 2D tensor form, which could then be accessed by the program, implemented as a tf.Tensor Variable. 

'User Interaction'
After the script is started, the print\_menu() function is called and a while loop runs, containing an If/Elif statement, which selects the actions taken after the user inputs their choice, read by the input() function. The loop will continue unless the user selects to quit the script. 

# #Printing the Cube
The print\_complete\_rubiks\_cube() method starts with printing the first three pages in a loop as individual pages. In contrast, the second part was printed line by line, considering the third index of each entry within the main page as depicted in figure.  

# #Moving Parts of the Cube
For moving parts of the Rubik's Cube, i. e. rotating sides, top or bottom, it was necessary to decide, whether to only reassign the color values at the respective position or to reassign the complete Tensor of shape=(3) at each position. 
While solving the 3D Rubik's Cube relies on specific algorithms to move the individual squares themselves, this can be solved differently when using tensors. A page is considered individually and only the color values at the respective index are changed. 
