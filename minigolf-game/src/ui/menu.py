from tkinter import Tk, ttk, StringVar, OptionMenu, Button, CENTER

from levels.field_importer import get_keys


class Menu:
    """A class for the main menu from where you can start a new game.

    Attributes:
        start_game: The main function to start the game.
        score_table: A function to open the score histroy view.
    """

    def __init__(self, start_game, score_table):
        """A constructor to set the UI root.

        Args:
            start_game: The main function to start the game.
            score_table: ScoreViewer class to see score history.
        """
        self._root = Tk()
        self.start_game = start_game
        self._entry = None
        self._levels = get_keys()
        self._level = StringVar()
        self._ball_color = StringVar()
        self._colors = ['blue', 'green', 'red', 'yellow']
        self.score_table = score_table

        self._root.title('Main menu')
        self._root['bg'] = '#99ff99'

    def initialize(self):
        """Initializes the tkinter elements."""
        label = ttk.Label(master=self._root,
                          text='Play some minigolf',
                          background='#408040',
                          justify=CENTER,
                          foreground='#fffff0',
                          padding=5,
                          borderwidth=5,
                          relief='sunken')
        username_label = ttk.Label(master=self._root,
                                   text='Username: ',
                                   background='#408040',
                                   justify=CENTER,
                                   foreground='#fffff0',
                                   padding=5,
                                   borderwidth=5,
                                   relief='sunken')
        self._entry = ttk.Entry(master=self._root)
        button = Button(master=self._root,
                        text='Start new game',
                        command=self.handle_click,
                        bg='#408040',
                        fg='#fffff0',
                        activebackground='#99ff99',
                        activeforeground='#408040',
                        bd=5,
                        relief='groove')

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._entry.grid(row=1, column=1, padx=10, pady=5)
        button.grid(row=4, column=1, pady=5)

        self._level.set(self._levels[0])
        level_dropdown = OptionMenu(self._root, self._level, *self._levels)
        level_dropdown.grid(row=2, column=1)
        level_dropdown_label = ttk.Label(master=self._root,
                                         text='Pick a level: ',
                                         background='#408040',
                                         justify=CENTER,
                                         foreground='#fffff0',
                                         padding=5,
                                         borderwidth=5,
                                         relief='sunken')
        level_dropdown_label.grid(row=2, column=0, padx=10, pady=5)

        self._ball_color.set('blue')
        ball_dropdown = OptionMenu(self._root, self._ball_color, *self._colors)
        ball_dropdown.grid(row=3, column=1)
        ball_dropdown_label = ttk.Label(master=self._root,
                                        text='Choose ball color: ',
                                        background='#408040',
                                        justify=CENTER,
                                        foreground='#fffff0',
                                        padding=5,
                                        borderwidth=5,
                                        relief='sunken')
        ball_dropdown_label.grid(row=3, column=0, padx=10, pady=5)

        table_button = Button(master=self._root,
                              text='View score history',
                              command=self.score_table,
                              bg='#408040',
                              fg='#fffff0',
                              activebackground='#99ff99',
                              activeforeground='#408040',
                              bd=5,
                              relief='groove')
        table_button.grid(row=4, column=0, padx=10)

    def handle_click(self):
        """Starts the game when called."""
        self.start_game(self._entry.get(), self._level.get(),
                        self._ball_color.get())

    def run(self):
        """Starts the tkinter menu."""
        self.initialize()
        self._root.mainloop()
