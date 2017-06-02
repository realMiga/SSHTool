from Gui.Base.BaseLineEdit import BaseLineEdit


CONFIG_PATH = 'Config/Gui/MainActivity/Edit/'


class HostLineEdit(BaseLineEdit):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "HostEdit.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])


class PortLineEdit(BaseLineEdit):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "PortEdit.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])


class UsernameLineEdit(BaseLineEdit):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "UsernameEdit.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])


class AuthEdit(BaseLineEdit):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "AuthEdit.json")

        print(self.echoMode())
        self.setEchoMode(self.Password)
        print(self.echoMode())
        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])
        self.show()
