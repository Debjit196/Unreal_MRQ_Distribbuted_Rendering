# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
import client_node_receive
import threading
class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.load_ui()
        self.setWindowTitle("Viga Distributed Rendering Client Manager")
        self.setGeometry(123, 461,400,200)
        self.setFixedSize(400,200)
        self.widget.startButton.clicked.connect(self.startServer)
    def startServer(self):
        t=threading.Thread(target=client_node_receive.run,kwargs={'port':int(self.widget.port_textBox.text())})
        t.setDaemon(True)
        t.start()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.widget=loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = mainwindow()
    widget.show()
    sys.exit(app.exec_())
