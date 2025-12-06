from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class Bienvenida(QWidget):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.setWindowTitle("Bienvenido")
        self.setGeometry(100, 100, 600, 500)#tamaño de la ventana
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
            }
            QLabel {
                font-size: 16px;
                color: #333;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 16px;
                border-radius: 6px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        # Imagen de bienvenida (opcional)
        self.logo = QLabel()
        pixmap = QPixmap("adiccion.png")  # Asegúrate de tener esta imagen
        if pixmap.isNull():
            self.logo.setText("🎮 Test de Adicción a Videojuegos")
            self.logo.setStyleSheet("font-size: 24px; font-weight: bold;")
        else:
            self.logo.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
        layout.addWidget(self.logo, alignment=Qt.AlignCenter)

        # Mensaje de bienvenida
        self.label_bienvenida = QLabel("¡Bienvenido al Test de Adicción a Videojuegos!")
        self.label_bienvenida.setFont(QFont("Arial", 18, QFont.Bold))
        self.label_bienvenida.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_bienvenida)

        self.label_instrucciones = QLabel("Este test te ayudará a evaluar tu relación con los videojuegos.\nPor favor, regístrate para continuar.")
        self.label_instrucciones.setAlignment(Qt.AlignCenter)
        self.label_instrucciones.setFont(QFont("Arial", 14))
        layout.addWidget(self.label_instrucciones)

        # Botón para continuar
        self.btn_continuar = QPushButton("Continuar")
        self.btn_continuar.clicked.connect(self.continuar)
        layout.addWidget(self.btn_continuar, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def continuar(self):
        self.close()
        self.callback()
