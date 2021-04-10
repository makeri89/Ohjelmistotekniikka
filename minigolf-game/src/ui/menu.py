from tkinter import ttk, StringVar, OptionMenu
from levels.field_importer import get_keys


class Menu:
    """A class for the main menu from where you can start a new game.
    """

    def __init__(self, root, start_game):
        """A constructor to set the UI root

        Args:
            root: Tk window
        """
        self.root = root
        self.start_game = start_game
        self.entry = None
        self.levels = get_keys()
        self.clicked = StringVar()

    def start(self):
        """A method to set the windows elements.
        """
        label = ttk.Label(master=self.root, text='Play some minigolf')
        username_label = ttk.Label(master=self.root, text='Username: ')
        self.entry = ttk.Entry(master=self.root)
        button = ttk.Button(
            master=self.root, text='Start new game', command=self.handle_click)

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self.entry.grid(row=1, column=1, padx=10, pady=5)
        button.grid(row=3, column=0, columnspan=2, pady=5)

        self.clicked.set(self.levels[0])
        drop = OptionMenu(self.root, self.clicked, *self.levels)
        # drop.pack()
        drop.grid(row=2, column=1)

    def handle_click(self):
        """Starts the game when called.
        """
        self.start_game(self.entry.get(), self.clicked.get())
