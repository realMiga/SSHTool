import json

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from Core.EventAction import EventAction


class BaseActivity(QMainWindow):
    def __init__(self, *__args):
        super().__init__(*__args)

    @staticmethod
    def parseConfig(path):
        with open(path) as f:
            data = json.load(f)

        return data

    def initWindow(self, title, width, height, resize=False):
        self.resize(width, height)
        self.setMinimumHeight(height)
        self.setMinimumWidth(width)
        self.setWindowTitle(title)

        if not resize:
            self.setMaximumHeight(height)
            self.setMaximumWidth(width)

    def setCss(self, style):
        styleFont = "QMainWindow {"
        styleEnd = "}"
        template = '''%(key)s: %(value)s'''

        for k, v in style.items():
            s = template % {"key": k, "value": v}
            styleFont += s + ";"

        self.setStyleSheet(styleFont + styleEnd)

    def createMenu(self, menus):
        for menu in menus:
            item = self.menuBar().addMenu(menu['name'])
            for subMenu in menu['subMenus']:
                action = EventAction(subMenu['text'], self)
                if subMenu['event'] is not "": action.setTriggered(eval(subMenu['event']))
                if subMenu['shortcut'] is not "": action.setShortcut(subMenu['shortcut'])
                if subMenu['status'] is not "": action.setStatusTip(subMenu['status'])
                item.addAction(action.push())

    def setIcon(self, path):
        self.setWindowIcon(QIcon(path))


