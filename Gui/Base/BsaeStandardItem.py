from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QStandardItem


class BaseStandardItem(QStandardItem):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.setEditable(False)

    def setImage(self, path):
        self.setIcon(QIcon(path))




