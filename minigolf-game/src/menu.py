from tkinter import Tk, ttk
from index import main as start_game


class UI:
    """A class for the main menu from where you can start a new game.
    """
    def __init__(self, root):
        """A constructor to set the UI root

        Args:
            root: Tk window
        """
        self.root = root

    def start(self):
        """A method to set the windows elements.
        """
        label = ttk.Label(master=self.root, text='Play some minigolf')
        username_label = ttk.Label(master=self.root, text='Username: ')
        entry = ttk.Entry(master=self.root)
        button = ttk.Button(
            master=self.root, text='Start new game', command=self.handle_click)

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        entry.grid(row=1, column=1, padx=10, pady=5)
        button.grid(row=2, column=0, columnspan=2, pady=5)

    def handle_click(self):
        """Starts the game when called.
        """
        start_game()


window = Tk()
window.title('Main menu')
window['bg'] = '#13a713'

ui = UI(window)
ui.start()

window.mainloop()
