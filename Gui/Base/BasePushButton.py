import json

import time
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *


class PushButton(QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.on = None
        self.off = None
        self.parent = __args[0]
        self.statusFlag = True

    @staticmethod
    def parseConfig(path):
        with open(path) as f:
            data = json.load(f)

        return data

    def initImage(self, on, off):
        self.on = on
        self.off = off

    def initColor(self, on, off):
        self.on = on
        self.off = off

    def setCss(self, style, append=None):
        styleFont = "QPushButton {"
        styleEnd = "}"
        template = '''%(key)s: %(value)s'''

        for k, v in style.items():
            s = template % {"key": k, "value": v}
            styleFont += s + ";"

        if not append:
            self.setStyleSheet(styleFont + styleEnd)
        else:
            self.setStyleSheet(styleFont + styleEnd + append)

    def changeBackground(self):
        if self.statusFlag:
            self.setBackground(self.on)
            self.statusFlag = False
        else:
            self.setBackground(self.off)
            self.statusFlag = True

    def changeColor(self):
        if self.statusFlag:
            self.setColor(self.on)
            self.statusFlag = False
        else:
            self.setColor(self.off)
            self.statusFlag = True

    def setBackground(self, path):
        bImage = QImage(path)
        palette = QPalette()
        palette.setBrush(QPalette.Button, QBrush(bImage))
        self.setPalette(palette)

    def setColor(self, color):
        config = self.config['css']
        config['background'] = color
        self.setCss(config)
