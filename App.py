import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('StegaText')

        self.setGeometry(10,10,800,600)

        self._createEditor()
        self._createMenu()

    def _createEditor(self):
        editor = QTextEdit()
        self.setCentralWidget(editor)
        
def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
