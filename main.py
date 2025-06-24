# Código de que peliculas puedes ver en el cine
edad_str = input("Bienvenido al cine, ¿cuál es tu edad?: ")
edad = int(edad_str)

if edad < 0:
    print("Edad no válida. Por favor, ingresa un número positivo.")
elif edad >= 18:
    print("¡Puedes ver películas clasificadas R!")
elif edad >= 13:  # Python llega aquí solo si edad NO es >= 18 y NO es < 0
    print("Puedes ver películas clasificadas PG-13.")
else:  # Si no es < 0, ni >= 18, ni >= 13, entonces debe ser < 13 y >= 0
    print("Te recomendamos películas clasificadas G o P.")

print("\n")

# Código de la tabla de multiplicar
num_tabla = int(input("Ingresa un número para ver su tabla de multiplicar: "))
print(f"--- Tabla del {num_tabla} ---")

for i in range(1, 11):  # i tomará valores de 1 a 10
    resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado}")


#Código bucle for
numeroenteroposit = int(input("Ingresa un número entero positivo: "))
print(f"Contando hasta {numeroenteroposit} (sin incluirlo):")
for numero in range(numeroenteroposit): 
         # range(n) genera números desde 0 hasta n-1
    print(numero, end=" ")


#Codigo de refactorizacion (incluimos variables y listas) rectangulo
def calcular_area_rectangulo(base, altura):
    return base * altura

rectangulos = []  #es una variable para almacenar los datos de los rectangulos
contador = 1   #es la variable para contar los rectangulos

while True:
    base = int(input("Ingrese la base del rectángulo: "))
    altura = int(input("Ingrese la altura del rectángulo: "))
    area = calcular_area_rectangulo(base, altura)
    rectangulos.append((contador, base, altura, area)) #el append te permite agregar elementos a la lista
    print(f"El área del rectángulo {contador} ({base}x{altura}) es: {area}")
    contador += 1

    continuar = input("¿Desea ingresar otro rectángulo? Presione Enter para continuar o 'n' para salir: ")
    if continuar.lower() == 'n':
        break

ver_datos = input("¿Desea ver los datos de los rectángulos guardados? Presione 1 para ver: ")
if ver_datos == '1':
    for rectangulo in rectangulos:
        numero, base, altura, area = rectangulo
        print(f"Rectángulo {numero}: Base = {base}, Altura = {altura}, Área = {area}")



#Codigo bucle while
contador = 0
numero = int(input("Introduce un número entero: "))
print("\nBucle while:")
while contador < numero:  # la condición depende del número ingresado
    print(f"Contador es: {contador}")
    contador = contador + 1  # Actualiza la variable de control(contador)
print("¡El bucle while ha terminado!")



# Código del juego adivina el número secreto
# El número secreto ahora es fijo: 6 pero puede ser cambiado por cualquier otro número entero.
numero_secreto = 6

print("¡Bienvenido al juego Adivina el Número Secreto!")
print("Estoy pensando en el...")

# Iniciamos la variable adivinanza con un valor diferente al número secreto para que el bucle WHILE se ejecute al menos una vez.
adivinanza = 0 

# Bucle que continua mientras la adivinanza no sea correcta
while adivinanza != numero_secreto:
    try:
        # Pide al usuario que adivine el número.
        adivinanza = int(input("Ingresa el número que crees que es el secreto: "))

        # Aqui le damos una pista si el número no es correcto
        if adivinanza > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        elif adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")

    except ValueError:
        # Maneja el error si el usuario no ingresa un número entero (int)
        print("Ingresa un número entero.")

# Mensaje (print)que aparece cuando el número fue adivinado
print(f"¡Correcto! El número era {numero_secreto}. ¡Felicidades, adivinaste!")



#Codigo lista de comidas bolivianas favoritas
 # Crea una lista llamada comidas_favoritas con los nombres (strings) de tus 3 comidas bolivianas favoritas.
comidas_favoritas = ["Pollo Frito", "Pique Macho", "Milanesa"]

# Imprimimos la lista completa para verificar que se creó bien.
print("Mi lista de comidas favoritas es:")
print(comidas_favoritas)

# Imprime un mensaje que diga: "Mi segunda comida favorita es: [el nombre de la segunda comida]".
print(f"\nMi segunda comida favorita es: {comidas_favoritas[1]}")

# Usamos len() al imprimir un mensaje 
# len() nos dara la cantidad de elementos en la lista.
print(f"Mi lista de comidas favoritas tiene {len(comidas_favoritas)} elementos.")



#Codigo para calcular el promedio de notas
# Creamos una lista llamada lista_mis_notas con las notas numéricas.
lista_mis_notas = [60.5, 74, 80.5, 90.5,]
# Creamos una variable suma_total inicializada en 0.
suma_total = 0

# Usamos un bucle for para recorrer lista_mis_notas.
# En cada iteración, añade la nota actual a suma_total.
for nota in lista_mis_notas:
    suma_total = suma_total + nota 

# Calcula el promedio: promedio = suma_total / len(lista_mis_notas).
# len(lista_mis_notas) nos da la cantidad de elementos en la lista.
promedio = suma_total / len(lista_mis_notas)

# Imprime(print) la suma total y el promedio.
print(f"Mis notas son: {lista_mis_notas}")
print(f"La suma total de las notas es: {suma_total:.2f}") 
print(f"El promedio de las notas es: {promedio:.2f}") # :.2f para mostrar dos decimales



# codigo acumulador suma
def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for numero in lista_numeros:
        acumulador_suma += numero  
    return acumulador_suma
mis_numeros = [10, 5, 20, 15, 8, 25]
resultado_suma = sumar_elementos(mis_numeros)

print(f"La lista de números es: {mis_numeros}")
print(f"La suma total es: {resultado_suma}")


# Codigo para sumar todos los elementos de una lista
def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for numero in lista_numeros:
        acumulador_suma += numero
    return acumulador_suma

# --- Casos de Prueba con assert y manejo de errores ---
print("Iniciando pruebas de la función 'sumar_elementos'...")
pruebas_pasadas = 0
total_pruebas = 0

# Prueba 1: Suma básica
total_pruebas += 1
try:
    assert sumar_elementos([1, 2, 3, 4, 5]) == 15
    print("✅ Prueba 1 (Suma básica): Pasó")
    pruebas_pasadas += 1
except AssertionError:
    print("❌ Prueba 1 (Suma básica): ¡Falló! El resultado no fue 15.")

# Prueba 2: Con números negativos
total_pruebas += 1
try:
    assert sumar_elementos([10, -2, 5]) == 13
    print("✅ Prueba 2 (Con números negativos): Pasó")
    pruebas_pasadas += 1
except AssertionError:
    print("❌ Prueba 2 (Con números negativos): ¡Falló! El resultado no fue 13.")

# Prueba 3: Lista vacía
total_pruebas += 1
try:
    assert sumar_elementos([]) == 0
    print("✅ Prueba 3 (Lista vacía): Pasó")
    pruebas_pasadas += 1
except AssertionError:
    print("❌ Prueba 3 (Lista vacía): ¡Falló! El resultado no fue 0.")

# Prueba 4: Un solo elemento
total_pruebas += 1
try:
    assert sumar_elementos([100]) == 100
    print("✅ Prueba 4 (Un solo elemento): Pasó")
    pruebas_pasadas += 1
except AssertionError:
    print("❌ Prueba 4 (Un solo elemento): ¡Falló! El resultado no fue 100.")

print(f"\nResumen de pruebas: {pruebas_pasadas} de {total_pruebas} pruebas pasaron exitosamente.")
if pruebas_pasadas == total_pruebas:
    print("¡Todas las pruebas pasaron exitosamente! Nuestra función es robusta.")
else:
    print("¡Advertencia! Algunas pruebas fallaron. Revisa tu función.")


# --- Uso principal de la función ---
print("\n--- Demostración con tu lista ---")
mis_numeros = [10, 5, 20, 15, 8, 25]
resultado_suma = sumar_elementos(mis_numeros)

print(f"La lista de números es: {mis_numeros}")
print(f"La suma total es: {resultado_suma}")

print("Codigo realizado por: Maria F. Vidaurre Alvarado")






#Codigo encontrar mayor o numero mas grande en lista
lista_numeros_grande = [45, 12, 78, 33, 90, 67, 21]
if not lista_numeros_grande:
    print("La lista está vacía, no se puede encontrar el número más grande.")
else:
    mayor_temporal = lista_numeros_grande[0]
    for i in range(1, len(lista_numeros_grande)):
        elemento_actual = lista_numeros_grande[i]
        if elemento_actual > mayor_temporal:
            mayor_temporal = elemento_actual
    print(f"\nLa lista de números es: {lista_numeros_grande}")
    print(f"El número más grande en la lista es: {mayor_temporal}")




#Codigo de contador en lista (cuantas veces aparece un elemento en una lista)
def contar_repeticiones(lista, elemento_buscado):
    contador = 0
    for elemento in lista:
        if elemento == elemento_buscado:
            contador += 1
    return contador

mi_lista = [1, 2, 3, 2, 4, 5, 2, 6, 7, 2, 8, 9, 2, 10]
elemento_a_buscar = 2

resultado = contar_repeticiones(mi_lista, elemento_a_buscar)

print(f"El número {elemento_a_buscar} aparece {resultado} veces en la lista.")




#Codigo de Invertir lista con range, append
def invertir_lista(lista_original):
    lista_invertida = []
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])
    return lista_invertida



#Codigo de busqueda lineal(hecho en prog1)(quitar luego)
def busqueda_lineal(lista, elemento_buscado):
    for i in range(len(lista)):
        if lista[i] == elemento_buscado:
            return i
    return -1
# lista de prueba de números
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# El número que estamos buscando
numero_buscado = 8
# Llamamos a la función de búsqueda lineal
indice_encontrado = busqueda_lineal(mi_lista, numero_buscado)
# Imprimimos el resultado
if indice_encontrado != -1:
    print(f"El número {numero_buscado} se encontró en el índice: {indice_encontrado}")
else:
    print(f"El número {numero_buscado} no se encontró en la lista.")




#Codigo de busqueda lineal
    def busqueda_lineal(lista, elemento_buscado):
        for i in range(len(lista)):
            if lista[i] == elemento_buscado:
                return i
        return -1

    mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elemento_buscado = 8
    #sustiui clave por elemento_buscado
    indice_encontrado = busqueda_lineal(mi_lista, elemento_buscado)

    if indice_encontrado != -1:
        print(f"El elemento {elemento_buscado} se encontró en el índice: {indice_encontrado}")
    else:
        print(f"El elemento {elemento_buscado} no se encontró en la lista.")





#Codigo de busqueda binaria
def busqueda_binaria(lista_ordenada, clave):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista_ordenada[medio] == clave:
            return medio
        elif clave > lista_ordenada[medio]:
            izquierda = medio + 1
        else:
            derecha = medio - 1      
    return -1
# lista de prueba xd
lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91] 
# Cuando la clave es encontrada o no
clave_buscada_1 = 23
indice_1 = busqueda_binaria(lista_ordenada, clave_buscada_1)
if indice_1 != -1:
    print(f"La clave {clave_buscada_1} se encontró en el índice: {indice_1}")
else:
    print(f"La clave {clave_buscada_1} no se encontró en la lista.")



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

    print("\nPrograma realizado por Maria F. Vidaurre Alvarado")






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


#




#Matrices
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

print("\nPrograma realizado por Maria F. Vidaurre Alvarado")




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
print("\nPrograma realizado por Maria F. Vidaurre Alvarado")




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
print("\nPrograma realizado por Maria F. Vidaurre Alvarado")