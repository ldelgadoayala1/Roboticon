import serial
import time

class ArduinoController:
    def __init__(self, port='COM3', baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
        time.sleep(2)  # esperar conexión

    def send_move(self, move):
        """
        move: int (1,2,3...)
        """
        self.ser.write(str(move).encode())

    def close(self):
        self.ser.close()