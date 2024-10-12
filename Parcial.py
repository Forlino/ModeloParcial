import random

# 1. Obtener existencias
def obtener_existencias():
    existencias = []
    for _ in range(20):  # Tenemos 20 depósitos
        deposito = [random.randint(5000, 20000) for _ in range(4)]  # 4 tipos de cereales
        existencias.append(deposito)
    return existencias

# 2. Calcular por cada depósito la cantidad total de kilos almacenados
def calcular_kilos_por_deposito(existencias):
    total_kilos = []
    for deposito in existencias:
        total = sum(deposito)
        total_kilos.append(total)
    return total_kilos

# 3. Nombre del cereal que almacenó menos kilos en cada depósito
def cereal_menos_kilos_por_deposito(existencias):
    menos_kilos = []
    cereales = ['maiz', 'trigo', 'cebada', 'centeno']
    for deposito in existencias:
        min_index = deposito.index(min(deposito))
        menos_kilos.append(cereales[min_index])
    return menos_kilos

# 4. Máxima cantidad de kilos almacenados de cada cereal
def max_kilos_por_cereal(existencias):
    maximos = [0, 0, 0, 0]
    for deposito in existencias:
        for i in range(4):
            if deposito[i] > maximos[i]:
                maximos[i] = deposito[i]
    return maximos

# 5. Depósito con mayor recaudación
def deposito_mayor_recaudacion(existencias, precios):
    recaudaciones = []
    for deposito in existencias:
        recaudacion = 0
        for i in range(4):
            recaudacion += deposito[i] * precios[i]
        recaudaciones.append(recaudacion)
    max_recaudacion = max(recaudaciones)
    for i in range(len(recaudaciones)):
        if recaudaciones[i] == max_recaudacion:
            return i + 1  # +1 para depósito 1 a 20

# 6. Cantidad de depósitos con más de 50000 kilos
def depositos_mas_de_50000(existencias):
    total_kilos = calcular_kilos_por_deposito(existencias)
    contador = 0
    for total in total_kilos:
        if total > 50000:
            contador += 1
    return contador

# 7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados
def porcentaje_kilos_cereal(existencias):
    total_kilos_cereales = [0, 0, 0, 0]
    total_kilos_general = 0
    for deposito in existencias:
        for i in range(4):
            total_kilos_cereales[i] += deposito[i]
            total_kilos_general += deposito[i]

    porcentajes = []
    for kilos in total_kilos_cereales:
        porcentaje = (kilos / total_kilos_general) * 100
        porcentajes.append(porcentaje)

    max_cereal = 0
    max_porcentaje = porcentajes[0]
    for i in range(1, len(porcentajes)):
        if porcentajes[i] > max_porcentaje:
            max_porcentaje = porcentajes[i]
            max_cereal = i

    return porcentajes, max_cereal

# 8. Informe de recaudaciones
def generar_informe_recaudaciones(existencias, precios):
    recaudaciones = []
    for deposito in existencias:
        recaudacion = 0
        for i in range(4):
            recaudacion += deposito[i] * precios[i]
        recaudaciones.append(recaudacion)
    
    informe_ordenado = []
    while recaudaciones:
        max_recaudacion = max(recaudaciones)
        for i in range(len(recaudaciones)):
            if recaudaciones[i] == max_recaudacion:
                informe_ordenado.append((i + 1, recaudaciones[i]))  # +1 para depósito 1 a 20
                recaudaciones[i] = -1
                break
    return informe_ordenado

def mostrar_menu():
    print("-" * 50)
    print("Seleccione una opción:")
    print("1. Obtener existencias")
    print("2. Calcular por cada depósito la cantidad total de kilos almacenados")
    print("3. Nombre del cereal que almacenó menos kilos en cada depósito")
    print("4. Máxima cantidad de kilos almacenados de cada cereal")
    print("5. Depósito con mayor recaudación")
    print("6. Cantidad de depósitos con más de 50000 kilos")
    print("7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados")
    print("8. Informe de recaudaciones")
    print("9. Salir")
    

def main():
    existencias = []
    precios = [10, 12, 8, 15]
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            existencias = obtener_existencias()
            print("-" * 50)
            print("Existencias:", existencias)
        elif opcion == '2':
            if existencias:
                total_kilos = calcular_kilos_por_deposito(existencias)
                print("-" * 50)
                print("Total kilos por depósito:", total_kilos)
            else:
                print("-" * 50)
                print("Primero debe obtener las existencias (opción 1).")
        elif opcion == '3':
            if existencias:
                menos_kilos = cereal_menos_kilos_por_deposito(existencias)
                print("-" * 50)
                print("Cereal con menos kilos por depósito:", menos_kilos)
            else:
                print("-" * 50)
                print("Primero debe obtener las existencias (opción 1).")
        elif opcion == '4':
            if existencias:
                maximos = max_kilos_por_cereal(existencias)
                print("-" * 50)
                print("Máxima cantidad de kilos por cereal:", maximos)
            else:
                print("-" * 50)
                print("Primero debe obtener las existencias (opción 1).")
                
        elif opcion == '5':
            if existencias:
                mayor_recaudacion = deposito_mayor_recaudacion(existencias, precios)
                print("-" * 50)
                print("Depósito con mayor recaudación:", mayor_recaudacion)
            else:
                print("-" * 50)
                print("Primero debe obtener las existencias (opción 1).")
        elif opcion == '6':
            if existencias:
                depositos_50000 = depositos_mas_de_50000(existencias)
                print("-" * 50)
                print("Cantidad de depósitos con más de 50000 kilos:", depositos_50000)
            else:
                print("-" * 50)
                print("Primero debe obtener las existencias (opción 1).")
        elif opcion == '7':
            if existencias:
                porcentajes, max_cereal = porcentaje_kilos_cereal(existencias)
                print("-" * 50)
                print("Porcentajes de kilos por cereal:", porcentajes)
                print("Cereal con mayor porcentaje de kilos:", max_cereal)
            else:
                print("-" * 50)
                print("Primero debe obtener las existencias (opción 1).")
        elif opcion == '8':
            if existencias:
                informe_recaudaciones = generar_informe_recaudaciones(existencias, precios)
                print("-" * 50)
                print("Informe de recaudaciones:", informe_recaudaciones)
            else:
                print("-" * 50)
                print("Primero debe obtener las existencias (opción 1).")
        elif opcion == '9':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

