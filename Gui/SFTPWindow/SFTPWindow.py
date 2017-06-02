from Gui.Base.BaseWidget import BaseWidget
from Gui.SFTPWindow.Tree import DirTree

CONFIG_PATH = 'Config/Gui/SFTPWindow/'


class SFTPWindow(BaseWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.client = parent.client

        self.config = self.parseConfig(CONFIG_PATH + 'SFTPWindow.json')
        self.initWindow(self.config['title'], self.config['width'], self.config['height'])
        self.setCss(self.config['css'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setIcon(self.config['icon'])

        self.tree = DirTree(self)