'''GUI Imports'''
import sys
from PyQt5.QtCore import QFile, QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''Other Scripts Imports'''
from Steg import decode, encode

'''Cryptography'''
from cryptography.fernet import Fernet

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('StegaText')

        self.setGeometry(10,10,800,600)
        
        self._createEditor()
        

    def _createEditor(self):
        self.editor = QTextEdit()
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        self.setCentralWidget(self.editor)

        #Set up connection for encoding images 
        encodeImageAction = QAction('&Encode Image', self)
        encodeImageAction.setStatusTip('Encode text into a image')
        encodeImageAction.triggered.connect(self.encodeImage)
        #Set up connection for decoding images
        decodeImageAction = QAction('&Decode Image', self)
        decodeImageAction.setStatusTip('Decode a image into text')
        decodeImageAction.triggered.connect(self.decodeImage)
        #Set up connection for encoding audio
        encodeAudioAction = QAction('&Encode Audio', self)
        encodeAudioAction.setStatusTip('Encode text into an audio file')
        encodeAudioAction.triggered.connect(self.encodeAudio)
        #Set up connection for decoding audio
        decodeAudioAction = QAction('&Decode Audio', self)
        decodeAudioAction.setStatusTip('Decode audio into text')
        decodeAudioAction.triggered.connect(self.decodeAudio)
        #Set up connection for encryption
        encryptAction = QAction('&Encrypt Text', self)
        encryptAction.setStatusTip('Encrypt the text using symmetric key encryption')
        encryptAction.triggered.connect(self.encryptHelper)
        #set up connection for decryption
        decryptAction = QAction('&Decrypt Text', self)
        decryptAction.setStatusTip('Decrypt the text using symmetric key decryption')
        decryptAction.triggered.connect(self.decryptHelper)

        fileMenu = menu.addMenu('File')
        fileMenu.addAction(encodeImageAction)
        fileMenu.addAction(decodeImageAction)
        fileMenu.addSeparator()
        fileMenu.addAction(encodeAudioAction)
        fileMenu.addAction(decodeAudioAction)

        encryptMenu = menu.addMenu('Encryption')
        encryptMenu.addAction(encryptAction)
        encryptMenu.addAction(decryptAction)

 

    def encodeImage(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Image File")
        print(file)
        url = QUrl.fromLocalFile(file)

        encode(url.fileName(), self.editor.toPlainText()) 

    def decodeImage(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Encoded Image File")
        url = QUrl.fromLocalFile(file)
        self.editor.setText(decode(url.fileName()))

    def encodeAudio(self):
        print('Encode Audio')
    
    def decodeAudio(self):
        print('Decode Audio')

    def encryptHelper(self):
        print('encrypt text')

        # if theres nothing to encrypt dont bother
        if self.editor.toPlainText() != '':
            # generate new key using the cryptography package
            key = Fernet.generate_key()
            print(key)
            print(type(key))
            # instanciate the fernet class
            fernet = Fernet(key)
            # get text form the text box
            text = self.editor.toPlainText()
            
            # perform the encryption
            encryptedText = fernet.encrypt(text.encode())
            #output the results
            self.editor.clear()
            self.editor.setText(encryptedText.decode('utf-8'))
        
            # give the user their key
            message = QMessageBox()
            message.setText("This is your key for decryption please save this in a safe place.")
            message.setInformativeText(key.decode('utf-8'))
            message.setWindowTitle("Encrypt")

            message.exec_()
        else:
            message = QMessageBox()
            message.setText("No text to encrypt")
            message.setWindowTitle("Encryption Error")
            message.exec_()

        

    def decryptHelper(self):
        print('decrypt text')

        if self.editor.toPlainText() != '':
            key = QInputDialog.getText(self, 'Decrypt Text', 'Enter your key below')
        
            bytesKey = bytes(key[0], 'utf-8')

            fernet = Fernet(bytesKey)

            encryptedText = self.editor.toPlainText()
            bytesText = bytes(encryptedText, 'utf-8')
            decodeText = fernet.decrypt(bytesText).decode()

            self.editor.clear()
            self.editor.setText(decodeText)
        else:
            message = QMessageBox()
            message.setText("No text do decrypt")
            message.setWindowTitle("Decryption Error")
            message.exec_()




def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
