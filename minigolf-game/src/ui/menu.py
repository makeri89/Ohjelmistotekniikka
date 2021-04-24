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
        self.level = StringVar()
        self.ball_color = StringVar()
        self.colors = ['blue', 'green', 'red', 'yellow']

    def initialize(self):
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
        button.grid(row=4, column=0, columnspan=2, pady=5)

        self.level.set(self.levels[0])
        level_dropdown = OptionMenu(self.root, self.level, *self.levels)
        level_dropdown.grid(row=2, column=1)
        level_dropdown_label = ttk.Label(
            master=self.root, text='Pick a level: ')
        level_dropdown_label.grid(row=2, column=0, padx=10, pady=5)

        self.ball_color.set('blue')
        ball_dropdown = OptionMenu(self.root, self.ball_color, *self.colors)
        ball_dropdown.grid(row=3, column=1)
        ball_dropdown_label = ttk.Label(
            master=self.root, text='Choose ball color: ')
        ball_dropdown_label.grid(row=3, column=0, padx=10, pady=5)

    def handle_click(self):
        """Starts the game when called.
        """
        self.start_game(self.entry.get(), self.level.get(),
                        self.ball_color.get())
