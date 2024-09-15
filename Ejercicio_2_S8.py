#Construir un programa que muestre una ventana y que 
# lea una clave secreta sin mostrar los caracteres que lo componen.

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso de Usuario")
        self.setGeometry(100, 100, 300, 200)

        # Crear widgets
        self.usuario_label = QLabel("Nombre de Usuario:", self)
        self.usuario_input = QLineEdit(self)
        self.password_label = QLabel("Contraseña:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Ocultar la contraseña

        self.boton = QPushButton("Iniciar Sesion", self)
        self.resultado = QLabel("", self)

        # los colores de fondo de la ventana y el boton
        self.setStyleSheet("background-color: #f8e49a ;")
        self.boton.setStyleSheet("background-color:#f89a9a ; color: white;")

        # configuraramos los layuot
        layout = QVBoxLayout()
        layout.addWidget(self.usuario_label)
        layout.addWidget(self.usuario_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        # se conecta el boton 
        self.boton.clicked.connect(self.iniciar_sesion)

        # se configura la ventana principal
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def iniciar_sesion(self):
        usuario = self.usuario_input.text()
        password = self.password_input.text()
        if usuario and password:
            self.resultado.setText(f"Usuario: {usuario}\nla contraseña esta oculta 🤐 ")
            self.resultado.setAlignment(Qt.AlignCenter)
         
        else:
            self.resultado.setText("ingrese ambos campos (ಠ_ಠ)")

# mostrar la ventana
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec())
