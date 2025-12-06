from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Resultados(QWidget):
    def __init__(self, puntaje_total, cuestionario):
        super().__init__()
        self.puntaje_total = puntaje_total
        self.cuestionario = cuestionario
        layout = QVBoxLayout()

        # Etiqueta con el puntaje total
        self.lb_info = QLabel(f"Puntaje total obtenido: {self.puntaje_total}")
        self.lb_info.setStyleSheet("font-size:16px; font-weight:bold;")
        layout.addWidget(self.lb_info)

        # Etiqueta con el diagnóstico (recomendaciones)
        self.lb_diagnostico = QLabel(self.obtener_diagnostico())
        self.lb_diagnostico.setStyleSheet("font-size:14px; color: #333; margin-top: 10px; margin-bottom: 20px;")
        layout.addWidget(self.lb_diagnostico)

        # Gráfica de barras
        self.fig = Figure(figsize=(4, 3))
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        # Resultados detallados (opcional)
        self.detalles = QTextEdit()
        self.detalles.setReadOnly(True)
        self.detalles.setStyleSheet("font-size:12px; background-color: #f9f9f9;")
        self.detalles.setPlainText(self.obtener_resultados_detallados_texto())
        layout.addWidget(self.detalles)

        self.setLayout(layout)
        self.graficar()

    def graficar(self):
        ax = self.fig.add_subplot(111)
        ax.clear()
        x = [p.num_pregunta for p in self.cuestionario]
        y = [p.puntaje for p in self.cuestionario]
        ax.bar(x, y, color="#4CAF50")
        ax.set_title("Puntuación por pregunta")
        ax.set_xlabel("Número de Pregunta")
        ax.set_ylabel("Puntaje (0 - 3)")
        ax.set_ylim(0, 3)
        self.canvas.draw()

    def obtener_diagnostico(self):
        if self.puntaje_total <= 10:
            return "✅ Bajo riesgo de adicción a videojuegos. Mantén un equilibrio saludable."
        elif 11 <= self.puntaje_total <= 20:
            return "⚠️ Riesgo moderado de adicción. Considera reducir el tiempo de juego y priorizar otras actividades."
        elif 21 <= self.puntaje_total <= 30:
            return "❌ Alto riesgo de adicción. Te recomendamos buscar apoyo profesional para manejar este hábito."
        else:
            return "❓ Puntuación fuera de rango. Revisa tus respuestas."

    def obtener_resultados_detallados(self):
        resultados = []
        for pregunta in self.cuestionario:
            resultados.append({
                "pregunta": pregunta.texto,
                "puntaje": pregunta.puntaje,
                "opcion": self._obtener_opcion(pregunta.puntaje)
            })
        return resultados

    def obtener_resultados_detallados_texto(self):
        texto = "RESULTADOS DETALLADOS:\n\n"
        for resultado in self.obtener_resultados_detallados():
            texto += f"• Pregunta: {resultado['pregunta']}\n  Respuesta: {resultado['opcion']} (Puntaje: {resultado['puntaje']})\n\n"
        return texto

    def _obtener_opcion(self, puntaje):
        if puntaje == 3:
            return "Siempre"
        elif puntaje == 2:
            return "Frecuentemente"
        elif puntaje == 1:
            return "A veces"
        elif puntaje == 0:
            return "Nunca"
        else:
            return "Sin respuesta"
