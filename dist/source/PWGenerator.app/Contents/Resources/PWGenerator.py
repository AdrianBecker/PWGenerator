import random
import string

from mainWindow import *


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def action(size, lc, uc, num, sc):

    chars = ''

    if lc == True and uc == True:
        chars += string.ascii_letters
    if (lc == True or uc == True) and (lc == True and uc == True) == False:
        if lc == True:
            chars += string.ascii_letters
            x = slice(0, 26)
            chars = chars[x]
        else:
            chars += string.ascii_letters
            x = slice(26, 52)
            chars = chars[x]

    if num == True:
        chars += '0123456789'

    if sc == True:
        chars += string.punctuation

    return generate(size, chars)

def generate(size, chars):

    str = random_string_generator(size, chars)
    #print(str)
    #print(chars)
    return str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec_())
