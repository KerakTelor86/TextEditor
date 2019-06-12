import tkinter as tk
from tkinter import ttk

class StatusBar:
    def __init__(self, root, column, row, padding, columnspan=1, rowspan=1):
        self._frame = ttk.Frame(root, padding=padding)
        self._frame.grid(column=column, row=row, sticky='nwes', columnspan=columnspan, rowspan=rowspan)

        self._label = ttk.Label(self._frame)
        self._label.grid(column=0, row=0, sticky='nws')
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
        self._after_id = None
    
    def set_font(self, string):
        self._label['font'] = string
    
    def set_status(self, text, time = 0):
        try:
            self._label.after_cancel(self._after_id)
        except ValueError as e:
            pass
        self._label['text'] = text
        if time > 0:
            self._after_id = self._label.after(time, lambda: self.set_status('', 0))

    def get_status(self, text):
        return self._label['text']