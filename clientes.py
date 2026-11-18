
# Clase Cliente del sistema Software FJ

import re

from entidades import EntidadSistema
from excepción import DatosInvalidosError


class Cliente(EntidadSistema):
    """Representa un cliente registrado en el sistema."""

    def __init__(self, identificacion, nombre, correo, telefono):
        # Inicializar los atributos de la clase padre
        super().__init__(identificacion, nombre)

        # Validar el correo electrónico
        if not isinstance(correo, str) or not correo.strip():
            raise DatosInvalidosError(
                "El correo electrónico no puede estar vacío."
            )

        patron_correo = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.match(patron_correo, correo.strip()):
            raise DatosInvalidosError(
                "El correo electrónico ingresado no es válido."
            )

        # Validar el teléfono
        if not isinstance(telefono, str):
            raise DatosInvalidosError(
                "El teléfono debe ingresarse como texto."
            )

        telefono = telefono.strip()

        if not telefono.isdigit() or len(telefono) < 7 or len(telefono) > 15:
            raise DatosInvalidosError(
                "El número de teléfono debe contener entre 7 y 15 dígitos."
            )

        # Atributos privados para proteger los datos personales
        self.__correo = correo.strip()
        self.__telefono = telefono

    @property
    def correo(self):
        """Permite consultar el correo electrónico."""
        return self.__correo

    @property
    def telefono(self):
        """Permite consultar el número telefónico."""
        return self.__telefono

    def mostrar_informacion(self):
        """Muestra la información del cliente."""
        return (
            f"Identificación: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )

    def actualizar_correo(self, nuevo_correo):
        """Actualiza el correo después de validar su formato."""

        if not isinstance(nuevo_correo, str) or not nuevo_correo.strip():
            raise DatosInvalidosError(
                "El nuevo correo no puede estar vacío."
            )

        patron_correo = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.match(patron_correo, nuevo_correo.strip()):
            raise DatosInvalidosError(
                "El nuevo correo electrónico no es válido."
            )

        self.__correo = nuevo_correo.strip()
