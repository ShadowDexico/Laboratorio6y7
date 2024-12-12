#1. Sintaxis Básica y Operaciones Simples
def SintaxisBasica():
    print("hola mundo")
    Entero = 10
    Flotante = 3.5
    texto = "Fernando"

    Resultado = Entero + Flotante

    print("Oye, ", texto, " El resultado de la suma de ", Flotante, " Y ", Entero, " Es: ", Resultado)

    Respuesta = input("Te gustó la experiencia?")

    if Respuesta == "No":
        print("chao pues")
    elif Respuesta == "Si":
        print("Gracias :D")
    else:
        print("Es Si y No")
    print("")

#2. Condicionales y Bucles
def CondicionalesYbucles():
    num = int(input("Introduce un numero para determinar si es par o impar: "))

    if num % 2 == 0:
        print("El numero es par.")
    else:
        print("El numero es impar.")

    print("")

    numeros = [1, 2, 3, 4, 5]
    for num in numeros:
        print(f"El cuadrado de {num} es {num**2}")
    print("")

#3. Lista y Diccionarios
ListaEstudiantes = []
Contactos = {}

def AgregarEstudiantes():
    NewEstudiante = input("Introduce el nombre del nuevo estudiante: ")
    ListaEstudiantes.append(NewEstudiante)
    print("Estudiante registrado")

def AgregarContactos(Diccionario):
    Nombre = input("Introduce el nombre: ")
    Apellido = input("Introduce el apellido: ")
    TipoDocumento = input("Introduce el tipo de documento: ")
    NumeroDocumento = input("Introduce el numero de documento: ")

    Diccionario[Nombre] = {
        'apellido': Apellido,
        'tipo_documento': TipoDocumento,
        'numero_documento': NumeroDocumento
    }
    print(f"Contacto '{Nombre} {Apellido}' ha sido agregado al diccionario.")

def ListaYdiccionario():
    while True:
        print("\nOpciones:")
        print("1. Agregar estudiante")
        print("2. Agregar Contacto")
        print("3. Ver estudiantes")
        print("4. Ver información de contacto")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            AgregarEstudiantes()
        elif opcion == "2":
            AgregarContactos(Contactos)
        elif opcion == "3":
            print("Lista de estudiantes")
            print("")
            for Estudiante in ListaEstudiantes:
                print(Estudiante)
        elif opcion == "4":
            print("")
            print("Lista del contacto")
            print("")
            for clave, valor in Contactos.items():
                print(f"{clave}: {valor}")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

#4. Script de Resolución de Problemas Simples
def Adivinanza():
    import random

    num = random.randint(1, 100)
    Acierto = False

    while not Acierto:
        intento = int(input("Adivina el número entre 1 y 100: "))
        if intento < num:
            print("El número es mayor.")
        elif intento > num:
            print("El número es menor.")
        else:
            print("¡Adivinaste el número!")
            Acierto = True


def Menu():
    while True:
        print("\nOpciones del menú:")
        print("1. Sintaxis básica y operaciones simples")
        print("2. Condicionales y bucles")
        print("3. Listas y diccionarios")
        print("4. Resolución de problemas simples")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            SintaxisBasica()
        elif opcion == "2":
            CondicionalesYbucles()
        elif opcion == "3":
            ListaYdiccionario()
        elif opcion == "4":
            Adivinanza()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige una opción entre 1 y 5")

Menu()
