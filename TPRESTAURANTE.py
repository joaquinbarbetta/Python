import random

platos = ["Milanesa", "Pizza", "Hamburguesa", "Ensalada", "Tallarines"]
precios_platos = [2500, 2200, 2000, 1800, 2300]

bebidas = ["Agua", "Coca-Cola", "Jugo", "Cerveza", "Sprite"]
precios_bebidas = [500, 800, 700, 900, 750]

dias= ["Lunes","Martes", "Miércoles", "Jueves", "Viernes"]
def mostrar_menu():
    print("Restaurante UADE")

    print("Platos disponibles:")
    for i in range(len(platos)):
        print(str(i + 1) + ". " + platos[i] + " - $" + str(precios_platos[i]))

    print("\nBebidas disponibles:")
    for i in range(len(bebidas)):
        print(str(i + 1) + ". " + bebidas[i] + " - $" + str(precios_bebidas[i]))
    

def sugerir_comida():
    indice_plato = random.randint(0, len(platos) - 1)
    indice_bebida = random.randint(0, len(bebidas) - 1)
    print("Sugerencia del chef:")
    print("Plato: " , platos[indice_plato] , " - $" , str(precios_platos[indice_plato]))
    print("Bebida: " , bebidas[indice_bebida] , " - $" , str(precios_bebidas[indice_bebida]))

def reserva():


a=mostrar_menu()
b=sugerir_comida()
print(a)
print(b)

plato_num = input("Ingrese el número del plato que desea: ")
bebida_num = input("Ingrese el número de la bebida que desea: ")

if (plato_num >= "1" and plato_num <= str(len(platos))) and (bebida_num >= "1" and bebida_num <= str(len(bebidas))):
    plato_index = int(plato_num) - 1
    bebida_index = int(bebida_num) - 1

    total = precios_platos[plato_index] + precios_bebidas[bebida_index]

    print("Pedido confirmado: " , platos[plato_index] , " con " , bebidas[bebida_index])
    print("Total a pagar: $" , str(total))
    print("¡Gracias por su visita!")
else:
    print("Entrada no válida. Por favor ingrese opciones del menú.")

