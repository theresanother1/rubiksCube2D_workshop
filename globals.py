import numpy as np

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    BLUEBACKGROUND = '\033[104m'
    REDBACKGROUND = '\033[101m'
    ORANGENOWPINKBACKGROUND = '\033[105m'
    YELLOWBACKGROUND = '\033[103m'
    GREENBACKGROUND = '\033[102m'
    WHITEBACKGROUND = '\033[107m'
    EMPTYBACKGROUND = '\033[108m'

rubiks_cube = np.array([
        # orange now pink side
        [[3, 0, 0], [3, 1, 0], [3, 2, 0], [3, 0, 1], [3, 1, 1], [3, 2, 1], [3, 0, 2], [3, 1, 2], [3, 2, 2]],
        #blue side
        [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 0, 2], [0, 1, 2], [0, 2, 2]],
        #red side
        [[1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 0, 2], [1, 1, 2], [1, 2, 2]],
        # white side
        [[5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 0, 1], [5, 1, 1], [5, 2, 1], [5, 0, 2], [5, 1, 2], [5, 2, 2]],
        # green side
        [[2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 0, 1], [2, 1, 1], [2, 2, 1], [2, 0, 2], [2, 1, 2], [2, 2, 2]],
        # yellow side
        [[4, 0, 0], [4, 1, 0], [4, 2, 0], [4, 0, 1], [4, 1, 1], [4, 2, 1], [4, 0, 2], [4, 1, 2], [4, 2, 2]],

    ])