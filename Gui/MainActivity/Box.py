from PyQt5.QtWidgets import QStyleOptionComboBox

from Gui.Base.BaseComboBox import BaseComboBox


CONFIG_PATH = 'Config/Gui/MainActivity/Box/'


class AuthMethodBox(BaseComboBox):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.config = self.parseConfig(CONFIG_PATH + "AuthMethodBox.json")

        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])
        self.setCss(self.config['css'])
        self.setItems(self.config['items'])
