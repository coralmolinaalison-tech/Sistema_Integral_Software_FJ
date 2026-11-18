
# Excepciones personalizadas del sistema Software FJ

class ErrorSistema(Exception):
    """Excepción base para los errores del sistema."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se genera cuando los datos ingresados no son válidos."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se genera cuando un cliente no existe en el sistema."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva presenta información incorrecta."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando se intenta realizar una operación no permitida."""
    pass
