# Programa que calcula dólares americanos a pesos mexicanos

dolares = input("¿Cuántos dolares americanos tienes?: ")
dolares = float(dolares)
valor_dolar = 20.54
pesos = dolares * valor_dolar
pesos = round(pesos, 2)  # Redondeo a dos decimales.
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")

# Uso de la función round(param1, param2)
""" Esta función redondea cierta cantidad de decimales:
    param1: el primer argumento es la variable que queremos redondear.
    param2: el segundo argumento corresponde a la cantidad de decimales 
            que queremos redondear. """
