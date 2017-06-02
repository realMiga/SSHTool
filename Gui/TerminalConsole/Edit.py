from Core.EventAction import EventAction
from Gui.Base.BaseTextEdit import *

CONFIG_PATH = 'Config/Gui/TerminalConsole/Edit/'


class ConsoleEdit(BaseTextEdit):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "ConsoleEdit.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])

        if self.config['event'] is not "":
            action = EventAction("", self).setShortcut(self.config['shortcut']).setTriggered(eval(self.config['event']))
            action2 = EventAction("", self).setShortcut("Alt+Return").setTriggered(self.parent.newLine)
            self.addAction(action.push())
            self.addAction(action2.push())
