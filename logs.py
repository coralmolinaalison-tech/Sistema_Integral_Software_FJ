
from datetime import datetime


class RegistroLogs:
    """Permite registrar los eventos y errores del sistema Software FJ."""

    ARCHIVO_LOG = "software_fj.log"

    @classmethod
    def registrar_evento(cls, mensaje):
        """Guarda un evento importante del sistema."""
        cls._registrar("EVENTO", mensaje)

    @classmethod
    def registrar_error(cls, mensaje):
        """Guarda un error ocurrido durante la ejecución."""
        cls._registrar("ERROR", mensaje)

    @classmethod
    def _registrar(cls, tipo, mensaje):
        """Escribe el registro en el archivo de logs."""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(cls.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
                archivo.write(f"[{fecha}] [{tipo}] {mensaje}\n")

        except OSError as error:
            print(f"No fue posible escribir en el archivo de logs: {error}")
