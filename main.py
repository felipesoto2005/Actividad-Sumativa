from PyQt5.QtWidgets import QApplication
import sys
from ui_elements import FinanzasApp  # Importa la clase principal de la interfaz

if __name__ == "__main__":
    app = QApplication(sys.argv)     # Crea la aplicación
    ventana = FinanzasApp()          # Instancia la interfaz
    ventana.show()                   # Muestra la ventana
    sys.exit(app.exec_())            # Ejecuta el bucle principal