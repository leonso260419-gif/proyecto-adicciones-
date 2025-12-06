from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QDesktopServices

class RecursosEducativos(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Título
        self.label_recursos = QLabel("Recursos Educativos")
        self.label_recursos.setFont(QFont("Arial", 18, QFont.Bold))
        self.label_recursos.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_recursos)

        # Descripción
        self.label_descripcion = QLabel(
            "Aquí encontrarás videos y recursos para aprender más sobre la adicción a videojuegos y cómo manejarla:"
        )
        self.label_descripcion.setAlignment(Qt.AlignCenter)
        self.label_descripcion.setWordWrap(True)
        layout.addWidget(self.label_descripcion)

        # Contenedor con scroll para los enlaces
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: white; border: none;")

        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.setSpacing(10)

        recursos = [
    {
        "titulo": "¿Cómo saber si soy adicto a los videojuegos?",
        "url": "https://youtube.com/shorts/rlr_VdLXX_U?si=83ehGrFZaji25QBp",  # Cambia esta URL
        "descripcion": "Video explicativo sobre los signos de adicción a videojuegos."
    },
    {
        "titulo": "Consejos para reducir el tiempo de juego",
        "url": "https://youtube.com/shorts/mNrzsgF87g0?si=G2m5qz9tzs7nSEAD",  # Cambia esta URL
        "descripcion": "Estrategias prácticas para equilibrar el tiempo de juego."
    },
    {
        "titulo": "Adicción a videojuegos: testimonios reales",
        "url": "https://youtube.com/shorts/dvYrdh_84-w?si=-ItjE0BFCpPSzG3W",  # Cambia esta URL
        "descripcion": "Historias de personas que superaron su adicción."
    },
    
]

        for recurso in recursos:
            # Título del recurso (clickeable)
            label_titulo = QLabel(f"<a href='{recurso['url']}'>{recurso['titulo']}</a>")
            label_titulo.setStyleSheet("font-size: 16px; font-weight: bold; color: #3498db;")
            label_titulo.setOpenExternalLinks(True)
            label_titulo.linkActivated.connect(lambda url: QDesktopServices.openUrl(QUrl(url)))
            container_layout.addWidget(label_titulo)

            # Descripción
            label_desc = QLabel(recurso["descripcion"])
            label_desc.setStyleSheet("font-size: 14px; color: #555;")
            label_desc.setWordWrap(True)
            container_layout.addWidget(label_desc)

        container.setLayout(container_layout)
        scroll.setWidget(container)
        layout.addWidget(scroll)

        self.setLayout(layout)
