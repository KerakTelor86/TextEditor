import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class FileIO:
    def __init__(self, root, column, row, padding, set_text, get_text, set_status=None, columnspan=1, rowspan=1):
        self._frame = ttk.Frame(root, padding=padding)
        self._frame.grid(column=column, row=row, sticky='nwes', columnspan=columnspan, rowspan=rowspan)

        self._text = ''
        self._openbutton = ttk.Button(self._frame, text='Open', command=lambda: self._openfile(set_text, set_status))
        self._openbutton.grid(column=1, row=0, sticky='nes')
        self._savebutton = ttk.Button(self._frame, text='Save', command=lambda: self._savefile(get_text, set_status))
        self._savebutton.grid(column=2, row=0, sticky='nes')
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)

    def _openfile(self, set_text, set_status):
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
    
    def _savefile(self, get_text, set_status):
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