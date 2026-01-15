# This class represents an arduino device connected to the system.
import serial
class Device:
    def __init__(self, device_id, name, baud, port):
        self.device_id = device_id
        self.name = name
        self.baud = baud
        self.port = port
    
    def read_data(self, time) -> list | None:
        try:
            with serial.Serial(self.port, self.baud, timeout=1) as ser:
                line = []
                for _ in range(time):
                    line.append(ser.readline().decode('utf-8').rstrip())    
                return line
        except serial.SerialException as e:
            print(f"Error reading from device {self.device_id} on port {self.port}: {e}")
            return None
    