#Codigo de ordenamiento burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)  # Cantidad de elementos en la lista

    for i in range(n - 1):   # Bucle exterior para las pasadas
        hubo_intercambio = False  # Marca si hubo un intercambio en esta pasada

        # Bucle interior para las comparaciones e intercambios
        for j in range(n - 1 - i):  # Cada pasada evita revisar los últimos ya ordenados
            if lista[j] > lista[j + 1]:
                # ¡Intercambio!
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True

        if not hubo_intercambio: # Si no hubo ningún intercambio, la lista ya está ordenada
            break

    return lista  # Opcional: también se puede omitir

if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_burbuja(numeros)
    print("Después Ordenamiento Burbuja:", numeros)

    print("\n--- Ejecutando pruebas con asserts ---")

    # Caso 1: Lista desordenada
    lista1 = [6, 3, 8, 2, 5]
    try:
        ordenamiento_burbuja(lista1)
        assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1: Lista desordenada"
        print("Caso 1 (Lista desordenada): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: Lista ya ordenada
    lista2 = [1, 2, 3, 4, 5]
    try:
        ordenamiento_burbuja(lista2)
        assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2: Lista ya ordenada"
        print("Caso 2 (Lista ya ordenada): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: Lista ordenada a la inversa (peor caso)
    lista3 = [5, 4, 3, 2, 1]
    try:
        ordenamiento_burbuja(lista3)
        assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3: Lista ordenada a la inversa"
        print("Caso 3 (Lista ordenada a la inversa): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: Lista con elementos duplicados
    lista4 = [5, 1, 4, 2, 8, 5, 2]
    try:
        ordenamiento_burbuja(lista4)
        assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4: Lista con elementos duplicados"
        print("Caso 4 (Lista con elementos duplicados): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso borde: Lista vacía
    try:
        assert ordenamiento_burbuja([]) == [], "Fallo en Caso borde: Lista vacía"
        print("Caso borde (Lista vacía): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso borde: Lista con un solo elemento
    try:
        assert ordenamiento_burbuja([42]) == [42], "Fallo en Caso borde: Lista con un solo elemento"
        print("Caso borde (Lista con un solo elemento): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    print("\nPrograma realizado por Maria Vidaurre")



#Codigo ordenamiento por insercion
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]  # La "carta" que vamos a insertar
        posicion_actual = i

        # Desplazar elementos mayores hacia la derecha
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        # Insertar la "carta" en su hueco correcto
        lista[posicion_actual] = valor_actual

    return lista

if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_insercion(numeros)
    print("Después Ordenamiento Inserción:", numeros)

    print("\n--- Ejecutando pruebas con asserts ---")

    # Caso 1: Lista desordenada
    lista1 = [6, 3, 8, 2, 5]
    try:
        # No imprimimos "Antes" y "Después" para cada caso de prueba aquí,
        # ya que la salida principal ya lo hace.
        ordenamiento_insercion(lista1)
        assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1: Lista desordenada"
        print("Caso 1 (Lista desordenada): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: Lista ya ordenada
    lista2 = [1, 2, 3, 4, 5]
    try:
        ordenamiento_insercion(lista2)
        assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2: Lista ya ordenada"
        print("Caso 2 (Lista ya ordenada): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: Lista ordenada a la inversa (peor caso)
    lista3 = [5, 4, 3, 2, 1]
    try:
        ordenamiento_insercion(lista3)
        assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3: Lista ordenada a la inversa"
        print("Caso 3 (Lista ordenada a la inversa): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: Lista con duplicados
    lista4 = [5, 1, 4, 2, 8, 5, 2]
    try:
        ordenamiento_insercion(lista4)
        assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4: Lista con duplicados"
        print("Caso 4 (Lista con duplicados): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso borde: Lista vacía
    try:
        assert ordenamiento_insercion([]) == [], "Fallo en Caso borde: Lista vacía"
        print("Caso borde (Lista vacía): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso borde: Lista con un solo elemento
    try:
        assert ordenamiento_insercion([42]) == [42], "Fallo en Caso borde: Lista con un solo elemento"
        print("Caso borde (Lista con un solo elemento): SUCCESS")
    except AssertionError as e:
        print(f"Error: {e}")

print("\nPrograma realizado por Maria Vidaurre")


#Codigo Merge Sort
def merge_sort(lista):
  # Paso Vencer (Condición Base de la Recursividad):
  if len(lista) <= 1:
      return lista

  # Paso 1: DIVIDIR
  medio = len(lista) // 2
  mitad_izquierda = lista[:medio]
  mitad_derecha = lista[medio:]

  # Paso 2: VENCER (Recursión)
  izquierda_ordenada = merge_sort(mitad_izquierda)
  derecha_ordenada = merge_sort(mitad_derecha)

  # Paso 3: COMBINAR
  print(f"Mezclaría {izquierda_ordenada} y {derecha_ordenada}")
  return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
  resultado = []
  i = j = 0

  # Comparar elementos de izquierda y derecha uno por uno
  while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
          resultado.append(izquierda[i])
          i += 1
      else:
          resultado.append(derecha[j])
          j += 1

  # Agregar cualquier elemento restante
  resultado.extend(izquierda[i:])
  resultado.extend(derecha[j:])

  return resultado

# --- Prueba ---
lista_prueba = [8, 3, 5, 1]
print("Lista original:", lista_prueba)
resultado = merge_sort(lista_prueba)
print("Lista ordenada:", resultado)

# --- Pruebas automatizadas ---
assert merge_sort([]) == []                         # Lista vacía
assert merge_sort([1]) == [1]                       # Lista con un solo elemento
assert merge_sort([5, 2]) == [2, 5]                  # Lista con dos elementos
assert merge_sort([3, 1, 2]) == [1, 2, 3]            # Lista con tres elementos desordenados
assert merge_sort([10, 5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8, 10]  # Lista par
assert merge_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]  # Lista en orden descendente
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # Lista ya ordenada
assert merge_sort([4, 2, 2, 4, 1]) == [1, 2, 2, 4, 4]  # Lista con elementos repetidos
assert merge_sort([100, -50, 0, 50, -100]) == [-100, -50, 0, 50, 100]  # Lista con enteros negativos y positivos
assert merge_sort([2.5, 1.2, 3.8]) == [1.2, 2.5, 3.8]  # Lista con flotantes
print("¡Todas las pruebas con assert pasaron correctamente!")
print("\nPrograma realizado por Maria Vidaurre")


#Codigo Matrices
# 1. Crear la matriz de 3x3
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Imprimir la matriz completa
print("Matriz original:")
for fila in teclado:
    print(fila)

# 3. Acceder a elementos específicos
print("\nNúmero en el centro:", teclado[1][1])  # 5
print("Número en la esquina inferior derecha:", teclado[2][2])  # 9

# 4. Modificar el número en la esquina superior izquierda (1 por un 0)
teclado[0][0] = 0

# 5. Imprimir la matriz modificada
print("\nMatriz modificada:")
for fila in teclado:
    print(fila)

# Usamos el teclado modificado del ejercicio anterior
teclado = [
    [0, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

print("Matriz como cuadrícula:")
for fila in teclado:
    for elemento in fila:
        print(elemento, end="\t")  # Imprimir sin salto de línea, separado por tabulador
    print()  # Salto de línea al terminar cada fila



# Crear matriz 5x5 con bucles anidados
matriz_ceros = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz_ceros.append(fila)

print("\nMatriz 5x5 llena de ceros (con bucles):")
for fila in matriz_ceros:
    print(fila)
print("\nMaria Vidaurre - FIN DEL PROGRAMA DE EJERCICOS DE MATRICES")


# Codigo sumar todo elementos de una matriz
def sumar_total_matriz(matriz):

    # matriz = [[1, 2], [3, 4]]
    # resultado = 10

    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

# Función para probar que sumar_total_matriz funciona correctamente
def probar_suma_total():
    print("--- Probando sumar_total_matriz ---")

    # Caso 1: matriz normal
    m1 = [[1, 2, 3], [4, 5, 6]]
    try:
        assert sumar_total_matriz(m1) == 21, "Fallo en Caso 1: Matriz normal"
        print("Caso 1 (Matriz normal): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: matriz con negativos y ceros
    m2 = [[-1, 0, 1], [10, -5, 5]]
    try:
        assert sumar_total_matriz(m2) == 10, "Fallo en Caso 2: Matriz con negativos y ceros"
        print("Caso 2 (Matriz con negativos y ceros): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: Matriz con una fila vacía
    m3 = [[]]
    try:
        assert sumar_total_matriz(m3) == 0, "Fallo en Caso 3: Matriz con una fila vacía"
        print("Caso 3 (Matriz con una fila vacía): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: Matriz completamente vacía
    m4 = []
    try:
        assert sumar_total_matriz(m4) == 0, "Fallo en Caso 4: Matriz completamente vacía"
        print("Caso 4 (Matriz completamente vacía): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 5: Matriz de un solo elemento
    m5 = [[42]]
    try:
        assert sumar_total_matriz(m5) == 42, "Fallo en Caso 5: Matriz de un solo elemento"
        print("Caso 5 (Matriz de un solo elemento): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    print("Todas las pruebas para sumar_total_matriz han finalizado")

# Llamamos a la función de pruebas
if __name__ == "__main__":
    probar_suma_total()



#Codigo para sumar por fila en matriz
# Definimos la función que suma los elementos por cada fila de la matriz
def sumar_por_filas(matriz):
    """
    Esta función recibe una matriz (lista de listas)
    y devuelve una lista con la suma de cada fila.

    Ejemplo:
    matriz = [[1, 2, 3], [4, 5, 6]]
    resultado = [6, 15]
    """
    resultado = []
    for fila in matriz:
        suma_fila = sum(fila)  # Suma todos los elementos de la fila
        resultado.append(suma_fila)
    return resultado

# Función de prueba para verificar que sumar_por_filas funciona correctamente
def probar_suma_por_filas():
    print("\n Probando sumar_por_filas")

    # Caso 1: matriz con 3 filas y 3 columnas
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    try:
        assert sumar_por_filas(m1) == [6, 15, 24], "Fallo en Caso 1: Matriz con 3x3"
        print("Caso 1 (Matriz 3x3): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: matriz con pares repetidos
    m2 = [[10, 10], [20, 20], [30, 30]]
    try:
        assert sumar_por_filas(m2) == [20, 40, 60], "Fallo en Caso 2: Matriz con pares repetidos"
        print("Caso 2 (Matriz con pares repetidos): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: matriz con números negativos
    m3 = [[-1, -2], [0, 5], [-3, 3]]
    try:
        assert sumar_por_filas(m3) == [-3, 5, 0], "Fallo en Caso 3: Matriz con números negativos"
        print("Caso 3 (Matriz con números negativos): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: matriz con filas de diferente longitud (aunque no es una matriz "regular", la función lo maneja)
    m4 = [[1, 2], [3, 4, 5], [6]]
    try:
        assert sumar_por_filas(m4) == [3, 12, 6], "Fallo en Caso 4: Matriz con filas de diferente longitud"
        print("Caso 4 (Matriz con filas de diferente longitud): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 5: matriz vacía
    m5 = []
    try:
        assert sumar_por_filas(m5) == [], "Fallo en Caso 5: Matriz vacía"
        print("Caso 5 (Matriz vacía): success")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 6: matriz con filas vacías
    m6 = [[], [], []]
    try:
        assert sumar_por_filas(m6) == [0, 0, 0], "Fallo en Caso 6: Matriz con filas vacías"
        print("Caso 6 (Matriz con filas vacías): success")
    except AssertionError as e:
        print(f"Error: {e}")

    print("Todas las pruebas para sumar_por_filas han finalizado")

# Llamamos a la función para ejecutar las pruebas
if __name__ == "__main__":
    probar_suma_por_filas()

print("\nPrograma realizado por Maria Vidaurre")




#Codigo para sumar diagonal en matriz
# Definimos la función que suma los elementos de la diagonal principal de una matriz cuadrada
def sumar_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]  # Accede al elemento en la posición (i, i)
    return suma

# Función de prueba para verificar que sumar_diagonal_principal funciona correctamente
def probar_suma_diagonal_principal():
    print("\nPrueba de sumar diagonal")

    # Caso 1: matriz 3x3 con números consecutivos
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    try:
        assert sumar_diagonal_principal(m1) == 15, "Fallo en Caso 1: Matriz 3x3 con números consecutivos"
        print("Caso 1 (Matriz 3x3): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 2: matriz 2x2 con ceros y valores definidos
    m2 = [[10, 0], [0, 20]]
    try:
        assert sumar_diagonal_principal(m2) == 30, "Fallo en Caso 2: Matriz 2x2 con ceros y valores definidos"
        print("Caso 2 (Matriz 2x2): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 3: matriz 1x1
    m3 = [[5]]
    try:
        assert sumar_diagonal_principal(m3) == 5, "Fallo en Caso 3: Matriz 1x1"
        print("Caso 3 (Matriz 1x1): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 4: Matriz con números negativos
    m4 = [[-1, 2], [3, -4]]
    try:
        assert sumar_diagonal_principal(m4) == -5, "Fallo en Caso 4: Matriz con números negativos" # -1 + (-4) = -5
        print("Caso 4 (Matriz con números negativos): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    # Caso 5: Matriz de 4x4
    m5 = [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
    try:
        assert sumar_diagonal_principal(m5) == 10, "Fallo en Caso 5: Matriz 4x4" # 1+2+3+4 = 10
        print("Caso 5 (Matriz 4x4): PASSED")
    except AssertionError as e:
        print(f"Error: {e}")

    print("Todas las pruebas para sumar_diagonal_principal han finalizado")

# Llamamos a la función para ejecutar las pruebas
if __name__ == "__main__":
    probar_suma_diagonal_principal()
print("\nPrograma realizado por Maria Vidaurre")




#Codigo Transponer una Matriz
def transponer_matriz(matriz):
  if not matriz or not matriz[0]:
      return []

  num_filas = len(matriz)
  num_columnas = len(matriz[0])

  # Inicializamos la transpuesta con la estructura correcta
  matriz_transpuesta = []

  for j in range(num_columnas):  # Itera sobre las COLUMNAS originales
      nueva_fila = []
      for i in range(num_filas):  # Itera sobre las FILAS originales
          nueva_fila.append(matriz[i][j])
      matriz_transpuesta.append(nueva_fila)

  return matriz_transpuesta

# Prueba tu función rigurosamente (incluye matrices no cuadradas):
m1 = [[1, 2, 3], [4, 5, 6]]  # 2x3
t1 = transponer_matriz(m1)
assert t1 == [[1, 4], [2, 5], [3, 6]]  # Debe ser 3x2
print("¡Prueba 1 (2x3) pasada! ✅")

# Puedes añadir más pruebas con assert si deseas:
# assert transponer_matriz([[1]]) == [[1]]
# assert transponer_matriz([[1, 2]]) == [[1], [2]]




#Codigo matriz identidad
def es_identidad(matriz):
    # Requisito 1: Debe ser cuadrada
    num_filas = len(matriz)
    if num_filas == 0:
        return True  # Una matriz vacía es trivialmente identidad

    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False  # No es cuadrada

    # Requisito 2: Verificar la diagonal y los ceros
    for i in range(num_filas):
        for j in range(num_filas):
            if i == j:
                if matriz[i][j] != 1:
                    return False  # La diagonal no tiene 1
            else:
                if matriz[i][j] != 0:
                    return False  # Elemento fuera de la diagonal no es 0

    return True  # Cumple con todas las condiciones de matriz identidad

# Prueba tu función:
identidad = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
no_identidad = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
no_cuadrada = [[1, 0], [0, 1], [0, 0]]

assert es_identidad(identidad) == True
assert es_identidad(no_identidad) == False
assert es_identidad(no_cuadrada) == False

print("¡Pruebas para es_identidad pasaron! ✅")




#Codigo Matriz Simetrica
def es_simetrica(matriz):
    # Requisito 1: Debe ser cuadrada
    num_filas = len(matriz)
    if num_filas == 0:
        return True  # Una matriz vacía es trivialmente simétrica

    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False  # No es cuadrada

    # Requisito 2: Comparar matriz[i][j] con matriz[j][i]
    for i in range(num_filas):
        for j in range(i + 1, num_filas):  # Solo necesitamos chequear la triangular superior
            if matriz[i][j] != matriz[j][i]:
                return False  # ¡Con una diferencia es suficiente!

    return True  # Si nunca encontramos diferencias, es simétrica

# Prueba tu función:
sim = [[1, 7, 3], [7, 4, -5], [3, -5, 6]]
no_sim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
no_cuadrada = [[1, 2], [3, 4], [5, 6]]

assert es_simetrica(sim) == True
assert es_simetrica(no_sim) == False
assert es_simetrica(no_cuadrada) == False

print("¡Pruebas para es_simetrica pasaron! ✅")



#Codigo Matriz Identidad
def es_identidad(matriz):
    # Requisito 1: Debe ser cuadrada
    num_filas = len(matriz)
    if num_filas == 0:
        return True  # Una matriz vacía es trivialmente identidad

    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False  # No es cuadrada

    # Requisito 2: Verificar la diagonal y los ceros
    for i in range(num_filas):
        for j in range(num_filas):
            if i == j:
                if matriz[i][j] != 1:
                    return False  # La diagonal no tiene 1
            else:
                if matriz[i][j] != 0:
                    return False  # Elemento fuera de la diagonal no es 0

    return True  # Cumple con todas las condiciones de matriz identidad

# Prueba tu función:
identidad = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
no_identidad = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
no_cuadrada = [[1, 0], [0, 1], [0, 0]]

assert es_identidad(identidad) == True
assert es_identidad(no_identidad) == False
assert es_identidad(no_cuadrada) == False

print("¡Pruebas para es_identidad pasaron! ✅")




#Codigo Matriz Simetrica
def es_simetrica(matriz):
  # Requisito 1: Debe ser cuadrada
  num_filas = len(matriz)
  if num_filas == 0:
      return True  # Una matriz vacía es trivialmente simétrica

  for i in range(num_filas):
      if len(matriz[i]) != num_filas:
          return False  # No es cuadrada

  # Requisito 2: Comparar matriz[i][j] con matriz[j][i]
  for i in range(num_filas):
      for j in range(i + 1, num_filas):  # Solo necesitamos chequear la triangular superior
          if matriz[i][j] != matriz[j][i]:
              return False  # ¡Con una diferencia es suficiente!

  return True  # Si nunca encontramos diferencias, es simétrica

# Prueba tu función:
sim = [[1, 7, 3], [7, 4, -5], [3, -5, 6]]
no_sim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
no_cuadrada = [[1, 2], [3, 4], [5, 6]]

assert es_simetrica(sim) == True
assert es_simetrica(no_sim) == False
assert es_simetrica(no_cuadrada) == False

print("¡Pruebas para es_simetrica pasaron! ✅")


#Codigo Sala Cine
# Crear la sala con precios asignados
def crear_sala(filas, columnas):
    sala = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Asigna un precio según la ubicación (ejemplo simple)
            if 2 <= j <= 5:
                precio = 50  # Asientos centrales
            else:
                precio = 30  # Asientos de los costados
            fila.append({"estado": "L", "precio": precio})
        sala.append(fila)
    return sala

# Mostrar la sala con precios y estados
def mostrar_sala(sala):
    print("\n     " + " ".join(f"{j:^5}" for j in range(len(sala[0]))))
    print("     " + " ".join("─" * 5 for _ in range(len(sala[0]))))
    for i, fila in enumerate(sala):
        estado_fila = " ".join(f"{a['estado']:^5}" for a in fila)
        print(f"F{i:>2} | {estado_fila}")

# Ocupar asiento individual
def ocupar_asiento(sala, fila, columna):
    if 0 <= fila < len(sala) and 0 <= columna < len(sala[0]):
        asiento = sala[fila][columna]
        if asiento["estado"] == "L":
            asiento["estado"] = "O"
            print(f"Asiento ({fila}, {columna}) reservado por Bs. {asiento['precio']}")
            return True
        else:
            print("❌ Ese asiento ya está ocupado.")
            return False
    else:
        print("❌ Coordenadas inválidas.")
        return False

# Buscar N asientos juntos en una fila
def buscar_asientos_juntos(sala, cantidad):
    for i, fila in enumerate(sala):
        consecutivos = 0
        inicio = 0
        for j, asiento in enumerate(fila):
            if asiento["estado"] == "L":
                consecutivos += 1
                if consecutivos == cantidad:
                    return i, j - cantidad + 1  # Fila y columna inicial
            else:
                consecutivos = 0
    return None, None

# Ocupar N asientos juntos si están disponibles
def ocupar_asientos_juntos(sala, cantidad):
    fila, inicio = buscar_asientos_juntos(sala, cantidad)
    if fila is not None:
        total = 0
        for j in range(inicio, inicio + cantidad):
            sala[fila][j]["estado"] = "O"
            total += sala[fila][j]["precio"]
        print(f"🎟️ {cantidad} asientos reservados en fila {fila}, desde columna {inicio}.")
        print(f"💰 Total a pagar: Bs. {total}")
        return True
    else:
        print("❌ No hay suficientes asientos contiguos disponibles.")
        return False

# Contar asientos libres
def contar_asientos_libres(sala):
    return sum(asiento["estado"] == "L" for fila in sala for asiento in fila)

# Programa principal
def main():
    filas, columnas = 5, 8
    sala = crear_sala(filas, columnas)

    while True:
        print("\n🎬 Sala actual:")
        mostrar_sala(sala)
        print(f"Asientos libres: {contar_asientos_libres(sala)}")
        print("\nMenú:")
        print("1. Ocupar asiento individual")
        print("2. Buscar y ocupar N asientos juntos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            try:
                fila = int(input("Fila: "))
                columna = int(input("Columna: "))
                ocupar_asiento(sala, fila, columna)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcion == '2':
            try:
                n = int(input("¿Cuántos asientos necesitas juntos?: "))
                ocupar_asientos_juntos(sala, n)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcion == '0':
            print("Gracias por usar el sistema de reserva de cine. 🎥")
            break
        else:
            print("❌ Opción no válida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()



#Codigo Diccionario
#Diccionario cancion
cancion = {
  "titulo": "Yellow",
  "artista": "Coldplay",
  "album": "Parachutes",
  "duracion_segundos": 266,
  "genero": "Alternative Rock",
  "fecha_lanzamiento": "2000-06-26"
}
print("Información de la canción")
print(f"Título: {cancion['titulo']}")
print(f"Artista: {cancion['artista']}")
print(f"Álbum: {cancion['album']}")
print(f"Duración: {cancion['duracion_segundos']} segundos")
print(f"Género: {cancion['genero']}")
print(f"Fecha de lanzamiento: {cancion['fecha_lanzamiento']}")
#Diccionario de post en red social
post_red_social = {
    "id_post": "P0ST001",
    "autor": "Franz123",
    "contenido_texto": "¡Qué gran día para aprender sobre diccionarios en Python! #Python #Programación #Aprendiendo",
    "lista_de_likes": ["Usuario1", "Usuario2", "Usuario3", "UsuarioEjemplo123"],
    "fecha_publicacion": "2025-06-24 08:45:00"
}

print("Información del Post de Red Social")
print(f"ID del Post: {post_red_social['id_post']}")
print(f"Autor: {post_red_social['autor']}")
print(f"Contenido: {post_red_social['contenido_texto']}")
print(f"Likes: {', '.join(post_red_social['lista_de_likes'])}") 
print(f"Fecha de Publicación: {post_red_social['fecha_publicacion']}")



#  Codigo Inventario
# 1. Crear una lista vacía llamada inventario
inventario = []

# 2. Crear al menos tres diccionarios de productos diferentes
producto1 = {
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "stock": 50
}

producto2 = {
    "nombre": "Café de los Yungas",
    "stock": 100
}

producto3 = {
    "nombre": "Quinua Real en Grano",
    "stock": 80
}

# 3. Añadir los productos al inventario
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# 4. Imprimir cantidad de tipos de producto
print(f"\nCantidad de productos en inventario: {len(inventario)}")

# 5. Recorrer el inventario e imprimir resumen
print("\n--- Inventario Actual ---")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")

#Codigo Key, items
#1 Uso de .keys(): Obtener todas las claves

producto = {
  "codigo": "P001",
  "nombre": "Chocolate para Taza 'El Ceibo'",
  "precio_unitario": 15.50,
  "stock": 50,
  "proveedor": "El Ceibo Ltda."
}

# Mostrar todas las claves
print("Claves del diccionario producto:")
for clave in producto.keys():
  print(f"→ {clave}")

#2 Uso de .keys(): Obtener todas las claves
print("\nValores del diccionario producto:")
for valor in producto.values():
    print(f"→ {valor}")

#3 Uso de .items(): Recorrer clave y valor al mismo tiempo (¡muy útil!)

print("\nContenido completo del diccionario producto:")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")

#4 Verificar si una clave existe usando in
clave_a_verificar = "en_oferta"

if clave_a_verificar in producto:
    print(f"\n🔍 La clave '{clave_a_verificar}' existe con valor: {producto[clave_a_verificar]}")
else:
    print(f"\n❌ La clave '{clave_a_verificar}' no existe.")

# Recuerda que también puedes usar not in para verificar si una clave NO existe
# o eitar un KeyError accediendo a una clave solo si existe
if "stock" in producto:
    print(f"Stock disponible: {producto['stock']} unidades")
else:
    print("No hay información de stock.")

#Aplicado al inventario (con .items())
inventario = [
  {"nombre": "Chocolate para Taza 'El Ceibo'", "stock": 50},
  {"nombre": "Café de los Yungas", "stock": 100},
  {"nombre": "Quinua Real en Grano", "stock": 80}
]

print("\n--- Detalle de productos usando .items() ---")
for producto in inventario:
  for clave, valor in producto.items():
      print(f"{clave} → {valor}")
  print("---")

# Modelado de datos con diccionarios para Canción
cancion = {
  "titulo": "Bohemian Rhapsody",
  "artista": "Queen",
  "album": "A Night at the Opera",
  "duracion_segundos": 354,  # (5 minutos 54 segundos)
  "genero": "Rock Progresivo",
  "es_explicita": False,
  "reproducciones": 275_000_000
}
#"duracion_segundos" es un número entero.
#"es_explicita" es un booleano.
#"reproducciones" usa el separador _ para mejor lectura

# Mostrar los datos
print("🎵 Canción:")
for clave, valor in cancion.items():
  print(f"{clave}: {valor}")

# Modelado de datos con diccionarios para Coche
coche = {
  "marca": "Toyota",
  "modelo": "Corolla Cross",
  "año": 2023,
  "color": "Gris Metálico",
  "placa": "5923-LLT",
  "kilometraje": 17450.6,
  "en_venta": True
}
#"kilometraje" es un número decimal.
#"año" es un entero.
#"en_venta" es booleano.

# Mostrar los datos
print("\n🚗 Coche:")
for clave, valor in coche.items():
  print(f"{clave}: {valor}")

# Modelado de datos con diccionarios para Post de Red Social
post_red_social = {
  "id_post": "POST-20250622-001",
  "autor": "jimmy.requena",
  "contenido_texto": "¡Hoy lanzamos nuestro nuevo ERP con IA! 🚀",
  "lista_de_likes": ["ana_123", "dev.mario", "claudia77"],
  "fecha_publicacion": "2025-06-22",
  "es_publico": True,
  "hashtags": ["#IA", "#ERP", "#ProductLaunch"]
}

# Mostrar los datos
print("\n📱 Post en Red Social:")
for clave, valor in post_red_social.items():
  print(f"{clave}: {valor}")
post_red_social = {
  "id_post": "POST-20250622-001",
  "autor": "jimmy.requena",
  "contenido_texto": "¡Hoy lanzamos nuestro nuevo ERP con IA! 🚀",
  "lista_de_likes": ["ana_123", "dev.mario", "claudia77"],
  "fecha_publicacion": "2025-06-22",
  "es_publico": True,
  "hashtags": ["#IA", "#ERP", "#ProductLaunch"]
}
#"lista_de_likes" y "hashtags" son listas de strings.
#"fecha_publicacion" es un string con formato de fecha.
#"es_publico" es booleano.

# Mostrar los datos
print("\n📱 Post en Red Social:")
for clave, valor in post_red_social.items():
  print(f"{clave}: {valor}")

# Probando si existe una clave
if "autor" in post_red_social:
  print(f"\n✅ Autor del post: {post_red_social['autor']}")
else:
  print("❌ Este post no tiene autor definido.")





#Codigo To Do List
# Paso 1: Variables Globales
lista_de_tareas = []
proximo_id_tarea = 1  # Para generar IDs únicos

# Paso 2: Implementar agregar_tarea
def agregar_tarea(descripcion, prioridad='media'):
    global proximo_id_tarea
    nueva_tarea = {
        "id": proximo_id_tarea,
        "descripcion": descripcion,
        "completada": False,
        "prioridad": prioridad
    }
    lista_de_tareas.append(nueva_tarea)
    proximo_id_tarea += 1
    print(f"✅ Tarea '{descripcion}' añadida con éxito.")

# Paso 3: Implementar mostrar_tareas
def mostrar_tareas():
    print("\n--- 📋 LISTA DE TAREAS ---")
    if not lista_de_tareas:
        print("¡No hay tareas pendientes! ¡A disfrutar!")
        return
    for tarea in lista_de_tareas:
        estado = "✅" if tarea["completada"] else "⬜"
        print(f"{estado} ID: {tarea['id']} | {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")

# Paso 4: Implementar buscar_tarea_por_id
def buscar_tarea_por_id(id_buscado):
    for tarea in lista_de_tareas:
        if tarea["id"] == id_buscado:
            return tarea
    return None

# Paso 5: Implementar marcar_tarea_completada
def marcar_tarea_completada(id_tarea):
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        tarea["completada"] = True
        print(f"✅ Tarea '{tarea['descripcion']}' marcada como completada.")
    else:
        print(f"❌ Error: No se encontró la tarea con ID {id_tarea}.")

# Paso 6: Implementar eliminar_tarea
def eliminar_tarea(id_tarea):
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        lista_de_tareas.remove(tarea)
        print(f"✅ Tarea '{tarea['descripcion']}' eliminada.")
    else:
        print(f"❌ Error: No se encontró la tarea con ID {id_tarea}.")

# Paso 7: El Bucle Principal del Programa
while True:
    print("\n==== MENÚ TO-DO LIST ====")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        desc = input("Descripción de la nueva tarea: ")
        prio = input("Prioridad (alta, media, baja): ")
        agregar_tarea(desc, prio)
    elif opcion == '2':
        mostrar_tareas()
    elif opcion == '3':
        id_t = int(input("ID de la tarea a completar: "))
        marcar_tarea_completada(id_t)
    elif opcion == '4':
        id_t = int(input("ID de la tarea a eliminar: "))
        eliminar_tarea(id_t)
    elif opcion == '0':
        print("¡Hasta pronto!")
        break
    else:
        print("❌ Opción no válida. Inténtalo de nuevo.")



#Codigo Batalla Naval
import random

FILAS = 4
COLUMNAS = 2
BARCOS = 3

# Crear un tablero vacío
def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Mostrar el tablero
def mostrar_tablero(tablero, ocultar_barcos=False):
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        fila_mostrar = []
        for celda in fila:
            if ocultar_barcos and celda == 1:
                fila_mostrar.append("0")
            elif celda == 0:
                fila_mostrar.append("0")
            elif celda == 1:
                fila_mostrar.append("1")
            elif celda == 2:
                fila_mostrar.append("X")
            elif celda == 3:
                fila_mostrar.append("*")
        print(letra + " " + " ".join(fila_mostrar))

# Convertir coordenada tipo "A3" a índices [fila][columna]
def coord_a_indices(coord):
    fila = ord(coord[0].upper()) - ord('A')
    columna = int(coord[1:]) - 1
    return fila, columna

# Colocar barcos aleatoriamente
def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1

# Ejecutar disparo
def disparar(tablero_objetivo, tablero_disparos, coord, nombre):
    fila, columna = coord_a_indices(coord)
    if tablero_objetivo[fila][columna] == 1:
        tablero_objetivo[fila][columna] = 2
        tablero_disparos[fila][columna] = 2
        print(f"{nombre} hizo ¡Tocado!")
    elif tablero_objetivo[fila][columna] in [0]:
        tablero_objetivo[fila][columna] = 3
        tablero_disparos[fila][columna] = 3
        print(f"{nombre} disparó al agua.")
    else:
        print("Ya se disparó allí.")

# Comprobar si quedan barcos
def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False

# Guardar puntuación
def guardar_puntuacion(nombre):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre} ganó la partida.\n")

# Menú principal del juego
def juego():
    print("=== Batalla Naval ===")
    print("1. Jugar contra la CPU")
    print("2. Jugar contra otro jugador")
    modo = input("Selecciona modo (1 o 2): ")

    if modo == "1":
        nombre_jugador = input("Tu nombre: ")
        nombre_cpu = "CPU"

        tablero_jugador = crear_tablero()
        tablero_cpu = crear_tablero()
        disparos_jugador = crear_tablero()
        disparos_cpu = crear_tablero()

        colocar_barcos(tablero_jugador, BARCOS)
        colocar_barcos(tablero_cpu, BARCOS)

        turno = 1
        while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu):
            print(f"\n--- Turno {turno} ---")
            print("Tu tablero:")
            mostrar_tablero(tablero_jugador)
            print("Tus disparos:")
            mostrar_tablero(disparos_jugador)

            coord = input("Dispara (ej. A3): ")
            disparar(tablero_cpu, disparos_jugador, coord, nombre_jugador)

            # Turno CPU
            while True:
                fila_cpu = random.randint(0, FILAS - 1)
                col_cpu = random.randint(0, COLUMNAS - 1)
                if tablero_jugador[fila_cpu][col_cpu] in [0, 1]:
                    break
            coord_cpu = f"{chr(ord('A') + fila_cpu)}{col_cpu + 1}"
            print(f"{nombre_cpu} dispara a {coord_cpu}")
            disparar(tablero_jugador, disparos_cpu, coord_cpu, nombre_cpu)
            turno += 1

        if quedan_barcos(tablero_jugador):
            print(f"¡{nombre_jugador} gana!")
            guardar_puntuacion(nombre_jugador)
        else:
            print("¡La CPU gana!")

    elif modo == "2":
        nombre1 = input("Nombre del Jugador 1: ")
        nombre2 = input("Nombre del Jugador 2: ")

        tablero1 = crear_tablero()
        tablero2 = crear_tablero()
        disparos1 = crear_tablero()
        disparos2 = crear_tablero()

        colocar_barcos(tablero1, BARCOS)
        colocar_barcos(tablero2, BARCOS)

        turno = 1
        while quedan_barcos(tablero1) and quedan_barcos(tablero2):
            print(f"\n--- Turno {turno} ---")

            print(f"{nombre1}, este es tu turno")
            mostrar_tablero(disparos1)
            coord = input("Dispara (ej. A3): ")
            disparar(tablero2, disparos1, coord, nombre1)

            if not quedan_barcos(tablero2):
                break

            print(f"\n{nombre2}, este es tu turno")
            mostrar_tablero(disparos2)
            coord = input("Dispara (ej. A3): ")
            disparar(tablero1, disparos2, coord, nombre2)

            turno += 1

        if quedan_barcos(tablero2):
            print(f"¡{nombre1} gana!")
            guardar_puntuacion(nombre1)
        else:
            print(f"¡{nombre2} gana!")
            guardar_puntuacion(nombre2)
    else:
        print("Opción inválida. Reinicia el programa.")

# Ejecutar juego
juego()



#Codigo agenda, gestor de contactos
# Diccionario principal donde las claves son nombres y los valores son diccionarios con info del contacto
agenda = {}

def agregar_contacto(nombre, telefonos, email):
    """
    Agrega un nuevo contacto a la agenda.
    telefonos: lista de números (puede tener uno o más).
    """
    if nombre in agenda:
        print(f"El contacto '{nombre}' ya existe.")
        return
    agenda[nombre] = {
        'telefonos': telefonos,
        'email': email
    }
    print(f"Contacto '{nombre}' agregado.")

def buscar_por_nombre(nombre):
    """
    Busca y devuelve la información del contacto por nombre.
    """
    return agenda.get(nombre, None)

def editar_contacto(nombre, telefonos=None, email=None):
    """
    Edita los datos de un contacto existente.
    Solo actualiza los campos que se pasen.
    """
    if nombre not in agenda:
        print(f"El contacto '{nombre}' no existe.")
        return
    if telefonos is not None:
        agenda[nombre]['telefonos'] = telefonos
    if email is not None:
        agenda[nombre]['email'] = email
    print(f"Contacto '{nombre}' actualizado.")

def mostrar_contacto(nombre):
    contacto = buscar_por_nombre(nombre)
    if contacto:
        print(f"Nombre: {nombre}")
        print(f"Teléfonos: {', '.join(contacto['telefonos'])}")
        print(f"Email: {contacto['email']}")
    else:
        print(f"No se encontró el contacto '{nombre}'.")

# Ejemplo de uso:
agregar_contacto('Juan Pérez', ['555-1234', '555-5678'], 'juan@example.com')
mostrar_contacto('Juan Pérez')

editar_contacto('Juan Pérez', email='juanperez@nuevoemail.com')
mostrar_contacto('Juan Pérez')
