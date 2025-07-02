# Ejercicio 1: Crear y escribir en un archivo de texto llamado "mi_diario.txt"

# Paso 1: Definimos el nombre del archivo
nombre_archivo = "mi_diario.txt"

# Paso 2: Usamos 'with open(...)' en modo escritura ('w')
# Esto Crea el archivo si no existe, y lo sobreescribe si ya existe.
with open(nombre_archivo, "w") as diario_file:
    # Paso 3: Escribimos varias líneas en el archivo usando .write()
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
    diario_file.write("¡Pero también es muy útil para comenzar desde cero!\n")

# Paso 4: Confirmamos que se ha terminado de escribir
print("✅ Diario creado y primeras entradas guardadas.")

# Ejercicio 2: Leer el contenido del diario después de escribirlo

# Opción A: Leer todo de golpe (menos recomendada porque no separa líneas bien al mostrar)
# La dejamos comentada como referencia didáctica

# with open(nombre_archivo, "r") as diario_file:
#     contenido = diario_file.read()
# print("\n--- Contenido completo del diario (modo A) ---")
# print(contenido)

# Opción B: Leer línea por línea (más clara y controlada)
print("\n--- Contenido del diario (línea por línea) ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())  # .strip() elimina el salto de línea al final
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# Ejercicio 2: Leer el contenido del archivo "mi_diario.txt"
# Probamos dos formas: opción A (leer todo) y opción B (leer línea por línea)

# ------------------------------
# 🔹 Opción A: Leer todo de golpe
# ------------------------------
# Esta opción carga todo el contenido del archivo como un solo string
# Útil si queremos procesar o mostrar todo junto

print("\n--- Contenido completo del diario (modo A - read()) ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        contenido = diario_file.read()  # Lee todo el contenido de una sola vez
    print(contenido)
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# -----------------------------------
# 🔸 Opción B: Leer línea por línea
# -----------------------------------
# Esta opción permite manejar cada línea por separado
# Ideal para procesar o mostrar contenido ordenado, sin saltos extra

print("\n--- Contenido del diario (modo B - línea por línea) ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())  # Eliminamos los '\n' del final para una impresión limpia
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# Ejercicio 3: Añadir nuevas entradas al archivo sin borrar lo anterior (modo 'a')

print("\n📝 Añadiendo nuevas entradas al diario...")

# Abrimos el archivo en modo añadir ('a')
with open(nombre_archivo, "a") as diario_file:
    # Escribimos nuevas líneas. También podemos añadir una línea separadora.
    diario_file.write("\n--- Entrada del 20 de Junio de 2025 ---\n")
    diario_file.write("El modo 'a' es genial para no perder datos.\n")
    diario_file.write("Ahora mi diario puede crecer cada día.\n")

# Confirmamos que se añadieron las nuevas entradas
print("✅ Nuevas entradas guardadas.")

# Verificamos que las nuevas entradas se añadieron correctamente
print("\n📖 Verificando el contenido final del diario...")

try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# --------------------------------------
# ✅ Ejercicio 1: Crear y escribir diario
# --------------------------------------

# Paso 1: Definimos el nombre del archivo
nombre_archivo = "mi_diario.txt"

# Paso 2: Creamos el archivo desde cero (modo 'w') y escribimos líneas predefinidas
with open(nombre_archivo, "a") as diario_file:
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
    diario_file.write("¡Pero también es muy útil para comenzar desde cero!\n")

# Confirmamos al usuario
print("✅ Diario creado y primeras entradas guardadas.")

# --------------------------------------
# ✅ Ejercicio 2: Leer el diario (modo A y B)
# --------------------------------------

# Opción A: Leer todo el contenido de una sola vez
print("\n--- Contenido completo del diario (modo A - read()) ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        contenido = diario_file.read()
    print(contenido)
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# Opción B: Leer el archivo línea por línea (más controlado)
print("\n--- Contenido del diario (modo B - línea por línea) ---")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())  # .strip() elimina los saltos de línea '\n'
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

# --------------------------------------
# ✅ Ejercicio 3: Añadir entrada desde input()
# --------------------------------------

# Aquí el usuario puede ingresar su propia entrada personalizada
print("\n📝 Vamos a añadir una nueva entrada a tu diario.")
print("Escribe tu entrada (usa varias líneas si quieres). Escribe una línea vacía para terminar.")

# Usamos una lista para recoger múltiples líneas del usuario
lineas_usuario = []
while True:
    linea = input()
    if linea == "":
        break  # Al ingresar una línea vacía, se termina la entrada
    lineas_usuario.append(linea)

# Añadimos las nuevas líneas al diario, en modo 'a' para no borrar lo anterior
print("\n✍️ Añadiendo tu entrada al diario...")
with open(nombre_archivo, "a") as diario_file:
    diario_file.write("\n--- Nueva entrada personalizada ---\n")
    for linea in lineas_usuario:
        diario_file.write(linea + "\n")

print("✅ ¡Tu entrada fue añadida con éxito!")

# --------------------------------------
# ✅ Verificación final: Leer todo el contenido actualizado
# --------------------------------------

print("\n📖 Verificando el contenido final del diario (modo B)...")
try:
    with open(nombre_archivo, "r") as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")


class Libro:
    """
    Clase que representa un libro con sus atributos principales.
    """

    def __init__(self, titulo, autor, isbn, paginas):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            isbn (str): ISBN del libro
            paginas (int): Número de páginas del libro
        """
        # Crear los atributos de instancia correspondientes
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas

        # Atributo extra que se inicializa siempre por defecto
        self.disponible = True

    def mostrar_info(self):
        """
        Método que imprime todos los atributos del libro de forma clara y formateada.
        """
        print("=" * 50)
        print("INFORMACIÓN DEL LIBRO")
        print("=" * 50)
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print("=" * 50)


# Ejemplo de uso (no te preocupes por crear objetos todavía, ¡solo define la clase!)
if __name__ == "__main__":
    # Creación de ejemplo para demostrar el funcionamiento
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 417)
    libro1.mostrar_info()

    # Cambiar disponibilidad
    libro1.disponible = False
    print("\nDespués de cambiar disponibilidad:")
    libro1.mostrar_info()


# Ejercicio 2: Creación de instancias y métodos de comportamiento

class Libro:
    """
    Clase que representa un libro con sus atributos principales.
    """

    def __init__(self, titulo, autor, isbn, paginas):
        """
        Constructor de la clase Libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.disponible = True

    def mostrar_info(self):
        """
        Método que imprime todos los atributos del libro de forma clara y formateada.
        """
        print("=" * 50)
        print("INFORMACIÓN DEL LIBRO")
        print("=" * 50)
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print("=" * 50)

    def prestar_libro(self):
        """
        Método para prestar el libro. Cambia disponible a False si está disponible.
        """
        if self.disponible == True:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver_libro(self):
        """
        Método para devolver el libro. Cambia disponible a True si estaba prestado.
        """
        if self.disponible == False:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")


# 1. Definición de clase Libro (arriba) ✓

# 2. Crear dos objetos Libro diferentes
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-3-14-046401-7", 120)
libro2 = Libro("Raza de Bronce", "Alcides Arguedas", "978-99905-2-213-9", 250)

# 3. Acceder y mostrar algunos de sus atributos directamente
print(f"\nEl autor del primer libro es: {libro1.autor}")
print(f"El ISBN del segundo libro es: {libro2.isbn}")

# 4. Llamar al método mostrar_info() para cada uno de los objetos
print("\n--- Mostrando información completa ---")
libro1.mostrar_info()
libro2.mostrar_info()

# 5. Añadir métodos de comportamiento (ya implementados arriba) ✓

# 6. Prueba los nuevos métodos con tus objetos libro1 y libro2
print("\n--- Probando métodos de comportamiento ---")

# Prestar libro1
libro1.prestar_libro()

# Intentar prestar libro1 otra vez (ya prestado)
libro1.prestar_libro()

# Devolver libro1
libro1.devolver_libro()

# Intentar devolver libro1 otra vez (ya disponible)
libro1.devolver_libro()

print("\n--- Probando con libro2 ---")

# Prestar libro2
libro2.prestar_libro()

# Devolver libro2
libro2.devolver_libro()

print("\n--- Estado final de los libros ---")
libro1.mostrar_info()
libro2.mostrar_info()


class Libro:
  """
  Clase que representa un libro con sus atributos principales.
  """

  def __init__(self, titulo, autor, isbn, paginas):
      """
      Constructor de la clase Libro.

      Args:
          titulo (str): Título del libro
          autor (str): Autor del libro
          isbn (str): ISBN del libro
          paginas (int): Número de páginas del libro
      """
      self.titulo = titulo
      self.autor = autor
      self.isbn = isbn
      self.paginas = paginas
      self.disponible = True

  def mostrar_info(self):
      """
      Método que imprime todos los atributos del libro de forma clara y formateada.
      """
      print("=" * 50)
      print("INFORMACIÓN DEL LIBRO")
      print("=" * 50)
      print(f"Título: {self.titulo}")
      print(f"Autor: {self.autor}")
      print(f"ISBN: {self.isbn}")
      print(f"Páginas: {self.paginas}")
      print(f"Disponible: {'Sí' if self.disponible else 'No'}")
      print("=" * 50)


if __name__ == "__main__":
  # Crear objetos de tipo Libro
  libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 417)
  libro2 = Libro("1984", "George Orwell", "978-0451524935", 328)
  libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0156013987", 96)

  # Crear una lista vacía
  mi_biblioteca = []

  # Añadir libros a la lista
  mi_biblioteca.append(libro1)
  mi_biblioteca.append(libro2)
  mi_biblioteca.append(libro3)

  # Mostrar el inventario completo
  print("\n\n--- INVENTARIO COMPLETO DE LA BIBLIOTECA ---")
  for libro_actual in mi_biblioteca:
      libro_actual.mostrar_info()
      print("=" * 20)  # Separador
