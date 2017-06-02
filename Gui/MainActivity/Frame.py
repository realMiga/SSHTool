from Gui.Base.BaseFrame import BaseFrame


CONFIG_PATH = 'Config/Gui/MainActivity/Frame/'


class HeaderFrame(BaseFrame):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "HeaderFrame.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])


class LeftTopFrame(BaseFrame):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "LeftTopFrame.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])


class LeftBottomFrame(BaseFrame):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "LeftBottomFrame.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])


class LeftMediumFrame(BaseFrame):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "LeftMediumFrame.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])
