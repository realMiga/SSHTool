import json

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFrame


class BaseFrame(QFrame):
    def __init__(self, *__args):
        super().__init__(*__args)

    @staticmethod
    def parseConfig(path):
        with open(path) as f:
            data = json.load(f)

        return data

    def setCss(self, style):
        styleFont = "QFrame {"
        styleEnd = "}"
        template = '''%(key)s: %(value)s'''

        for k, v in style.items():
            s = template % {"key": k, "value": v}
            styleFont += s + ";"

        self.setStyleSheet(styleFont + styleEnd)

    def setIcon(self, path):
        self.setWindowIcon(QIcon(path))
