pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)  # Redondeo a dos decimales.
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")

# Uso de la función round(param1, param2)
""" Esta función redondea cierta cantidad de decimales:
    param1: el primer argumento es la variable que queremos redondear.
    param2: el segundo argumento corresponde a la cantidad de decimales 
            que queremos redondear. """
