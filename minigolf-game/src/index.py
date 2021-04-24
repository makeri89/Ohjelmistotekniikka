from tkinter import Tk
from ui.menu import Menu
from main import main

window = Tk()
window.title('Main menu')
window['bg'] = '#13a713'

ui = Menu(window, main)
ui.initialize()

if __name__ == '__main__':
    window.mainloop()
    # main()
