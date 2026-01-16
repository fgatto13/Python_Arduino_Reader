from AbstractDevice import AbsDevice
import serial
import time

# this class represents an arduino device that reads water level data
class WaterDevice(AbsDevice):
    def read_data(self) -> list | None:
        try:
            with serial.Serial(self.port, self.baud, timeout=1) as ser:
                line = []
                while True:
                    line.append(ser.readline().decode('ascii').strip())
                    print(f"Device {self.device_id} on port {self.port} read water level: {line[-1]}")
                    time.sleep(1)
                    continue_reading = input("Continue reading? (y/n): ").strip().lower()
                    if continue_reading != 'y':
                        print("Exiting water level read loop.")
                        return line
        except serial.SerialException as e:
            print(f"Error reading from device {self.device_id} on port {self.port}: {e}")