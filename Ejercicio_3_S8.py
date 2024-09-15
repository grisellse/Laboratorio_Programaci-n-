#Construir un programa que muestre una a través de la
#  cual se pueda leer su número de cédula y su nombre completo.

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cedula y nombre")
        self.setGeometry(100, 100, 300, 200)

        # widgets
        self.cedula = QLabel("Numero de cedula:", self)
        self.cedula_input = QLineEdit(self)
        self.cedula_input.setPlaceholderText("ingrese su numero de cedula")

        self.nombre = QLabel("Nombre completo:", self)
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText("Ingresa tu nombre completo")

        self.boton = QPushButton("Mostrar datos", self)
        self.resultado = QLabel("", self)

        # cplores de fondo
        self.setStyleSheet("background-color: #9ab9f8;")
        self.boton.setStyleSheet("background-color: #9ae3f8; color: black;")
        self.nombre_input.setStyleSheet("background-color: white;")
        self.cedula_input.setStyleSheet("background-color: white;")

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.cedula)
        layout.addWidget(self.cedula_input)
        layout.addWidget(self.nombre)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        # Conectar el boton
        self.boton.clicked.connect(self.mostrar_datos)

        # Configuraramos la ventana principal
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mostrar_datos(self):
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()
        if cedula and nombre:
            self.resultado.setText(f"Numero de cedula: {cedula}\nNombre completo: {nombre}")
            self.resultado.setAlignment(Qt.AlignCenter)
        else:
            self.resultado.setText("ingrese todos los datos (ಠ_ಠ)")

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec())
