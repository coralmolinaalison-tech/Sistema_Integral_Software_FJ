
# Clase abstracta para las entidades del sistema Software FJ

from abc import ABC, abstractmethod
from excepción import DatosInvalidosError


class EntidadSistema(ABC):
    """Clase abstracta que representa las entidades generales del sistema."""

    def __init__(self, identificador, nombre):
        # Validar el identificador
        if identificador is None or str(identificador).strip() == "":
            raise DatosInvalidosError(
                "El identificador de la entidad no puede estar vacío."
            )

        # Validar el nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre de la entidad debe ser un texto válido."
            )

        # Atributos encapsulados
        self.__identificador = str(identificador).strip()
        self.__nombre = nombre.strip()

    @property
    def identificador(self):
        """Permite consultar el identificador de la entidad."""
        return self.__identificador

    @property
    def nombre(self):
        """Permite consultar el nombre de la entidad."""
        return self.__nombre

    @abstractmethod
    def mostrar_informacion(self):
        """Método abstracto para mostrar la información de cada entidad."""
        pass
