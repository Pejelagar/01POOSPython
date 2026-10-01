class Departamento:

    def __init__(self, id_dep:int, nombre:str, piso:int):
        self.id_dep = id_dep
        self.nombre = nombre
        self.piso = piso

    @property
    def id_dep(self)-> int:
        return self._id_dep

    @id_dep.setter
    def rut(self,id_dep:int)-> None:
        self._id_dep = id_dep

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)-> None:
        self._nombre = nombre

    @property
    def piso(self)->int:
        return self._piso

    @piso.setter
    def piso(self,piso:int)-> None:
        self._piso = piso

    def __str__(self)-> str:
        return f"Informacion del departamento:\nID: {self.id_dep}\nNombre: {self.nombre}\nPiso: {self.piso}"

    def __repr__(self)-> str:
        return f"Departamento(id_dep={self.id_dep}, nombre='{self.nombre}', piso='{self.piso}')"
