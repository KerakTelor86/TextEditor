import tkinter as tk
from tkinter import ttk
from TextEditor import menu
from TextEditor import editor
from TextEditor import statusbar

if __name__ == '__main__':
    root = tk.Tk()
    # root.tk.call('tk', 'scaling', 1)
    root.title('Simple Text Editor')
    root.minsize(400,300)
    root.style = ttk.Style()
    root.style.theme_use('clam')
    root.option_add('*tearOff', False)

    menubar = menu.Menu(root)
    menubar.set_font('TkSmallCaptionFont')

    editor = editor.Editor(root)
    editor.render(0, 1, '3 3 3 3', 2)

    statusbar = statusbar.StatusBar(root)
    statusbar.render(0, 2, '3 0 3 3')
    statusbar.set_font('TkSmallCaptionFont')
    statusbar.set_status('Welcome!', 5000)

    root.mainloop()