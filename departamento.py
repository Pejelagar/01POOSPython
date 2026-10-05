class Departamento:

    def __init__(self, id_dep:int, nombre:str, piso:int):
        self.id_dep = id_dep
        self.nombre = nombre
        self.piso = piso

    @property
    def id_dep(self)-> int:
        return self._id_dep

    @id_dep.setter
    def id_dep(self,id_dep:int)-> None:
        if not isinstance(id_dep,int) or not id_dep.strip():
            raise ValueError("El ID no puede estar vacío!")
        self._id_dep = id_dep.strip().upper()

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)-> None:
        if not isinstance(nombre,str) or not len(nombre.strip()) > 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres!")
        self._nombre = nombre.strip().upper()

    @property
    def piso(self)->int:
        return self._piso

    @piso.setter
    def piso(self,piso:int)-> None:
        if not isinstance(piso,int):
            raise TypeError("El piso debe ser un número entero!")
        self._edad=piso

    def __str__(self)-> str:
        return f"Informacion del departamento:\nID: {self.id_dep}\nNombre: {self.nombre}\nPiso: {self.piso}"

    def __repr__(self)-> str:
        return f"Departamento(id_dep={self.id_dep}, nombre='{self.nombre}', piso='{self.piso}')"
