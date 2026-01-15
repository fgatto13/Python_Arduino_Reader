from DbManager import DbManager
from Device import Device
from dotenv import load_dotenv
import serial
import serial.tools.list_ports

# part of the code adapted from stackoverflow.com/questions/53214304/python-pyserial-auto-detect-com-ports
def find_serial_ports():
    ports = serial.tools.list_ports.comports(include_links=False)
    if not ports:
        return []
    return ports

def main():
    load_dotenv()
    # Initialize database manager
    db_manager = DbManager()
    db_manager.close()
    
    ports = find_serial_ports()
    if ports:
        print('Available serial ports:')
        for port in ports :
            print('Find port '+ port.device)
        # now we create a device object
        device = Device(device_id=1, name='INO_TEST', baud=9600, port=ports[0].device)
        data = device.read_data(time=5)
        if data:
            print(f'Read data: {data}')
        else:
            print('No data read from device')
    else:
        print('No ports found')

if __name__ == "__main__":
    main()