from Gui.Base.BaseLabel import BaseLabel


CONFIG_PATH = 'Config/Gui/MainActivity/Label/'


class AuthenticationLabel(BaseLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "AuthenticationLabel.json")

        self.resize(config['width'], config['height'])
        self.move(config['position']['x'], config['position']['y'])
        self.setText(config['text'])
        self.setCss(config['css'])


class CheckBox(BaseLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "CheckBox.json")

        self.resize(config['width'], config['height'])
        self.move(config['position']['x'], config['position']['y'])
        self.setText(config['text'])
        self.setCss(config['css'])


class HostLabel(BaseLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "HostLabel.json")

        self.resize(config['width'], config['height'])
        self.move(config['position']['x'], config['position']['y'])
        self.setText(config['text'])
        self.setCss(config['css'])


class InitialLabel(BaseLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "InitialLabel.json")

        self.resize(config['width'], config['height'])
        self.move(config['position']['x'], config['position']['y'])
        self.setText(config['text'])
        self.setCss(config['css'])


class PasswordLabel(BaseLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "PasswordLabel.json")

        self.resize(config['width'], config['height'])
        self.move(config['position']['x'], config['position']['y'])
        self.setText(config['text'])
        self.setCss(config['css'])


class PortLabel(BaseLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "PortLabel.json")

        self.resize(config['width'], config['height'])
        self.move(config['position']['x'], config['position']['y'])
        self.setText(config['text'])
        self.setCss(config['css'])


class ServerLabel(BaseLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "ServerLabel.json")

        self.resize(config['width'], config['height'])
        self.move(config['position']['x'], config['position']['y'])
        self.setText(config['text'])
        self.setCss(config['css'])


class UsernameLabel(BaseLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "UsernameLabel.json")

        self.resize(config['width'], config['height'])
        self.move(config['position']['x'], config['position']['y'])
        self.setText(config['text'])
        self.setCss(config['css'])


class SplLabel(BaseLabel):
    def __init__(self, *__args, x, y):
        super().__init__(*__args)

        config = self.parseConfig(CONFIG_PATH + "SplLabel.json")

        self.resize(config['width'], config['height'])
        self.move(x, y)
        self.setText(config['text'])
        self.setCss(config['css'])
