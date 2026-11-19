
from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


class Reserva:
    """Representa una reserva de un cliente para un servicio."""

    def __init__(self, identificador, cliente, servicio, duracion):
        if identificador is None or not str(identificador).strip():
            raise ReservaInvalidaError("El identificador de la reserva no puede estar vacío.")

        if cliente is None or not hasattr(cliente, "mostrar_informacion"):
            raise ReservaInvalidaError("La reserva debe tener un cliente válido.")

        if servicio is None or not hasattr(servicio, "calcular_costo"):
            raise ReservaInvalidaError("La reserva debe tener un servicio válido.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración de la reserva debe ser mayor que cero.")

        self.__identificador = str(identificador).strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__servicio.validar_disponibilidad()
        self.__estado = "Confirmada"
        print("La reserva ha sido confirmada correctamente.")

    def cancelar(self):
        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        if self.__estado == "Procesada":
            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva que ya fue procesada."
            )

        self.__estado = "Cancelada"
        print("La reserva ha sido cancelada correctamente.")

    def procesar(self, impuesto=0, descuento=0):
        if self.__estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "Solo se pueden procesar reservas confirmadas."
            )

        try:
            costo = self.__servicio.calcular_costo(
                duracion=self.__duracion,
                impuesto=impuesto,
                descuento=descuento
            )
        except DatosInvalidosError as error:
            raise ReservaInvalidaError(
                "No fue posible calcular el costo de la reserva."
            ) from error

        self.__estado = "Procesada"
        return costo

    def mostrar_informacion(self):
        return (
            f"Reserva: {self.__identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}"
        )
