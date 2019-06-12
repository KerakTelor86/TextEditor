from tkinter import filedialog

class FileIO:
    def __init__(self, textbox, statusbar=None):
        self._textbox = textbox
        self._statusbar = statusbar
    
    def set_textbox(self, textbox):
        self._textbox = textbox

    def set_statusbar(self, statusbar):
        self._statusbar = statusbar

    def openfile(self):
        try:
            file_ = filedialog.askopenfile(title='Open')
            self._textbox.set_text(file_.read())
            file_.close()
            if self._statusbar is not None:
                self._statusbar.set_status('Opened \'' + file_.name + '\'', 5000)
        except Exception as e:
            if self._statusbar is None:
                raise e
            else:
                self._statusbar.set_status('Failed to open file: ' + str(e), 5000)

    def savefile(self):
        try:
            file_ = filedialog.asksaveasfile(title='Save')
            file_.write(self._textbox.get_text())
            file_.close()
            if self._statusbar is not None:
                self._statusbar.set_status('Saved \'' + file_.name + '\'', 5000)
        except Exception as e:
            if self._statusbar is None:
                raise e
            else:
                self._statusbar.set_status('Failed to save file: ' + str(e), 5000)