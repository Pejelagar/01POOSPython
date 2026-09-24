#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from paciente import Paciente
import paciente
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
pacientes:list[Paciente]=[
    Paciente("11.111.111-1","Gaspar Galves",30,"Fonasa"),
    Paciente("22.222.222-2","Boris Navarro",25,"Isapre")
]
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("!): Debe ingresar un número entero.")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def menu():
    print("=" * 20)
    print("Menú Clínica")
    print("=" * 20)
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar un paciente")
    print("5.- Mostrar todos los pacientes")
    print("0.- Salir")
    op = leer_numero("Ingrese una opción:")
    print("=" * 20)
    return op
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def agregar_paciente():
    rut = input("Ingrese RUT del paciente: ")
    nombre = input("Ingrese nombre del paciente: ")
    edad = leer_numero("Ingrese edad del paciente: ")
    print("Tipo de previsión del paciente: ")
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro")
    op=leer_numero("Seleciona una previsión del paciente:")
    if op == 1:
        prevision="Fonasa"
    elif op == 2:
        prevision="Isapre"
    elif op == 3:
        prevision="Particular"
    elif op == 4:
        prevision="Otro"
    else:
        print("Opción Inválida")

    paciente=Paciente(rut,nombre,edad,prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente")
    print(f"Total pacientes registrados:{len(pacientes)}")
    input("Enter para continuar...")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def imprimir_pacientes()->None:
    if len(pacientes) == 0:
        print("No hay pacientes.")
    else:
        for paciente in pacientes:
            print(paciente)
            print("-" * 20)
    input("Enter para continuar...")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def buscar_paciente()->paciente:
    rut = input("Ingrese el rut del paciente: ")
    for p in pacientes:
        if p.rut == rut:
            return p
        
    return None
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def imprimir_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("No se encontró el paciente.")
    input("Enter para continuar...")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        pacientes.remove(paciente)
        print("Paciente eliminado.")
    else:
        print("No me encontraras. No me pondras las manos encima. Ríndete. Césa tu vana búsqueda y abandona toda esperanza de encontrarme. Púdrete.")
    input("Enter para continuar...")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def editar_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print(paciente)
        print("Menú de edición")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar previsión")
        print("0.- Salir")
        op=leer_numero("Ingrese una opción: ")
        if op == 1:
            nombre_nuevo = input("Ingrese nuevo nombre")
            paciente.nombre = nombre_nuevo
            print("Nombre actualizado.")
        elif op == 2:
            edad_nueva = leer_numero("Ingrese edad nueva")
            paciente.edad = edad_nueva
            print("Edad actualuzada.")
        elif op== 3:
            print("Tipos de previsión")
            print("1.- Fonasa")
            print("2.- Isapre")
            print("3.- Particular")
            print("4.- Otro")
            op=leer_numero("Seleccione una previsión: ")
            if op == 1:
                paciente.prevision = "Fonasa"
                print("Prevision actualizada")
            elif op == 2:
                paciente.prevision = "Isapre"
                print("Prevision actualizada")
            elif op == 3:
                paciente.prevision = "Particular"
                print("Prevision actualizada")
            elif op == 4:
                paciente.prevision = "Otro"
                print("Prevision actualizada")
            else:
                print("Opción Inválida")
    else:
        print("No se encontro al paciente blehhhh")
    input("Enter para continuar...")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def main():
    while True:
        opcion=menu()
        if opcion == 1:
            print("Agregar paciente")
            agregar_paciente()
        elif opcion == 2:
            print("Editar paciente")
            editar_paciente()
        elif opcion == 3:
            print("Eliminar paciente")
            eliminar_paciente()
        elif opcion == 4:
            print("Mostrar paciente")
            imprimir_paciente()
        elif opcion == 5:
            print("Mostrar todos los pacientes")
            imprimir_pacientes()
        elif opcion == 0:
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
if __name__=="__main__":
    main()
