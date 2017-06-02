from PyQt5.QtWidgets import QMessageBox


class BaseMessageBox(QMessageBox):
    def __init__(self, title, *__args):
        super().__init__(*__args)

        self.hide()
        self.setWindowTitle(title)
