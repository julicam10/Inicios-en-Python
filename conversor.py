def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('¿Cuantos pesos ' + tipo_pesos + ' quieres convertir?: '))
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes ' + dolares + ' dólares')


menu = """
Bienvenido al conversor de monedas 🪙

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor('colombianos', 4132)
elif opcion == 2:
    conversor('argentinos', 124.71)
elif opcion == 3:
    conversor('mexicano', 19.90) 
else: 
    print('Por favor selecciona una opción correcta')