import tkinter as tk
from tkinter import ttk
from .fileio import *

class Menu:
    def __init__(self, root, fileio, tabvar):
        self._menu = tk.Menu(root)
        self._fileio = fileio
        self._tabvar = tabvar
        root['menu'] = self._menu

    def init_menu(self):
        self._file = tk.Menu(self._menu)
        self._menu.add_cascade(label='File', menu=self._file)
        # self._edit = tk.Menu(self._menu)
        # self._menu.add_cascade(label='Edit', menu=self._edit)
        # self._tabs = tk.Menu(self._menu)
        # self._menu.add_cascade(label='Tabs', menu=self._tabs)
        # self._options = tk.Menu(self._menu)
        # self._menu.add_cascade(label='Options', menu=self._options)

        # self._file.add_command(label='New')
        self._file.add_command(label='Open...', command=self._fileio.openfile)
        self._file.add_command(label='Save...', command=self._fileio.savefile)

    def set_font(self, string):
        self._menu.configure(font=string)

    # def add_tab(self):
    #     pass

    # def remove_tab(self):
    #     pass
        