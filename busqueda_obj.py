class EventoObj:
    def __init__(self, idEventos, idUsuarios, nombre, categoría, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo, modalidad):
        self.idEventos = idEventos
        self.idUsuarios = idUsuarios
        self.nombre = nombre
        self.categoría = categoría
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.valorEntrada = valorEntrada
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad
        self.ciudad = ciudad
        self.pais = pais
        self.direccion = direccion
        self.tipo = tipo
        self.modalidad = modalidad
class CategoriaObj:
    def __init__(self, idcategorias_eventos, nombreCat):
        self.idcategorias_eventos = idcategorias_eventos
        self.nombreCat = nombreCat

class TipoObj:
    def __init__(self, idtipo_eventos, nombreTipo):
        self.idtipo_eventos = idtipo_eventos
        self.nombreTipo = nombreTipo

