
# Archivo principal del sistema Software FJ

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from logs import RegistroLogs


# Listas para almacenar los datos durante la ejecución
clientes = []
servicios = []
reservas = []


def ejecutar_operacion(descripcion, operacion):
    """Ejecuta una operación y controla los posibles errores."""

    print(f"\n--- {descripcion} ---")

    try:
        operacion()

    except Exception as error:
        print(f"Error controlado: {error}")
        RegistroLogs.registrar_error(
            f"{descripcion}: {error}"
        )

    else:
        print("Operación realizada correctamente.")
        RegistroLogs.registrar_evento(descripcion)

    finally:
        print("Finalizó la operación.")


def registrar_cliente():
    cliente = Cliente(
        "1001",
        "Ana Perez",
        "ana@gmail.com",
        "3001234567"
    )
    clientes.append(cliente)
    print(cliente.mostrar_informacion())


def registrar_cliente_invalido():
    cliente = Cliente(
        "1002",
        "Carlos Lopez",
        "correo_invalido",
        "3001234568"
    )
    clientes.append(cliente)


def crear_sala():
    sala = ReservaSala(
        "S01",
        "Sala de reuniones",
        50000,
        10
    )
    servicios.append(sala)
    print(sala.describir_servicio())


def crear_sala_invalida():
    sala = ReservaSala(
        "S02",
        "Sala pequeña",
        40000,
        -5
    )
    servicios.append(sala)


def crear_equipo():
    equipo = AlquilerEquipo(
        "E01",
        "Alquiler tecnológico",
        30000,
        "Proyector"
    )
    servicios.append(equipo)
    print(equipo.describir_servicio())


def crear_asesoria():
    asesoria = AsesoriaEspecializada(
        "A01",
        "Asesoría informática",
        60000,
        "Programación"
    )
    servicios.append(asesoria)
    print(asesoria.describir_servicio())


def crear_reserva():
    reserva = Reserva(
        "R01",
        clientes[0],
        servicios[0],
        2
    )
    reservas.append(reserva)
    print(reserva.mostrar_informacion())


def confirmar_reserva():
    reservas[0].confirmar()


def procesar_reserva():
    costo = reservas[0].procesar(impuesto=19, descuento=0)
    print(f"Costo total de la reserva: ${costo:,.0f}")


def cancelar_reserva():
    reservas[0].cancelar()


def crear_reserva_invalida():
    reserva = Reserva(
        "R02",
        "Cliente incorrecto",
        servicios[0],
        2
    )
    reservas.append(reserva)


def procesar_reserva_cancelada():
    reservas[0].procesar()


def main():
    """Ejecuta las operaciones de prueba del sistema."""

    print("======================================")
    print(" SISTEMA INTEGRAL SOFTWARE FJ")
    print("======================================")

    RegistroLogs.registrar_evento(
        "Inicio del sistema Software FJ."
    )

    # Operaciones con clientes
    ejecutar_operacion("1. Registrar cliente válido", registrar_cliente)

    ejecutar_operacion(
        "2. Registrar cliente con correo inválido",
        registrar_cliente_invalido
    )

    # Operaciones con servicios
    ejecutar_operacion("3. Crear reserva de sala", crear_sala)

    ejecutar_operacion(
        "4. Crear sala con capacidad inválida",
        crear_sala_invalida
    )

    ejecutar_operacion("5. Crear alquiler de equipo", crear_equipo)

    ejecutar_operacion("6. Crear asesoría especializada", crear_asesoria)

    # Operaciones con reservas
    ejecutar_operacion("7. Crear reserva válida", crear_reserva)

    ejecutar_operacion("8. Confirmar reserva", confirmar_reserva)

    ejecutar_operacion("9. Procesar reserva", procesar_reserva)

    ejecutar_operacion("10. Cancelar reserva", cancelar_reserva)

    ejecutar_operacion(
        "11. Intentar crear reserva con cliente inválido",
        crear_reserva_invalida
    )

    ejecutar_operacion(
        "12. Intentar procesar una reserva cancelada",
        procesar_reserva_cancelada
    )

    print("\n======================================")
    print(" FIN DE LAS PRUEBAS DEL SISTEMA")
    print("======================================")

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas registradas: {len(reservas)}")

    RegistroLogs.registrar_evento(
        "Finalización de las pruebas del sistema."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error general del sistema: {error}")
        RegistroLogs.registrar_error(
            f"Error general: {error}"
        )
    finally:
        print("\nEjecución del programa finalizada.")
