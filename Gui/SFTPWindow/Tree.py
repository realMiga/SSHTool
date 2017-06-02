import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMenu

from Core.Helper import Helper
from Gui.Base.BaseMessageBox import BaseMessageBox
from Gui.Base.BaseTreeView import BaseTreeView
from Gui.Base.BsaeStandardItem import BaseStandardItem
from Gui.SFTPWindow.StandardItem import FolderItem, FileItem

CONFIG_PATH = 'Config/Gui/SFTPWindow/Tree/'
DOWNLOAD_PATH = "/".join(os.path.realpath(__file__).split("\\")[:-3]) + "/Downloads/"


class DirTree(BaseTreeView):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.client = self.parent.client

        self.config = self.parseConfig(CONFIG_PATH + 'DirTree.json')
        self.resize(self.config['width'], self.config['height'])
        self.move(self.config['position']['x'], self.config['position']['y'])

        self.root = FolderItem(self.config['root'])
        self.root.setStatusTip("No")

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(self.config['headerLabel'])
        self.model.appendRow(self.root)

        self.setModel(self.model)
        self.setColumnsWidth(len(self.config['headerLabel']), self.config['columnWidths'])

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)

        path = self.getPath("/")
        self.parsePath(self.root, path)
        self.doubleClicked.connect(self.doubleClick)

    def getPath(self, path):
        pathList = self.client.run("ls -la %s" % path).getResult()
        return pathList

    def parsePath(self, root, pathList):
        result = []
        for path in pathList[1:]:
            data = path[:-1].split(" ")
            if ".." == data[-1] or "." == data[-1]:
                continue
            u = []
            for d in data:
                if d:
                    u.append(d)
            result.append(u)
        for line in result:
            if line[0][0] == 'l':
                continue
            if line[0][0] == "d":
                item = FolderItem(line[8])
            else:
                item = FileItem(line[8])

            root.appendRow([item,
                            BaseStandardItem(line[2]),
                            BaseStandardItem(line[3]),
                            BaseStandardItem(Helper.formatSize(int(line[4]))),
                            BaseStandardItem(line[0][1:])
                            ])

    def doubleClick(self, index):
        item = self.selectedIndexes()[0].model().itemFromIndex(index)

        if item.statusTip() == 'No':
            return
        i = item
        path = ''
        while True:
            if i.parent() is not None:
                path += i.parent().text() + "/"
                i = i.parent()
            else:
                break

        path = "/".join(path.split("/")[::-1][1:])[1:]
        try:
            p = self.getPath(path + "/" + item.text())
            self.parsePath(item, p)
            item.setStatusTip("No")
        except:
            alertBox = BaseMessageBox("Alert", self)
            alertBox.setText("Permission Denied")
            alertBox.show()

    def openMenu(self, index):
        itemID = self.selectedIndexes()[0]
        item = self.selectedIndexes()[0].model().itemFromIndex(itemID)

        if item.text() == "/":
            return

        path = ''
        i = item
        while True:
            if i.parent() is not None:
                path += i.parent().text() + "/"
                i = i.parent()
            else:
                break
        dialog = BaseMessageBox("Status", self)

        path = "/".join(path.split("/")[::-1][1:])[1:]
        itemPath = path + '/' + item.text()

        def download():
            r = self.client.download(itemPath, DOWNLOAD_PATH)
            if r.Suc:
                dialog.setText("Success")
            else:
                dialog.setText(str(r.getError()))
            dialog.show()

        def upload():
            fileDialog = QFileDialog(self)
            file = fileDialog.getOpenFileName(caption="Choose File")[0]
            if not file:
                return
            r = self.client.upload(file, itemPath)
            if r.Suc:
                ''' Refresh Child Item '''
                item.removeRows(0, item.rowCount())
                self.parsePath(item, self.getPath(itemPath))
                dialog.setText("Success")
            else:
                dialog.setText(str(r.getError()))
            fileDialog.close()
            dialog.show()

        menu = QMenu()
        if isinstance(item, FileItem):
            menu.addAction("Download", download)
        elif isinstance(item, FolderItem):
            menu.addAction("Upload", upload)
        menu.exec_(self.viewport().mapToGlobal(index))
