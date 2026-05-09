import serial
import time


class RobotHandController:

    def __init__(self):

        self.serial_connection = None

        possible_ports = [
            "COM3",
            "COM4",
            "COM5",
            "COM6"
        ]

        for port in possible_ports:

            try:

                print(f"Intentando conectar en {port}...")

                self.serial_connection = serial.Serial(
                    port,
                    9600,
                    timeout=1
                )

                time.sleep(2)

                print(f"Conectado correctamente en {port}")

                break

            except Exception:

                continue

        if self.serial_connection is None:

            print(
                "\nERROR:"
                "\nNo se pudo entablar conexión con la mano robótica."
                "\nPor favor revise el puerto COM "
                "y vuelva a intentarlo.\n"
            )

    def send_command(self, command):

        if self.serial_connection is None:

            print(
                "No existe conexión activa con Arduino."
            )

            return

        try:

            self.serial_connection.write(
                str(command).encode()
            )

        except Exception as e:

            print(
                f"Error enviando comando: {e}"
            )

    def close(self):

        if self.serial_connection:

            self.serial_connection.close()