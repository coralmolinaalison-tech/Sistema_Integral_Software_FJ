
from abc import abstractmethod
from entidades import EntidadSistema
from excepciones import DatosInvalidosError, ServicioNoDisponibleError


class Servicio(EntidadSistema):
    """Clase abstracta que representa los servicios de Software FJ."""

    def __init__(self, identificador, nombre, precio):
        super().__init__(identificador, nombre)

        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio <= 0:
            raise DatosInvalidosError("El precio del servicio debe ser mayor que cero.")

        self._precio = float(precio)
        self._disponible = True

    @property
    def precio(self):
        return self._precio

    @property
    def disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        if not isinstance(estado, bool):
            raise DatosInvalidosError("El estado de disponibilidad debe ser verdadero o falso.")
        self._disponible = estado

    def validar_disponibilidad(self):
        if not self._disponible:
            raise ServicioNoDisponibleError("El servicio no se encuentra disponible.")

    @abstractmethod
    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    def mostrar_informacion(self):
        return self.describir_servicio()


class ReservaSala(Servicio):
    """Servicio de reserva de salas."""

    def __init__(self, identificador, nombre, precio, capacidad):
        super().__init__(identificador, nombre, precio)

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad de la sala debe ser un entero mayor que cero.")

        self.__capacidad = capacidad

    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        self.validar_disponibilidad()

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")

        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        subtotal = self.precio * duracion
        total = subtotal - (subtotal * descuento / 100)
        return total + (total * impuesto / 100)

    def describir_servicio(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Identificador: {self.identificador}\n"
            f"Precio por hora: ${self.precio:,.0f}\n"
            f"Capacidad: {self.__capacidad} personas"
        )


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnológicos."""

    def __init__(self, identificador, nombre, precio, tipo_equipo):
        super().__init__(identificador, nombre, precio)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise DatosInvalidosError("Debe especificar el tipo de equipo.")

        self.__tipo_equipo = tipo_equipo.strip()

    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        self.validar_disponibilidad()

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")

        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        subtotal = self.precio * duracion
        total = subtotal - (subtotal * descuento / 100)
        return total + (total * impuesto / 100)

    def describir_servicio(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Identificador: {self.identificador}\n"
            f"Precio por día: ${self.precio:,.0f}\n"
            f"Tipo de equipo: {self.__tipo_equipo}"
        )


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoría especializada."""

    def __init__(self, identificador, nombre, precio, especialidad):
        super().__init__(identificador, nombre, precio)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("Debe especificar la especialidad de la asesoría.")

        self.__especialidad = especialidad.strip()

    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        self.validar_disponibilidad()

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")

        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        subtotal = self.precio * duracion
        total = subtotal - (subtotal * descuento / 100)
        return total + (total * impuesto / 100)

    def describir_servicio(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Identificador: {self.identificador}\n"
            f"Precio por hora: ${self.precio:,.0f}\n"
            f"Especialidad: {self.__especialidad}"
        )
