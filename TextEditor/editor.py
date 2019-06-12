import tkinter as tk
from tkinter import ttk

class Editor:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(root)
        self._textbox = tk.Text(self._frame, wrap='none', undo='true')
        self._yscroll = ttk.Scrollbar(self._frame, orient='vertical', command=self._textbox.yview)
        self._xscroll = ttk.Scrollbar(self._frame, orient='horizontal', command=self._textbox.xview)
        self._textbox.configure(yscrollcommand=self._yscroll.set, xscrollcommand=self._xscroll.set)
        self._textbox.bind('<Tab>', self._tab)
        self._tab_spaces = 4

    def render(self, column, row, padding, columnspan=1, rowspan=1):
        self._frame['padding'] = padding
        self._frame.grid(column=column, row=row, sticky='nwes', columnspan=columnspan, rowspan=rowspan)
        self._root.columnconfigure(column, weight=1)
        self._root.rowconfigure(row, weight=1)
        self._textbox.grid(column=0, row=0, sticky='nwes')
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
        self._yscroll.grid(column=1, row=0, rowspan=2, sticky='nwes')
        self._xscroll.grid(column=0, row=1, sticky='nwes')
    
    def hide(self):
        for i in self._frame.grid_slaves():
            i.grid_forget()
        self._frame.grid_forget()

    def destroy(self):
        for i in self._frame.grid_slaves():
            i.destroy()
        self._frame.destroy()

    def set_tab_spaces(self, spaces):
        self._tab_spaces = spaces

    def get_tab_spaces(self):
        return self._tab_spaces

    def _tab(self, *args):
        self._textbox.insert(tk.INSERT, ' ' * self._tab_spaces)
        return 'break'

    def set_text(self, text):
        self._textbox.delete(1.0, tk.END)
        self._textbox.edit_reset()
        self._textbox.insert(1.0, text)

    def get_text(self):
        return self._textbox.get(1.0, tk.END)

    # def enable(self):
    #     pass
    # def disable(self):
    #     pass
    # def set_theme(self):
    #     pass
    # def set_padding(self):
    #     pass
    # def set_wrapping(self):
    #     pass
    # def set_font(self):
    #     pass
    # def get_font(self):
    #     pass