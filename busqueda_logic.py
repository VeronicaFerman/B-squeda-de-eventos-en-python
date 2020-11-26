from busqueda_obj import EventoObj, CategoriaObj, TipoObj
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

    def getEventosById(self, id):
        database = self.database
        sql = f"SELECT * FROM eventbrite.eventos where idEventos = {id};"
        rows = database.executeQueryOneRow(sql)
        return rows

    def getEventosByCategoria(self, categoria):
        database = self.database
        data = database.executeQueryRows(
            f"SELECT eventos.* FROM eventos inner join categorias_eventos "
            + f"on eventos.categoria = categorias_eventos.idcategorias_eventos "
            + f"where categorias_eventos.nombreCat = '{categoria}'"
        )
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList
    
    def getEventosByTipo(self, tipo):
        database = self.database
        data = database.executeQueryRows(
            f"SELECT eventos.* FROM eventos inner join tipo_eventos "
            + f"on eventos.tipo = tipo_eventos.idtipo_eventos "
            + f"where tipo_eventos.nombreTipo = '{tipo}'"
        )
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList
    
    def getEventosByDate(self, date):
        database = self.database
        data = database.executeQueryRows(f"SELECT * from eventos where eventos.fecha = '{date}'")
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList

    def getEventosByCity(self, city):
        database = self.database
        data = database.executeQueryRows(f"SELECT * from eventos where eventos.ciudad = '{city}'")
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList
    
    def getEventosByCountry(self, country):
        database = self.database
        data = database.executeQueryRows(f"SELECT * from eventos where eventos.pais = '{country}'")
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList
    
    def getEventosByModality(self, modality):
        database = self.database
        data = database.executeQueryRows(f"SELECT * from eventos where eventos.modalidad = '{modality}'")
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList

    def getCategoriasByEvent(self, id):
        database = self.database
        sql = (
            f"SELECT eventos.categoria, categorias_eventos.nombreCat FROM eventos inner join categorias_eventos "
            + f"on eventos.categoria = categorias_eventos.idcategorias_eventos where eventos.idEventos = {id}"
        )
        rows = database.executeQueryOneRow(sql)
        return rows
    
    def getAllCategorias(self):
        database = self.database
        data = database.executeQueryRows("SELECT * FROM categorias_eventos;")
        categoriaList = []
        for element in data:
            newCat = self.createCategoriaObj(element)
            categoriaList.append(newCat)
        return categoriaList

    def getAllTipos(self):
        database = self.database
        data = database.executeQueryRows("SELECT * FROM tipo_eventos;")
        tipoList = []
        for element in data:
            newTipo = self.createTipoObj(element)
            tipoList.append(newTipo)
        return tipoList

    def getTiposByEvent(self, id):
        database = self.database
        sql = (
            f"SELECT eventos.tipo, tipo_eventos.nombreTipo FROM eventos inner join tipo_eventos "
            + f"on eventos.categoria = tipo_eventos.idtipo_eventos where eventos.idEventos = {id}"
        )
        rows = database.executeQueryOneRow(sql)
        return rows

    def getUserName(self, id):
        database = self.database
        sql = (
            f"SELECT eventos.idUsuarios, usuarios.nombre FROM eventos inner join usuarios "
            + f"on eventos.idUsuarios = usuarios.idUsuarios where eventos.idEventos = {id}"
        )
        rows = database.executeQueryOneRow(sql)
        return rows

    def createEventoObj(self, idEventos, idUsuarios, nombre, categoría, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo, modalidad):
        eventoObj = EventoObj(idEventos, idUsuarios, nombre, categoría, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo, modalidad)
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
            eventoDict["modalidad"]
        )
        return eventoObj

    def createCategoriaObj(self, idcategorias_eventos, nombreCat):
        eventoObj = CategoriaObj(idcategorias_eventos, nombreCat)
        return CategoriaObj

    def createCategoriaObj(self, categoriaDict):
        categoriaObj = CategoriaObj(
            categoriaDict["idcategorias_eventos"],
            categoriaDict["nombreCat"]
        )
        return categoriaObj

    def createTipoObj(self, idtipo_eventos, nombreTipo):
        eventoObj = TipoObj(idtipo_eventos, nombreTipo)
        return TipoObj

    def createTipoObj(self, tipoDict):
        tipoObj = TipoObj(
            tipoDict["idtipo_eventos"],
            tipoDict["nombreTipo"]
        )
        return tipoObj