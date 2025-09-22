from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
)
from logic import calcular_balance
from messages import mostrar_resultado, mostrar_error

class FinanzasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Finanzas Personales")
        self.init_ui()

    def init_ui(self):
        # Widgets de entrada
        self.ingresos_label = QLabel("Ingresos mensuales:")
        self.ingresos_input = QLineEdit()

        self.alimentacion_label = QLabel("Gasto en alimentación:")
        self.alimentacion_input = QLineEdit()

        self.transporte_label = QLabel("Gasto en transporte:")
        self.transporte_input = QLineEdit()

        self.otros_label = QLabel("Otros gastos:")
        self.otros_input = QLineEdit()

        # Botón de cálculo
        self.calcular_btn = QPushButton("Calcular Balance")
        self.calcular_btn.clicked.connect(self.on_calcular)

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.ingresos_label)
        layout.addWidget(self.ingresos_input)
        layout.addWidget(self.alimentacion_label)
        layout.addWidget(self.alimentacion_input)
        layout.addWidget(self.transporte_label)
        layout.addWidget(self.transporte_input)
        layout.addWidget(self.otros_label)
        layout.addWidget(self.otros_input)
        layout.addWidget(self.calcular_btn)

        self.setLayout(layout)

    def on_calcular(self):
        try:
            ingresos = float(self.ingresos_input.text())
            alimentacion = float(self.alimentacion_input.text())
            transporte = float(self.transporte_input.text())
            otros = float(self.otros_input.text())

            total_gastos, balance = calcular_balance(ingresos, alimentacion, transporte, otros)
            mostrar_resultado(self, total_gastos, balance)
        except ValueError:
            mostrar_error(self)