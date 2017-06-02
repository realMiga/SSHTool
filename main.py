#!/usr/bin/env python3
import sys

from PyQt5.QtWidgets import *

from Gui.MainActivity.MainActivity import MainActivity

"""

@Setup Environment:
    python3 -m pip install PyQt5 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

@Run:
    python3 main.py

"""

app = QApplication(sys.argv)

mainActivity = MainActivity()
#
#
# w = QWidget()
# b = QComboBox(w)
# b.insertItem(0, "Hello")
# b.insertItem(1, "BWorld")
# def test():
#     print(b.currentText())
# b.currentIndexChanged.connect(test)
# w.show()

sys.exit(app.exec_())
