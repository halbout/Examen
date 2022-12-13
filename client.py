from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox
import socket

class Client(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        lab1 = QLabel("Serveur")
        lab2 = QLabel("Port")
        lab3 = QLabel("Message: ")
        self.__serveur = QLineEdit("")
        self.__port = QLineEdit("")
        message = QLineEdit("")
        echange = QTextEdit("")
        echange.setReadOnly(True)
        self.__connexion = QPushButton("Connexion")
        self.__envoyer = QPushButton("Envoyer")
        effacer = QPushButton("Effacer")
        quitter = QPushButton("Quitter")

        grid.addWidget(lab1, 0, 0)
        grid.addWidget(self.__serveur, 0, 1)
        grid.addWidget(lab2, 1, 0)
        grid.addWidget(self.__port, 1, 1)
        grid.addWidget(self.__connexion, 2, 0)
        grid.addWidget(echange, 3, 0)
        grid.addWidget(lab3, 4, 0)
        grid.addWidget(message, 4, 1)
        grid.addWidget(self.__envoyer, 5, 0)
        grid.addWidget(effacer, 6, 0)
        grid.addWidget(quitter, 6, 1)

        quitter.clicked.connect(self.__actionQuit)
        self.setWindowTitle("Un logiciel de tchat")
        self.__connexion.clicked.connect(self.__actionConn)
        self.__envoyer.clicked.connect(self.__actionEnvoie)

    def __actionQuit(self, _e: QCloseEvent):
        box = QMessageBox()
        box.setWindowTitle("Quitter")
        box.setText("Voulez vous quitter ?")
        box.addButton(QMessageBox.Yes)
        box.addButton(QMessageBox.No)

        ret = box.exec()

        if ret == QMessageBox.Yes:
            QCoreApplication.exit(0)
        else:
            _e.ignore()

    def __actionEnvoie(self):
        if self.__connexion.text == "Connexion":
            self.__envoyer.setEnabled(False)
        else:
            self.__envoyer.setEnabled(True)

    def __actionConn(self):
        data = ""
        client = socket.socket()
        client.connect((self.__serveur, self.__port))
        while client.connect == True :
            data = client.recv(1024).decode()
            data.setAlignment(Qt.AlignLeft)
