def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)  # Redondeo a dos decimales.
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
$$$ Bienvenido al conversor de divisas $$$

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Eligeuna opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)    
elif opcion == 3:
    conversor("mexicanos", 20.54)    
else:
    print('Ingresa una opción correcta por favor')



# Uso de la función round(param1, param2)
""" Esta función redondea cierta cantidad de decimales:
    param1: el primer argumento es la variable que queremos redondear.
    param2: el segundo argumento corresponde a la cantidad de decimales 
            que queremos redondear. """
