from busqueda_logic import EventoLogic
from prettytable import PrettyTable

#Búsqueda general
logic = EventoLogic()

def detallesEventos():

    id = int(input("¿Cuál es el id del evento que desea ver más detalles?  "))

    eventoElegido = logic.getEventosById(id)
    catEventoElegido = logic.getCategoriasByEvent(id)
    tipoEventoElegido = logic.getTiposByEvent(id)
    userEventoElegido = logic.getUserName(id)

    print("----------------------------------------------------------------------------------------------")
    print("La información adicional de este evento es: ")
    print("\n")
    print("El creador del evento es: "+ str(userEventoElegido['nombre']))
    print("La categoría del evento es: "+ catEventoElegido['nombreCat'])
    print("Descripción: "+ eventoElegido['descripcion'])
    print("El valor de la entrada es: ($) "+ str(eventoElegido ['valorEntrada']))
    print("La máxima capacidad de asistentes es: "+ str(eventoElegido['capacidad']) + " (personas)")
    print("La cantidad de entradas disponibles es: "+ str(eventoElegido['disponibilidad']))
    print("La dirección detallada de la ubicación del evento es: "+ eventoElegido['direccion'])
    print("El tipo del evento es: "+ tipoEventoElegido['nombreTipo'])

def tablaEventos(eventoList):
    if eventoList == []:
        print("**No hay eventos existentes**\n")
    else:
        table = PrettyTable()
        table.field_names = ["IdEvento", "nombre", "fecha", "hora", "valorEntrada", "disponibilidad", "ciudad", "pais", "modalidad"]
        for eventoObj in eventoList:
            table.add_row([eventoObj.idEventos, 
                            eventoObj.nombre,
                            eventoObj.fecha, 
                            eventoObj.hora, 
                            eventoObj.valorEntrada, 
                            eventoObj.disponibilidad, 
                            eventoObj.ciudad, 
                            eventoObj.pais,
                            eventoObj.modalidad])
        print(table)
        detallesEventos()

while True:
    print("Elija de qué manera desea realizar la búsqueda de eventos\n")
    print("(0) Salir de la búsqueda")
    print("(1) General")
    print("(2) Por categoría")
    print("(3) Por fecha")
    print("(4) Por ciudad")
    print("(5) Por país")
    print("(6) Por tipo")
    print("(7) Por modalidad\n")
    option = int(input("Opción: "))

    if option == 0:
        break
    elif option == 1:
        eventoList = logic.getAllEventosFromSearch()
        tablaEventos(eventoList)

    elif option == 2:
        categoriaList = logic.getAllCategorias()
        table = PrettyTable()
        table.field_names = ["Categorías"]
        for categoriaObj in categoriaList:
            table.add_row([categoriaObj.nombreCat])
        print(table)

        categoria = input("Escriba el nombre de la categoria en la que quiere buscar eventos: ")

        eventoList = logic.getEventosByCategoria(categoria)

        tablaEventos(eventoList)

    elif option == 3:
        date = str(input("Escriba la fecha (YYYY-MM-DD) en la que desea buscar eventos: "))
        eventoList = logic.getEventosByDate(date)
        tablaEventos(eventoList)

    elif option == 4:
        city = input("Escriba la ciudad en la que quiere buscar los eventos: ")
        eventoList = logic.getEventosByCity(city)
        tablaEventos(eventoList)

    elif option == 5:
        country = input("Escriba el país en el que quiere buscar los eventos: ")
        eventoList = logic.getEventosByCountry(country)
        tablaEventos(eventoList)

    elif option == 6:
        tipoList = logic.getAllTipos()
        table = PrettyTable()
        table.field_names = ["Tipos"]
        for tipoObj in tipoList:
            table.add_row([tipoObj.nombreTipo])
        print(table)

        tipo = input("Escriba el nombre del tipo de eventos que quiere buscar: ")

        eventoList = logic.getEventosByTipo(tipo)

        tablaEventos(eventoList)

    elif option == 7:
        modality = input("Escriba la modalidad  (virtual o presencial) de los eventos que quiere buscar: ")
        eventoList = logic.getEventosByModality(modality)
        tablaEventos(eventoList)
    else:
        print("Opción incorrecta")