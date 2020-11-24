from busqueda_obj import EventoObj
from dx_logic import Logic

class EventoLogic(Logic):
    def __init__(self):
        super().__init__()

    def getAllEventosFromSearch(self):
        database = self.database
        data = database.executeQueryRows("select * from eventos;")
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList

    # polimorfismo
    def createEventoObj(self, idEventos, idUsuarios, nombre, categoría, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo):
        eventoObj = EventoObj(idEventos, idUsuarios, nombre, categoría, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo)
        return EventoObj

    def createEventoObj(self, eventoDict):
        eventoObj = EventoObj(
            eventoDict["idEventos"],
            eventoDict["idUsuarios"],
            eventoDict["nombre"],
            eventoDict["categoria"],
            eventoDict["fecha"],
            eventoDict["hora"],
            eventoDict["descripcion"],
            eventoDict["valorEntrada"],
            eventoDict["capacidad"],
            eventoDict["disponibilidad"],
            eventoDict["ciudad"],
            eventoDict["pais"],
            eventoDict["direccion"],
            eventoDict["tipo"],
        )
        return eventoObj
