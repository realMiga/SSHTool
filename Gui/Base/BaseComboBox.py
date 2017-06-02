import json

from PyQt5.QtWidgets import QComboBox


class BaseComboBox(QComboBox):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.parent = __args[0]

    @staticmethod
    def parseConfig(path):
        with open(path) as f:
            data = json.load(f)

        return data

    def setCss(self, style):
        styleFont = "QComboBox {"
        styleEnd = "}"
        template = '''%(key)s: %(value)s'''

        for k, v in style.items():
            s = template % {"key": k, "value": v}
            styleFont += s + ";"

        self.setStyleSheet(styleFont + styleEnd)

    def getText(self):
        return self.currentText()

    def setOnChangeEvent(self, event):
        self.currentIndexChanged.connect(event)

    def setItems(self, items):
        for i in range(0, len(items)):
            self.insertItem(i, items[i])