from PyQt5.QtGui import QTextCursor

from Gui.Base.BaseWidget import BaseWidget
from Gui.TerminalConsole.Edit import *


class TerminalConsole(BaseWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.client = self.parent.client

        self.config = self.parseConfig('Config/Gui/TerminalConsole/TerminalConsole.json')
        self.initWindow(self.config['title'], self.config['width'], self.config['height'])
        self.setCss(self.config['css'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setIcon(self.config['icon'])

        self.consoleEdit = ConsoleEdit(self)
        self.consoleEdit.setText('%s@%s:%s$ ' % (self.client.user, self.client.host, self.client.curPath))
        self.consoleEdit.moveCursor(QTextCursor.End)

        self.tmpContent = self.consoleEdit.getText()

    def run(self):
        command = self.consoleEdit.getText().split("\n")[-1].split("$")[-1].strip()

        if command == 'exit':
            self.close()

        r = self.client.run(command)
        prompt_end = '%s@%s:%s$ ' % (self.client.user, self.client.host, self.client.curPath)
        content = ''
        result = r.getResult() if r.Suc else r.getError()
        if result:
            for line in result:
                content += line
        data = content + prompt_end

        self.consoleEdit.append(data)
        self.consoleEdit.moveCursor(QTextCursor.End)

        self.tmpContent = self.consoleEdit.toPlainText()

    def newLine(self):
        prompt = '%s@%s:%s$ ' % (self.client.user, self.client.host, self.client.curPath)
        self.consoleEdit.append(prompt)
