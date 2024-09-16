from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QFormLayout, QLabel)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,300,300)

        #Se crea la ventana principal
        central = QWidget()
        self.setCentralWidget(central)

       #Se crea el layout del formulario
        layout = QFormLayout()

        #Lista donde se almacenan las 10 caracteristicas
        Caracteristicas = ["Alto", "Responsable","Amable","Inteligente","Honesto","Puntual","Empatico","Paciente","Respetuoso","Tolerante"]

    #Ciclo for para iterar  sobre la lista de caracteristicas y crear 2 QLabel para que muestre cada caracteristica y el numero

        for i in range(len(Caracteristicas)): 
          layout.addRow(QLabel("Característica " + str(i+1) + ":"), QLabel(Caracteristicas[i]))

       
        central.setLayout(layout)
#Se ejecuta la app
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()