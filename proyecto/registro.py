import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit,QVBoxLayout, QMessageBox, QStackedWidget, QTextEdit
from alumno import Alumno

class registro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("registro")
        self.setGeometry(200, 100, 400, 400)
        self.stacked = QStackedWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.stacked)
        self.setLayout(layout)
        self.pantalla_crear_cuenta()

#registro
    def pantalla_crear_cuenta(self):
        self.crear_cuenta = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Crear Cuenta"))
        self.input_correo = QLineEdit()
        self.input_contra = QLineEdit()
        self.input_contra.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Correo:"))
        layout.addWidget(self.input_correo)
        layout.addWidget(QLabel("Contraseña:"))
        layout.addWidget(self.input_contra)

        btn_registrar = QPushButton("Registrar")
        btn_registrar.clicked.connect(self.registrar_usuario)
        layout.addWidget(btn_registrar)
        self.crear_cuenta.setLayout(layout)
        self.stacked.addWidget(self.crear_cuenta)

    def registrar_usuario(self):
        correo = self.input_correo.text()
        contra = self.input_contra.text()
        if correo == "" or contra == "":
            QMessageBox.warning(self, "Error", "completa todos los campos")
        else:
            [correo] = contra
            QMessageBox.information(self, "Éxito", "Cuenta creada")
           
app = QApplication(sys.argv)
ventana = registro()
ventana.show()
sys.exit(app.exec_())