#Programa 2: Aprobación de préstamo
"""
Un banco evalúa solicitudes de préstamo bajo dos criterios principales: (1) el solicitante debe tener un ingreso mensual mayor a $2000 o una puntuación de crédito de al menos 650, y (2) no debe tener deudas pendientes. Si cumple estas condiciones, el préstamo se aprueba; en caso contrario, se rechaza."
"""

# Variables
ingreso_mensual = 6000
deuda = 1
puntuacion_credito = 800

# Operadores lógicos
if (ingreso_mensual > 2000 or puntuacion_credito > 649 ) and deuda == 0:
    print("Préstamo aprobado 💰")
else:
    print("Préstamo rechazado 🚫")