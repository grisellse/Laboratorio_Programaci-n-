from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QFormLayout, QLabel)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

 
        central = QWidget()
        self.setCentralWidget(central)

        
        layout = QFormLayout()

      
        mascotas = ["Coco", "4 años", "Perro"],["Laika", "5 años", "Perro"], ["Tom", "2 años", "Gato"]

        

        for i in range(len(mascotas)):  
            layout.addRow(QLabel("Mascota "+  str(i+1) +":"))
            layout.addRow(QLabel(f"Nombre:{mascotas[i][0]}"))
            layout.addRow(QLabel(f"Edad:{mascotas[i][1]}"))
            layout.addRow(QLabel(f"Especie: {mascotas[i][2]}"))
            layout.addRow(QLabel("")) 

       
        central.setLayout(layout)


app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()