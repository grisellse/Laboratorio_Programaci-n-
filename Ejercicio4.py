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

      #Se crea una lista con tres listas dentro de ella, una para cada mascota
        mascotas = ["Coco", "4 años", "Perro"],["Laika", "5 años", "Perro"], ["Tom", "2 años", "Gato"]

        
        #Se utiliza un for para iterar dentro de la lista principal y las sublistas para mostrar los datos de las 3 mascotas
        for i in range(len(mascotas)):  
            layout.addRow(QLabel("Mascota "+  str(i+1) +":"))
            layout.addRow(QLabel(f"Nombre:{mascotas[i][0]}"))
            layout.addRow(QLabel(f"Edad:{mascotas[i][1]}"))
            layout.addRow(QLabel(f"Especie: {mascotas[i][2]}"))
            layout.addRow(QLabel("")) 

       
        central.setLayout(layout)

#Se ejecuta la app
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()