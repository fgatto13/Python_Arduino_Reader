from abc import ABC, abstractmethod

# Abstract base class for devices
class AbsDevice(ABC):
    def __init__(self, device_id, name, baud, port):
        self.device_id = device_id
        self.name = name
        self.baud = baud
        self.port = port
        
    @abstractmethod
    def read_data(self):
        pass