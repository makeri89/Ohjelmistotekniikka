from tkinter import Tk, ttk, Canvas, StringVar, OptionMenu, Button, CENTER


class ScoreViewer:
    """A class to display the score history."""

    def __init__(self, score_repository, levels):
        """Initializes the tkinter window.

        Args:
            score_repository (ScoreRepository):
                Handles the database actions.
            levels: Available levels
        """
        self._score_repository = score_repository
        self._root = Tk()
        self._root.title('Scores')
        self._root['bg'] = '#99ff99'
        self._level = StringVar()
        self._levels = levels
        self._level.set(levels[0])

        self.add_items()

    def add_items(self, scores=None):
        """Creates the tkinter objects on the window.

        Args:
            scores: A list of sqlite row objects. Defaults to None.
        """
        row = 0
        headers = ['Level', 'Player', 'Score']
        self._canvas = Canvas(self._root, bg='#99ff99')
        self._canvas.pack()
        if scores is None:
            scores = self._score_repository.find_all()
        for i in range(3):
            label = ttk.Label(self._canvas,
                              text=headers[i],
                              background='#408040',
                              padding=8,
                              justify=CENTER,
                              borderwidth=5,
                              relief='sunken',
                              foreground='#fffff0')
            label.grid(row=row, column=i, padx=20, pady=10)

        row += 1

        if len(scores) == 0:
            empty_label = ttk.Label(self._canvas,
                                    text='No scores found with your search :(',
                                    background='#408040',
                                    foreground='#fffff0',
                                    padding=10)
            empty_label.grid(row=row, pady=20, columnspan=3)
            row += 1
        else:
            for i, datarow in enumerate(scores):
                for j, value in enumerate(datarow):
                    label = ttk.Label(self._canvas,
                                      text=value,
                                      background='#99ff99',
                                      padding=3,
                                      justify=CENTER)
                    label.grid(row=i+1, column=j, padx=20)
                row += 1

        self._name_entry = ttk.Entry(master=self._canvas)
        self._name_entry.grid(row=row, columnspan=2)
        name_button = Button(master=self._canvas,
                             text='Filter by player',
                             command=self.filter_by_name,
                             bg='#408040',
                             fg='#fffff0',
                             activebackground='#99ff99',
                             activeforeground='#408040',
                             bd=5,
                             relief='groove')
        name_button.grid(row=row, column=2, padx=5)

        row += 1

        level_dropdown = OptionMenu(
            self._canvas, self._level, *self._levels)
        level_dropdown.grid(row=row, column=1)
        level_button = Button(master=self._canvas,
                              text='Filter by level',
                              command=self.filter_by_level,
                              bg='#408040',
                              fg='#fffff0',
                              activebackground='#99ff99',
                              activeforeground='#408040',
                              bd=5,
                              relief='groove')
        level_button.grid(row=row, column=2, padx=5)

        button = Button(master=self._canvas,
                        text='Reset',
                        command=self.reset,
                        bg='#408040',
                        fg='#fffff0',
                        activebackground='#99ff99',
                        activeforeground='#408040',
                        bd=5,
                        relief='groove')
        button.grid(row=row, column=0, pady=10)

    def clear(self):
        """Clears the canvas but does not affect the root window."""
        self._canvas.destroy()

    def reset(self):
        """Resets the view to show all scores."""
        self.clear()
        self.add_items(self._score_repository.find_all())

    def filter_by_name(self):
        """Filters the results by name.

        Clears the current view first.
        """
        name = self._name_entry.get()
        self.clear()
        self.add_items(self._score_repository.find_all_by_player(name))

    def filter_by_level(self):
        """Filters the results by level.

        Clears the current view first.
        """
        self.clear()
        level = self._level.get()
        self.add_items(self._score_repository.find_all_by_level(level))

    def fire_up(self):
        """Starts the tkinter Tk mainloop to display the window."""
        self._root.mainloop()
