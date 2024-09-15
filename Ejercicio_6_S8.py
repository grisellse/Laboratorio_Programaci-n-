#Construir un programa que permita registrar y mostrar los datos de los
#pacientes usando estos widgets: radiobox, combobox y spinbox

#La funcionalidad que tiene este programa es que permite ingresar la información de un paciente, 
# como el nombre, la edad, el género, y se usan widgets para seleccionar los items

#El problema que resuelve este programa es que es útil para agilizar 
# la manera en que se hacen los registreos de los pacientes ya que solo se selcciona de manera 
# rapida.

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QRadioButton, QComboBox, QSpinBox
from PyQt5.QtCore import Qt
import sys

class Ventana_clinica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de pacientes")
        self.setGeometry(100, 100, 400, 300)

        # widgets
        self.nombre_label = QLabel("Nombre del paciente:")
        self.nombre = QLineEdit(self)

        self.edad_label = QLabel("Edad:")
        self.edad = QSpinBox(self)
        self.edad.setRange(1, 120)

        self.genero_label = QLabel("Genero:")
        self.masculino = QRadioButton("Masculino")
        self.femenino = QRadioButton("Femenino")

        self.consulta_label = QLabel("Tipo de consulta:")
        self.consulta = QComboBox(self)
        self.consulta.addItems(["general", "pediatria", "cardiologia", "otontologia"])

        self.medico_label = QLabel("Medico asignado:")
        self.medico = QComboBox(self)
        self.medico.addItems(["Dr. Rodriguez", "Dr.Morales", "Dr.Stark", "Dr.Martinez"])

        self.boton = QPushButton("Registrar", self)
        self.resultado = QLabel("", self)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre)
        layout.addWidget(self.edad_label)
        layout.addWidget(self.edad)
        layout.addWidget(self.genero_label)
        layout.addWidget(self.masculino)
        layout.addWidget(self.femenino)
        layout.addWidget(self.consulta_label)
        layout.addWidget(self.consulta)
        layout.addWidget(self.medico_label)
        layout.addWidget(self.medico)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        # conectar el boton 
        self.boton.clicked.connect(self.mostrar_datos)

        # establecer el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # colores de fondo
        self.setStyleSheet("background-color: #9ab9f8;")
        self.boton.setStyleSheet("background-color: #d4f4fd;")
        self.nombre.setStyleSheet("background-color: white;")
        self.edad.setStyleSheet("background-color: white;")
        self.consulta.setStyleSheet("background-color: white;")
        self.medico.setStyleSheet("background-color: white;")



    def mostrar_datos(self):
        nombre = self.nombre.text()
        edad = self.edad.value()

        if self.masculino.isChecked():
            genero = "Masculino"
        elif self.femenino.isChecked():
            genero = "Femenino"
        

        consulta = self.consulta.currentText()
        medico = self.medico.currentText()

        if nombre:
            self.resultado.setText(f"Nombre: {nombre}\nEdad: {edad}\nGenero: {genero}\nConsulta: {consulta}\nMedico asignado: {medico}")
        else:
            self.resultado.setText("ingrese el nombre del paciente!")

# ejecucion de la aplicación
app = QApplication(sys.argv)
ventana = Ventana_clinica()
ventana.show()
sys.exit(app.exec())
