# This class represents an arduino device connected to the system.
import serial
import time
class Device:
    def __init__(self, device_id, name, baud, port):
        self.device_id = device_id
        self.name = name
        self.baud = baud
        self.port = port
    
    def read_data(self) -> list | None:
        try:
            with serial.Serial(self.port, self.baud, timeout=1) as ser:
                line = []
                while True:
                    i = input("on/off: ").strip()
                    if i == "done":
                        print("Exiting read loop.")
                        return line
                    ser.write(i.encode())
                    time.sleep(0.5)
                    print(ser.readline().decode('ascii'))
                    line.append(ser.readline().decode('ascii'))    
                    print(f"Device {self.device_id} on port {self.port} read data: {line[-1]}")
        except serial.SerialException as e:
            print(f"Error reading from device {self.device_id} on port {self.port}: {e}")
            return None
    