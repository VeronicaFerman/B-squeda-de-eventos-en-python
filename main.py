from busqueda_logic import EventoLogic
from prettytable import PrettyTable

#Búsqueda general
logic = EventoLogic()
eventoList = logic.getAllEventosFromSearch()
table = PrettyTable()
table.field_names = ["IdEvento", "nombre", "categoría", "fecha", "hora", "valorEntrada", "disponibilidad", "ciudad", "pais", "tipo"]
for eventoObj in eventoList:
    table.add_row([eventoObj.idEventos, eventoObj.nombre, eventoObj.categoría, eventoObj.fecha, eventoObj.hora, eventoObj.valorEntrada, eventoObj.disponibilidad, eventoObj.ciudad, eventoObj.pais, eventoObj.tipo])
print(table)

#Evento seleccionado después de la búsqueda general
logic = EventoLogic()
id = int(input("¿Cuál es el id del evento que desea ver a detalle?  "))

eventoElegido = logic.getEventosById(id)
print("----------------------------------------------------------------------------------------------")
print("La información completa de este evento es: ")
print("\n")
print("El id del evento es: "+ str(eventoElegido['idEventos']))
print("El creador del evento es: "+ str(eventoElegido['idUsuarios']))
print("El nombre del evento es: "+ eventoElegido['nombre'])
print("La categoría del evento es: "+ str(eventoElegido['categoria']))
print("El fecha en la que se realizará el evento es: "+ str(eventoElegido['fecha']))
print("La hora en que se realizará el evento es: "+ str(eventoElegido['hora']))
print("Descrición: "+ eventoElegido['descripcion'])
print("El valor de la entrada es: ($) "+ str(eventoElegido ['valorEntrada']))
print("La máxima capacidad de asistentes es: "+ str(eventoElegido['capacidad']) + " (personas)")
print("La cantidad de entradas disponibles es: "+ str(eventoElegido['disponibilidad']))
print("La ciudad en que se llevará a cabo el evento es: "+eventoElegido['ciudad'])
print("El país en donde se llevara acabo el evento es: "+ eventoElegido['pais'])
print("La dirección detallada de la ubicación del evento es: "+ eventoElegido['direccion'])
print("El tipo del evento es: "+ str(eventoElegido['tipo']))






