import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Menu:
    def __init__(self, root):
        self._menu = tk.Menu(root)
        root['menu'] = self._menu

    def init_menu(self):
        self._file = tk.Menu(self._menu)
        self._menu.add_cascade(label='File', menu=self._file)
        self._edit = tk.Menu(self._menu)
        self._menu.add_cascade(label='Edit', menu=self._edit)
        self._tabs = tk.Menu(self._menu)
        self._menu.add_cascade(label='Tabs', menu=self._tabs)
        self._options = tk.Menu(self._menu)
        self._menu.add_cascade(label='Options', menu=self._options)

    def openfile(set_text, set_status):
        try:
            file_ = filedialog.askopenfile(title='Open')
            set_text(file_.read())
            file_.close()
            if set_status is not None:
                set_status('Opened \'' + file_.name + '\'', 5000)
        except Exception as e:
            if set_status is None:
                raise e
            else:
                set_status('Failed to open file: ' + str(e), 5000)

    def savefile(get_text, set_status):
        try:
            file_ = filedialog.asksaveasfile(title='Save')
            file_.write(get_text())
            file_.close()
            if set_status is not None:
                set_status('Saved \'' + file_.name + '\'', 5000)
        except Exception as e:
            if set_status is None:
                raise e
            else:
                set_status('Failed to save file: ' + str(e), 5000)

    def set_font(self, string):
        self._menu.configure(font=string)

    def add_tab(self):
        pass

    def remove_tab(self):
        pass
        