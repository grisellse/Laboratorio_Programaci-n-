#Construir un programa que muestre una ventana en la cual aparezca 
# su nombre completo y su edad centrados.

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos personales")
        self.setGeometry(100,200,300,300)

        
        # Widgets para campos de texto y boton
        self.nombre = QLineEdit(self)
        self.nombre.setPlaceholderText("Ingresa tu nombre")
        self.edad = QLineEdit(self)
        self.edad.setPlaceholderText("Ingresa tu edad")
        self.boton = QPushButton("Mostrar", self)
        self.mostrar = QLabel("", self)

        self.setStyleSheet("background-color: #cdb1e8;") 
        self.nombre.setStyleSheet("background-color: white; color: black;")
        self.edad.setStyleSheet("background-color: white;")
        self.boton.setStyleSheet("background-color: #cf81ec; color: white;")

        # los Layout
        layout = QVBoxLayout()
        layout.addWidget(self.nombre)
        layout.addWidget(self.edad)
        layout.addWidget(self.boton)
        layout.addWidget(self.mostrar)

        # se conecta el boton al metodo que muestra los datos
        self.boton.clicked.connect(self.mostrar_datos)

        # la ventana principal
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mostrar_datos(self):
        nombre = self.nombre.text()
        edad = self.edad.text()
        if nombre and edad.isdigit():
            self.mostrar.setText(f"Su nombre es: {nombre}\n y tiene: {edad} años")
            self.mostrar.setAlignment(Qt.AlignCenter)
        else:
            self.mostrar.setText("ingrese un nombre y una edad que sea valida ")


   # aqui se crea y muestra la aplicación
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec())
