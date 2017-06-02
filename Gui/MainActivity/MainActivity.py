from Gui.Base.BaseActivity import BaseActivity
from Gui.Base.BaseMessageBox import BaseMessageBox
from Gui.MainActivity.Box import AuthMethodBox
from Gui.MainActivity.Button import *
from Gui.MainActivity.Edit import *
from Gui.MainActivity.Frame import *
from Gui.MainActivity.Label import *
from Core.SSHCore import *
from Gui.SFTPWindow.SFTPWindow import SFTPWindow
from Gui.TerminalConsole.TerminalConsole import TerminalConsole


class MainActivity(BaseActivity):
    def __init__(self):
        super().__init__()

        self.config = self.parseConfig('Config/Gui/MainActivity/MainActivity.json')
        self.initWindow(self.config['title'], self.config['width'], self.config['height'])
        self.setCss(self.config['css'])

        self.createMenu(self.config['menus'])
        self.statusbar = QStatusBar()
        self.statusbar.setStyleSheet("QStatusBar {color: white}")

        self.setStatusBar(self.statusbar)

        self.headerFrame = HeaderFrame(self)
        self.leftTopFrame = LeftTopFrame(self)
        self.leftMediumFrame = LeftMediumFrame(self)
        self.leftBottomFrame = LeftBottomFrame(self)



        SplLabel(self.headerFrame, x=20, y=0)
        self.sftpButton = SFTPButton(self.headerFrame)
        SplLabel(self.headerFrame, x=181, y=0)
        self.terminalButton = TerminalButton(self.headerFrame)
        SplLabel(self.headerFrame, x=367, y=0)

        self.headerLabel = ServerLabel(self.leftTopFrame)
        self.hostLabel = HostLabel(self.leftTopFrame)
        self.hostEdit = HostLineEdit(self.leftTopFrame)
        self.hostEdit.setFocus()
        self.portLabel = PortLabel(self.leftTopFrame)
        self.portEdit = PortLineEdit(self.leftTopFrame)


        self.authenticationLabel = AuthenticationLabel(self.leftMediumFrame)

        self.usernameLabel = UsernameLabel(self.leftMediumFrame)
        self.usernameEdit = UsernameLineEdit(self.leftMediumFrame)

        self.initialLabel = InitialLabel(self.leftMediumFrame)
        self.authMethodBox = AuthMethodBox(self.leftMediumFrame)
        self.authMethodBox.setOnChangeEvent(self.onAuthBoxChange)

        self.passwordLabel = PasswordLabel(self.leftMediumFrame)
        self.authEdit = AuthEdit(self.leftMediumFrame)


        self.checkBox = CheckBox(self.leftMediumFrame)

        self.connectButton = ConnectButton(self.leftBottomFrame)
        self.connectButton.clicked.connect(self.connectByPassword)
        self.connectButton.setShortcut("Return")

        self.terminalButton.clicked.connect(self.newTerminal)
        self.sftpButton.clicked.connect(self.newSFTP)

        self.client = None
        self.sftpWindow = None
        self.terminalConsole = None

        self.show()

    def connectByPassword(self):
        if self.client is None:
            try:
                host = self.hostEdit.getText()
                port = int(self.portEdit.getText())
                username = self.usernameEdit.getText()
                password = self.authEdit.getText()
            except Exception as e:
                self.statusbar.showMessage("Format Error" + str(e), 5000)
                return
            try:
                self.client = SSHClient(host, port, username, password=password)
                self.client.connect()
                self.statusbar.showMessage("Connect to %s" % host, 5000)
                self.connectButton.changeBackground()
                self.terminalConsole = TerminalConsole(self)
                self.sftpWindow = SFTPWindow(self)
            except Exception as e:
                self.statusbar.showMessage(str(e), 5000)
                if self.client is not None:
                    self.client.quit()
                    self.client = None
        else:
            self.client.quit()
            self.sftpWindow.close()
            self.terminalConsole.close()
            self.client = None
            self.connectButton.changeBackground()
            self.statusbar.showMessage("Disconnected", 5000)

    def connectByKey(self):
        if self.client is None:
            try:
                host = self.hostEdit.getText()
                port = int(self.portEdit.getText())
                username = self.usernameEdit.getText()
                key = self.authEdit.getText()
            except Exception as e:
                self.statusbar.showMessage("Format Error" + str(e), 5000)
                return
            try:
                self.client = SSHClient(host, port, username, key=key)
                self.client.connect()
                self.statusbar.showMessage("Connect to %s" % host, 5000)
                self.connectButton.changeBackground()
                self.terminalConsole = TerminalConsole(self)
                self.sftpWindow = SFTPWindow(self)
            except Exception as e:
                self.statusbar.showMessage(str(e), 5000)
                if self.client is not None:
                    self.client.quit()
                    self.client = None
        else:
            self.client.quit()
            self.sftpWindow.close()
            self.terminalConsole.close()
            self.client = None
            self.connectButton.changeBackground()
            self.statusbar.showMessage("Disconnected", 5000)


    def newTerminal(self):
        if self.terminalConsole is not None and self.client is not None:
            self.terminalConsole.show()
        else:
            self.statusbar.showMessage("Not connected any target.")


    def newSFTP(self):
        if self.sftpWindow is not None and self.client is not None:
            self.sftpWindow.show()
        else:
            self.statusbar.showMessage("Not connected any target.")

    def alertAbout(self):
        dialog = BaseMessageBox("Information", self)
        dialog.setText("   Verions: 0.1   \nAuthor: c0hb1rd   ")
        dialog.show()

    def onAuthBoxChange(self):
        text = self.authMethodBox.getText()
        if text == 'Password':
            self.authEdit.setText("")
            self.authEdit.setEchoMode(QLineEdit.Password)
            self.passwordLabel.setText("Password:")
            self.connectButton.clicked.connect(self.connectByPassword)
        else:
            self.passwordLabel.setText("PublicKey:")
            self.authEdit.setEchoMode(0)
            fileDialog = QFileDialog(self)
            file = fileDialog.getOpenFileName(caption="Choose File")[0]
            self.authEdit.setText(file)
            self.connectButton.clicked.connect(self.connectByKey)