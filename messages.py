from PyQt5.QtWidgets import QMessageBox

def mostrar_resultado(widget, gastos, balance):
    QMessageBox.information(widget, "Balance Mensual",
        f"Total de gastos: ${gastos:.2f}\nBalance final: ${balance:.2f}")

def mostrar_error(widget):
    QMessageBox.warning(widget, "Error", "Por favor, ingrese valores numéricos válidos.")