from busqueda_logic import EventoLogic
from prettytable import PrettyTable

#Búsqueda general
logic = EventoLogic()

while True:
    print("Elija de qué manera desea realizar la búsqueda de eventos\n")
    print("(0) Salir de la búsqueda")
    print("(1) General")
    print("(2) Por categoría")
    print("(3) Por fecha")
    print("(4) Por ciudad")
    print("(5) Por país")
    print("(6) Por modalidad\n")
    option = int(input("Opción: "))

    if option == 0:
        break
    elif option == 1:
        eventoList = logic.getAllEventosFromSearch()
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

        #Evento seleccionado después de la búsqueda general
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

    elif option == 2:
        categoriaList = logic.getAllCategorias()
        table = PrettyTable()
        table.field_names = ["Id", "nombre"]
        for categoriaObj in categoriaList:
            table.add_row([categoriaObj.idcategorias_eventos, 
                            categoriaObj.nombreCat])
        print(table)

        categoria = input("Escriba el nombre de la categoria en la que quiere buscar eventos: ")

        eventoList = logic.getEventosByCategoria(categoria)

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