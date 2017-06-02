from PyQt5.QtWidgets import QAction


class EventAction:
    def __init__(self, text, content):
        self.action = QAction(text, content)

    def setShortcut(self, key):
        self.action.setShortcut(key)
        return self

    def setStatusTip(self, text):
        self.action.setStatusTip(text)
        return self

    def setTriggered(self, event):
        self.action.triggered.connect(event)
        return self

    def push(self):
        return self.action
