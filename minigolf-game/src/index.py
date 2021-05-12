from ui.menu import Menu
from ui.score_table import open_table
from services.main import main

ui = Menu(main, open_table)

if __name__ == '__main__':
    ui.run()
