from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QFormLayout, QLabel)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        central = QWidget()
        self.setCentralWidget(central)

      
        layout = QFormLayout()

     
        Caracteristicas = ["Alto", "Responsable","Amable","Inteligente","Honesto","Puntual","Empatico","Paciente","Respetuoso","Tolerante"]

        
        for i in range(len(Caracteristicas)): 
          layout.addRow(QLabel("Característica " + str(i+1) + ":"), QLabel(Caracteristicas[i]))

       
        central.setLayout(layout)

app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()