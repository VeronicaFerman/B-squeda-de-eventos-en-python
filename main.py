from busqueda_logic import EventoLogic


logic = EventoLogic()
eventoList = logic.getAllEventosFromSearch()
for eventoObj in eventoList:
    print(eventoObj.idEventos, eventoObj.idUsuarios, eventoObj.nombre, eventoObj.categoría, eventoObj.fecha, eventoObj.hora, eventoObj.descripcion, eventoObj.valorEntrada, eventoObj.capacidad, eventoObj.disponibilidad, eventoObj.ciudad, eventoObj.pais, eventoObj.direccion, eventoObj.tipo)


