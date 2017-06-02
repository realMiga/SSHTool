from Gui.Base.BasePushButton import *


CONFIG_PATH = "Config/Gui/MainActivity/Button/"


class ConnectButton(PushButton):
    def __init__(self, *args):
        super().__init__(*args)

        self.config = self.parseConfig(CONFIG_PATH + "ConnectButton.json")
        self.statusFlag = False

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])
        self.initImage(self.config['on'], self.config['off'])
        self.setBackground(self.config['on'])
        # self.setStatusTip(self.config['status'])

        self.setFlat(True)
        self.setAutoFillBackground(True)


class SFTPButton(PushButton):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "SFTPButton.json")

        self.statusFlag = False

        self.setText(self.config['text'])
        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'], self.config['append'])
        self.setStatusTip(self.config['status'])

        self.setFlat(True)
        self.setAutoFillBackground(True)


class TerminalButton(PushButton):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "TerminalButton.json")

        self.statusFlag = False

        self.setText(self.config['text'])
        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'], self.config['append'])
        self.setStatusTip(self.config['status'])

        self.setFlat(True)
        self.setAutoFillBackground(True)
