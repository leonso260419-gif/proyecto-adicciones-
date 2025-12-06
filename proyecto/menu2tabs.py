import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel,QTabWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QRadioButton, QButtonGroup, QHBoxLayout, QFileDialog, QScrollArea
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QDesktopServices
from Pregunta import Pregunta

# Función para validar correo electrónico
def validar_email(email):
    """
    Valida si un correo electrónico tiene un formato válido.
    Patrón de validación:
    - Debe contener un solo @
    - Dominio debe tener al menos un punto
    - No puede empezar ni terminar con punto o @
    - No puede contener caracteres especiales no permitidos
    - Debe tener al menos un carácter antes y después del @
    - La parte después del @ debe tener al menos un punto
    - La parte después del último punto debe tener 2-6 caracteres
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
    return re.match(patron, email) is not None
#Clase Resultados para mostrar los resultados del test
class Resultados(QWidget):
    def __init__(self, puntaje_total, cuestionario):
        super().__init__()
        self.puntaje_total = puntaje_total
        self.cuestionario = cuestionario
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Etiqueta de puntaje
        self.lb_info = QLabel(f"Puntaje total obtenido: {self.puntaje_total}")
        self.lb_info.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        self.lb_info.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lb_info)

        # Recomendaciones
        self.lb_recomendacion = QLabel(self.obtener_recomendacion())
        self.lb_recomendacion.setStyleSheet("font-size: 14px; color: #34495e;")
        self.lb_recomendacion.setWordWrap(True)
        self.lb_recomendacion.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lb_recomendacion)

        # Gráfica
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
        self.fig = Figure(figsize=(5, 4))
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.graficar()

        # Botón para guardar resultados
        self.btn_guardar = QPushButton("Guardar Resultados")
        self.btn_guardar.setStyleSheet("background-color: #3498db;")
        self.btn_guardar.clicked.connect(self.guardar_resultados)
        layout.addWidget(self.btn_guardar, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def obtener_recomendacion(self):
        if self.puntaje_total <= 15:
            return " Tu relación con los videojuegos es saludable. Sigue así y equilibra tu tiempo con otras actividades."
        elif 16 <= self.puntaje_total <= 30:
            return " Parece que los videojuegos están tomando más tiempo del recomendado. Intenta reducir tu tiempo de juego y busca otras actividades."
        else:
            return " Tu puntuación indica una posible adicción. Te recomendamos buscar ayuda profesional y reducir drásticamente tu tiempo de juego."

    def graficar(self):
        ax = self.fig.add_subplot(111)
        ax.clear()
        x = [p.num_pregunta for p in self.cuestionario]
        y = [p.puntaje for p in self.cuestionario]
        ax.bar(x, y, color="#3498db")
        ax.set_title("Puntuación por Pregunta", fontsize=14, fontweight='bold')
        ax.set_xlabel("Número de Pregunta", fontsize=12)
        ax.set_ylabel("Puntaje (0 - 3)", fontsize=12)
        ax.set_ylim(0, 3)
        self.canvas.draw()

    def guardar_resultados(self):
        import json
        data = {
            "puntaje_total": self.puntaje_total,
            "preguntas": [{"num_pregunta": p.num_pregunta, "texto": p.texto, "puntaje": p.puntaje} for p in self.cuestionario]
        }
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar Resultados", "", "JSON Files (*.json)")
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            QMessageBox.information(self, "Éxito", "Resultados guardados correctamente.")

#Clase de RecursosEducativos
class RecursosEducativos(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        #Título
        self.label_recursos = QLabel("Recursos Educativos")
        self.label_recursos.setFont(QFont("Arial", 18, QFont.Bold))
        self.label_recursos.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_recursos)

        #Descripción
        self.label_descripcion = QLabel("Aquí encontrarás videos y recursos para aprender más sobre la adicción a videojuegos y cómo manejarla:")
        self.label_descripcion.setAlignment(Qt.AlignCenter)
        self.label_descripcion.setWordWrap(True)
        layout.addWidget(self.label_descripcion)

        # Contenedor para los enlaces
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: white; border: none;")
        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.setSpacing(10)

        # Enlaces a YouTube
        recursos = [
            {
                "titulo": "Señales de adicción a los videojuegos",
                "url": "https://youtube.com/shorts/rlr_VdLXX_U?si=83ehGrFZaji25QBp",
                "descripcion": "Video que explica las señales principales de la adicción a los videojuegos."
            },
            {
                "titulo": "Consejos para controlar el tiempo de juego",
                "url": "https://youtube.com/shorts/mNrzsgF87g0?si=G2m5qz9tzs7nSEAD",
                "descripcion": "Estrategias efectivas para manejar y reducir el tiempo que pasas jugando."
            },
            {
                "titulo": "Cómo afecta la adicción a los videojuegos",
                "url": "https://youtube.com/shorts/dvYrdh_84-w?si=-ItjE0BFCpPSzG3W",
                "descripcion": "Video que muestra los efectos de la adicción a los videojuegos en la vida diaria."
            }
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

#Clase Principal
class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test de Adicción a Videojuegos")
        self.setGeometry(100, 100, 735, 500)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-size: 14px;
                background-color: white;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 14px;
                border-radius: 6px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QRadioButton {
                font-size: 14px;
                spacing: 8px;
            }
            QTabWidget::pane {
                border: 1px solid #ddd;
                border-radius: 6px;
                background-color: white;
            }
            QTabBar::tab {
                padding: 10px 20px;
                background-color: #ecf0f1;
                border: 1px solid #ddd;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                font-size: 14px;
            }
            QTabBar::tab:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        self.usuario_registrado = False
        self.init_ui()

    def init_ui(self):
        # Tabs
        self.tabs = QTabWidget()
        self.tabs.currentChanged.connect(self.verificar_registro)
        self.setCentralWidget(self.tabs)

        # Crear ventanas
        self.tab_registro = QWidget()
        self.tab_test = QWidget()
        self.tab_resultados = QWidget()
        self.tab_sintomas = QWidget()
        self.tab_recursos = QWidget()
        self.tabs.addTab(self.tab_registro, "Registro")
        self.tabs.addTab(self.tab_test, "Test")
        self.tabs.addTab(self.tab_resultados, "Resultados")
        self.tabs.addTab(self.tab_sintomas, "Síntomas y Señales")
        self.tabs.addTab(self.tab_recursos, "Recursos Educativos")

        # Deshabilitar pestañas hasta que el usuario se registre
        self.tabs.setTabEnabled(1, False)  # Test
        self.tabs.setTabEnabled(2, False)  # Resultados
        self.tabs.setTabEnabled(3, False)  # Síntomas
        self.tabs.setTabEnabled(4, False)  # Recursos Educativos

        # Configurar cada ventana
        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()
        self.crear_pestana_sintomas()
        self.crear_pestana_recursos()

        # Botón de salir
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.setStyleSheet("background-color: #e74c3c;")
        self.btn_salir.clicked.connect(self.close)
        self.tabs.setCornerWidget(self.btn_salir, Qt.TopRightCorner)

    def verificar_registro(self, index):
        if index != 0 and not self.usuario_registrado:
            QMessageBox.warning(self, "Advertencia", "Debes registrarte primero para acceder a esta sección.")
            self.tabs.setCurrentIndex(0)

    #Registro
    def crear_pestana_registro(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        self.label_registro = QLabel("Regístrate para continuar")
        self.label_registro.setFont(QFont("Arial", 15, QFont.Bold))
        self.label_registro.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_registro)

        self.input_correo = QLineEdit()
        self.input_correo.setPlaceholderText("ejemplo@correo.com")

        self.input_contra = QLineEdit()
        self.input_contra.setPlaceholderText("Contraseña")
        self.input_contra.setEchoMode(QLineEdit.Password)

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Correo:"))
        form_layout.addWidget(self.input_correo)
        form_layout.addWidget(QLabel("Contraseña:"))
        form_layout.addWidget(self.input_contra)
        layout.addLayout(form_layout)

        self.btn_registrar = QPushButton("Registrarse")
        self.btn_registrar.clicked.connect(self.registrar_usuario)
        layout.addWidget(self.btn_registrar, alignment=Qt.AlignCenter)

        self.tab_registro.setLayout(layout)

    def registrar_usuario(self):
        correo = self.input_correo.text()
        contra = self.input_contra.text()

        if correo == "" or contra == "":
            QMessageBox.warning(self, "Error", "Completa todos los campos")
            return

        # Validar formato de correo electrónico
        if not validar_email(correo):
            QMessageBox.warning(self, "Error", "Por favor ingresa un correo electrónico válido.\nEjemplo: usuario@dominio.com")
            return

        QMessageBox.information(self, "Éxito", "Registro exitoso. Ahora puedes realizar el test.")
        self.usuario_registrado = True
        self.tabs.setTabEnabled(1, True)  # Habilitar Test
        self.tabs.setTabEnabled(3, True)  # Habilitar Síntomas
        self.tabs.setTabEnabled(4, True)  # Habilitar Recursos Educativos
        self.tabs.setCurrentIndex(1)  # Cambiar a pestaña Test
    #Test
    def crear_pestana_test(self):
        layout = QGridLayout()
        layout.setSpacing(15)

        self.crearCuestionario()
        self.index = 0
        self.maximo = len(self.cuestionario)
        self.puntaje_total = 0

        self.lb_num = QLabel("")
        self.lb_num.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.lb_pregunta = QLabel("")
        self.lb_pregunta.setWordWrap(True)
        self.lb_pregunta.setStyleSheet("font-size: 15px;")

        # Opciones de respuesta
        self.opcion_siempre = QRadioButton("Siempre")
        self.opcion_frecuente = QRadioButton("Frecuentemente")
        self.opcion_aveces = QRadioButton("A veces")
        self.opcion_nunca = QRadioButton("Nunca")

        self.grupo_opciones = QButtonGroup()
        self.grupo_opciones.addButton(self.opcion_siempre)
        self.grupo_opciones.addButton(self.opcion_frecuente)
        self.grupo_opciones.addButton(self.opcion_aveces)
        self.grupo_opciones.addButton(self.opcion_nunca)

        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_siguiente.clicked.connect(self.siguiente)

        layout.addWidget(self.lb_num, 0, 0, 1, 2)
        layout.addWidget(self.lb_pregunta, 1, 0, 1, 2)
        layout.addWidget(self.opcion_siempre, 2, 0, 1, 2)
        layout.addWidget(self.opcion_frecuente, 3, 0, 1, 2)
        layout.addWidget(self.opcion_aveces, 4, 0, 1, 2)
        layout.addWidget(self.opcion_nunca, 5, 0, 1, 2)
        layout.addWidget(self.btn_siguiente, 6, 0, 1, 2)

        self.tab_test.setLayout(layout)
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
        self.grupo_opciones.setExclusive(False)
        for btn in [self.opcion_siempre, self.opcion_frecuente, self.opcion_aveces, self.opcion_nunca]:
            btn.setChecked(False)
        self.grupo_opciones.setExclusive(True)

        pregunta = self.cuestionario[self.index]
        self.lb_num.setText(f"Pregunta {pregunta.num_pregunta} de {self.maximo}")
        self.lb_pregunta.setText(pregunta.texto)

    def obtenerPuntajeOpcion(self):
        if self.opcion_siempre.isChecked(): return 3
        if self.opcion_frecuente.isChecked(): return 2
        if self.opcion_aveces.isChecked(): return 1
        if self.opcion_nunca.isChecked(): return 0
        return None

    def siguiente(self):
        puntaje = self.obtenerPuntajeOpcion()
        if puntaje is None:
            QMessageBox.warning(self, "Advertencia", "Debes seleccionar una opción antes de continuar.")
            return

        self.cuestionario[self.index].puntaje = puntaje
        self.puntaje_total += puntaje

        if self.index < self.maximo - 1:
            self.index += 1
            self.mostrarPregunta()
        else:
            self.finalizarTest()

    def finalizarTest(self):
        QMessageBox.information(
            self,
            "Test Completado",
            f"Has finalizado el test.\n\nTu puntuación total es: {self.puntaje_total} puntos."
        )
        resultados_widget = Resultados(self.puntaje_total, self.cuestionario)

        # Limpiar pestaña de resultados
        layout = self.tab_resultados.layout()
        if layout:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()
        else:
            layout = QVBoxLayout()
            self.tab_resultados.setLayout(layout)

        layout.addWidget(resultados_widget)
        self.tabs.setTabEnabled(2, True) 
        self.tabs.setCurrentIndex(2)  # Cambiar a pestaña Resultados

    #Resultados
    def crear_pestana_resultados(self):
        layout = QVBoxLayout()
        self.resultado_label = QLabel("Completa el test para ver tus resultados.")
        self.resultado_label.setAlignment(Qt.AlignCenter)
        self.resultado_label.setFont(QFont("Arial", 14))
        layout.addWidget(self.resultado_label)
        self.tab_resultados.setLayout(layout)

    #Síntomas y Señales
    def crear_pestana_sintomas(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        self.label_sintomas = QLabel("Síntomas y Señales de Adicción a Videojuegos")
        self.label_sintomas.setFont(QFont("Arial", 18, QFont.Bold))
        self.label_sintomas.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_sintomas)

        sintomas = [
            "✔ Pérdida de control sobre el tiempo de juego.",
            "✔ Abandono de responsabilidades como escuela, trabajo, familia ect",
            "✔ Irritabilidad o ansiedad cuando no se puede jugar",
            "✔ Priorizar videojuegos sobre relaciones sociales",
            "✔ Dificultad para reducir el tiempo de juego",
            "✔ Mentir sobre el tiempo dedicado a los videojuegos",
            "✔ Problemas de sueño o alimentación por jugar",
            "✔ Bajo rendimiento académico o laboral"
        ]

        for sintoma in sintomas:
            label = QLabel(sintoma)
            label.setStyleSheet("font-size: 14px;")
            layout.addWidget(label)

        self.tab_sintomas.setLayout(layout)

    #Pestaña de Recursos Educativos
    def crear_pestana_recursos(self):
        layout = QVBoxLayout()
        recursos_widget = RecursosEducativos()
        layout.addWidget(recursos_widget)
        self.tab_recursos.setLayout(layout)

#iniciar el codigo
app = QApplication(sys.argv)
from Bienvenida import Bienvenida  # Asegúrate de tener este archivo

def abrir_principal():
    global window_principal
    window_principal = Principal()
    window_principal.show()

bienvenida = Bienvenida(abrir_principal)
bienvenida.show()
app.exec_()
