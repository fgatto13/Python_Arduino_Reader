# This class represents an arduino device connected to the system.
class Device:
    def __init__(self, device_id, name, baud, port):
        self.device_id = device_id
        self.name = name
        self.baud = baud
        self.port = port
    
    def read_data(self):
        # Placeholder for reading data from the device
        pass
