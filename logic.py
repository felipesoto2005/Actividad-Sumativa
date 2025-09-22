def calcular_balance(ingresos, alimentacion, transporte, otros):
    total_gastos = alimentacion + transporte + otros
    balance = ingresos - total_gastos
    return total_gastos, balance