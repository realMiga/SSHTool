import json

from PyQt5.QtWidgets import QTreeView


class BaseTreeView(QTreeView):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.parent = __args[0]

    @staticmethod
    def parseConfig(path):
        with open(path) as f:
            data = json.load(f)

        return data

    def setCss(self, style):
        styleFont = "QTreeView {"
        styleEnd = "}"
        template = '''%(key)s: %(value)s'''

        for k, v in style.items():
            s = template % {"key": k, "value": v}
            styleFont += s + ";"

        self.setStyleSheet(styleFont + styleEnd)

    def setColumnsWidth(self, columnCount, widths):
        for i in range(0, columnCount):
            self.setColumnWidth(i, widths[i])
