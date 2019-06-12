import tkinter as tk
from tkinter import ttk
from TextEditor import menu
from TextEditor import editor
from TextEditor import statusbar
from TextEditor import fileio

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Simple Text Editor')
    root.minsize(400, 300)
    root.style = ttk.Style()
    root.style.theme_use('clam')
    root.option_add('*tearOff', False)

    curtab = tk.IntVar()

    editor = editor.Editor(root)
    editor.render(0, 1, '3 3 3 3', 2)

    fileman = fileio.FileIO(editor, statusbar)

    statusbar = statusbar.StatusBar(root)
    statusbar.render(0, 2, '3 0 3 3')
    statusbar.set_font('TkSmallCaptionFont')
    statusbar.set_status('Welcome!', 5000)

    fileman.set_statusbar(statusbar)

    menubar = menu.Menu(root, fileman, curtab)
    menubar.init_menu()
    menubar.set_font('TkSmallCaptionFont')

    root.bind('<Control-n>', fileman.newfile)
    root.bind('<Control-o>', fileman.openfile)
    root.bind('<Control-s>', fileman.savefile)

    root.mainloop()