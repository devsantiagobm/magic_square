def preguntarValores(pregunta, dimension):
    valor = input(pregunta)

    if dimension:
        while not valor.isnumeric() or (int(valor) == 1) or (int(valor) % 2 == 0):
            valor = input(pregunta)
    else:
        while not valor.isnumeric() or (int(valor) != 1 and int(valor) != 6):
            valor = input(pregunta)

    return int(valor)


def mostrar_cuadrado(cuadrado):
    for fila in cuadrado:
        print(fila)

def crear_cuadrado(n, combinacion):
    combinacion_uno = combinacion == 1
    cuadrado = [[0] * n for _ in range(n)]

    fila = 0 if combinacion_uno else n - 1
    columna = n // 2
    casillas = n ** 2

    for num in range(1, casillas + 1):
        cuadrado[fila][columna] = num

        nueva_fila = (fila - 1) % n if combinacion_uno else (fila + 1) % n
        nueva_columna = (columna - 1) % n

        if cuadrado[nueva_fila][nueva_columna]:
            fila = (fila + 1) % n if combinacion_uno else (fila - 1) % n
        else:
            fila, columna = nueva_fila, nueva_columna

    mostrar_cuadrado(cuadrado)


def inicio():
    dimension = preguntarValores("Escribe la dimensión del cuadrado ", True)
    combinacion = preguntarValores("Escribe la combinación del cuadrado ", False)
    print("Cuadrado de dimensión ", dimension, " en combinacion ", combinacion)
    crear_cuadrado(dimension, combinacion)

    inicio()

inicio()
