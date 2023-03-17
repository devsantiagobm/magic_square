
def preguntarValores(pregunta, dimension):
    valor = input(pregunta)

    if dimension: 
      while not valor.isnumeric() or (int(valor) == 1) or (int(valor) % 2 == 0):
            valor = input(pregunta)
    else: 
      while not valor.isnumeric() or (int(valor) <= 0) or (int(valor) > 8):
            valor = input(pregunta)

    return int(valor)
    
def mostrar_cuadrado(cuadrado):
  for fila in cuadrado:
    print(fila)
  
def crear_cuadrado(n):
  cuadrado = [[0] * n for _ in range(n)]

  fila = 0
  columna = n // 2
  casillas = n ** 2 
  
  for num in range(1, casillas + 1):
    cuadrado[fila][columna] = num

    nueva_fila = (fila - 1) % n
    nueva_columna = (columna - 1) % n
    
    if cuadrado[nueva_fila][nueva_columna]:
      fila = (fila + 1) % n
    else:
      fila, columna = nueva_fila, nueva_columna
  
  return cuadrado
    
def rotar_cuadrado(cuadrado, n):
    cuadrado_a_llenar = [[0] * n for _ in range(n)]
  
    for fila in cuadrado:
        indexFila = cuadrado.index(fila)
        
        for numero in fila:
            indexNumero = fila.index(numero)
            nuevoIndiceColumna = len(fila) - indexFila - 1
            cuadrado_a_llenar[indexNumero][nuevoIndiceColumna] = numero
       
    return cuadrado_a_llenar

def reflejar_cuadrado(cuadrado, dimension):
    index_uno = None
    centro = dimension //2
    
    for fila in cuadrado:
      try:
        index_uno = fila.index(1)
        break
      except: "no hacer nada"
    
    if index_uno == centro:
      for fila in cuadrado: fila.reverse()
    else:
      cuadrado.reverse()
    return cuadrado

def mover_cuadrado(combinacion, dimension, cuadrado):
    combinacion_rango = combinacion
      
    if combinacion % 2 == 0: combinacion_rango -= 1
    for i in range(combinacion_rango // 2): cuadrado = rotar_cuadrado(cuadrado, dimension)
    if combinacion % 2 == 0: cuadrado = reflejar_cuadrado(cuadrado, dimension)

    return cuadrado

def inicio():
    dimension = preguntarValores("Escribe la dimensión del cuadrado ", True)
    combinacion = preguntarValores("Escribe la combinación del cuadrado ", False)
    
    cuadrado = crear_cuadrado(dimension)
    cuadrado = mover_cuadrado(combinacion, dimension, cuadrado)
    mostrar_cuadrado(cuadrado)
    
    print("Cuadrado ", dimension, "x", dimension, " con combinación ", combinacion)
    
    inicio()
    
inicio()