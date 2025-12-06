import sys
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QApplication,QLabel, QPushButton, QRadioButton, QButtonGroup, QMessageBox
from Pregunta import Pregunta

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")

        # Crear preguntas
        self.crearCuestionario()
        self.index = 0
        self.maximo = len(self.cuestionario)
        self.puntaje_total = 0

        # Widgets
        self.lb_num = QLabel("")
        self.lb_pregunta = QLabel("")

        # Opciones
        self.opcion_siempre = QRadioButton("Siempre")
        self.opcion_frecuente = QRadioButton("Frecuentemente")
        self.opcion_aveces = QRadioButton("A veces")
        self.opcion_nunca = QRadioButton("Nunca")

        # Grupo de opciones
        self.grupo_opciones = QButtonGroup()
        self.grupo_opciones.addButton(self.opcion_siempre)
        self.grupo_opciones.addButton(self.opcion_frecuente)
        self.grupo_opciones.addButton(self.opcion_aveces)
        self.grupo_opciones.addButton(self.opcion_nunca)

        # Botón siguiente
        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_siguiente.clicked.connect(self.siguiente)

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.lb_num, 0, 0)
        layout.addWidget(self.lb_pregunta, 1, 0)

        layout.addWidget(self.opcion_siempre, 2, 0)
        layout.addWidget(self.opcion_frecuente, 3, 0)
        layout.addWidget(self.opcion_aveces, 4, 0)
        layout.addWidget(self.opcion_nunca, 5, 0)

        layout.addWidget(self.btn_siguiente, 6, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Mostrar primera pregunta
        self.mostrarPregunta()

    def crearCuestionario(self):
        self.cuestionario = [
            Pregunta(1, "¿Cuánto tiempo pasas jugando videojuegos al día?", 0),
            Pregunta(2, "¿Has dejado de hacer tareas o labores por jugar?", 0),
            Pregunta(3, "¿Qué sientes cuando no puedes jugar?", 0),
            Pregunta(4, "¿Juegas incluso cuando sabes que deberías estar haciendo otra cosa importante?", 0),
            Pregunta(5, "¿Te cuesta detenerte cuando dices 'solo jugaré un rato'?", 0),
            Pregunta(6, "¿Has mentido a tu familia o amigos sobre cuánto tiempo juegas?", 0),
            Pregunta(7, "¿Prefieres jugar antes que salir con amigos o actividades sociales?", 0),
            Pregunta(8, "¿Los videojuegos son lo único que te hace sentir bien?", 0),
            Pregunta(9, "¿Has gastado dinero en videojuegos?", 0),
            Pregunta(10, "¿Cómo reaccionas si alguien te pide dejar de jugar?", 0),
            Pregunta(11, "¿Has perdido horas de sueño por seguir jugando?", 0),
            Pregunta(12, "¿Tu rendimiento ha bajado por jugar?", 0),
            Pregunta(13, "¿Te distraes pensando en videojuegos cuando no estás jugando?", 0),
            Pregunta(14, "¿Has intentado dejar de jugar sin lograrlo?", 0),
            Pregunta(15, "¿Los videojuegos son más importantes que tus relaciones personales?", 0)
        ]

    def mostrarPregunta(self):
        # Limpiar selección
        self.grupo_opciones.setExclusive(False)
        for btn in [self.opcion_siempre, self.opcion_frecuente, self.opcion_aveces, self.opcion_nunca]:
            btn.setChecked(False)                                                                                                                                                                                                                                                                
        self.grupo_opciones.setExclusive(True) 

        # Mostrar pregunta actual                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        pregunta = self.cuestionario[self.index]
        self.lb_num.setText(f"Pregunta {pregunta.num_pregunta}")
        self.lb_pregunta.setText(pregunta.texto)

    def obtenerPuntajeOpcion(self):
        if self.opcion_siempre.isChecked(): return 3
        if self.opcion_frecuente.isChecked(): return 2
        if self.opcion_aveces.isChecked(): return 1
        if self.opcion_nunca.isChecked(): return 0
        return None  # Nada seleccionado

    def siguiente(self):
        puntaje = self.obtenerPuntajeOpcion()

        if puntaje is None:
            QMessageBox.warning(self, "Advertencia", "Debes seleccionar una opción antes de continuar.")
            return

        # Guardar puntaje en la pregunta actual
        self.cuestionario[self.index].puntaje = puntaje
        self.puntaje_total += puntaje 

        # ¿Quedan preguntas?
        if self.index < self.maximo - 1:
            self.index += 1
            self.mostrarPregunta()
        else:
            self.finalizarTest()

    def finalizarTest(self):
        QMessageBox.information(
            self,
            "Resultado",
            f"Has finalizado el test.\n\nTu puntuación total es: {self.puntaje_total} puntos."
        )
        self.close()

app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()

