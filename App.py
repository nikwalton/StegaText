'''GUI Imports'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from Steg import decode, encode


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('StegaText')

        self.setGeometry(10,10,800,600)

        self._createEditor()
        

    def _createEditor(self):
        editor = QTextEdit()
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        fileMenu = menu.addMenu('File')
        fileMenu.addAction('Encode Image File')
        fileMenu.addAction('Decode Image File')
        fileMenu.addSeparator()
        fileMenu.addAction('Encode Audio File')
        fileMenu.addAction('Decode Audio File')

        encryptMenu = menu.addMenu('Encryption')
        encryptMenu.addAction('Encrypt')
        encryptMenu.addAction('Decrypt')
        self.setCentralWidget(editor)
        editor.setText(decode('EncodedImage.png'))


def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
