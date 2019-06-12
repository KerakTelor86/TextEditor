import tkinter as tk
from tkinter import ttk
from TextEditor import editor, fileio, statusbar
from pathlib import Path

if __name__ == '__main__':
    root = tk.Tk()
    # root.tk.call('tk', 'scaling', 1)
    root.title('Simple Text Editor')
    root.minsize(400,300)
    root.style = ttk.Style()
    root.style.theme_use('clam')

    texteditor = editor.Editor(root, 0, 0, '3 3 3 3', 2)
    texteditor.enable_resize()

    statusbar = statusbar.StatusBar(root, 0, 1, '3 0 3 3')
    statusbar.set_font('TkSmallCaptionFont')
    statusbar.set_status('Welcome!', 5000)

    fileio = fileio.FileIO(root, 1, 1, '3 3 3 3', texteditor.set_text, texteditor.get_text, statusbar.set_status)

    root.mainloop()