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