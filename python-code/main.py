from DbManager import DbManager
from dotenv import load_dotenv
import serial
import serial.tools.list_ports

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
    # Search for available serial ports
    # The following block of code was adapted from stackoverflow.com/questions/53214304/python-pyserial-auto-detect-com-ports
    ports = find_serial_ports()
    if ports:
        print('Available serial ports:')
        for port in ports :
            print('Find port '+ port.device)
    else:
        print('No ports found')

if __name__ == "__main__":
    main()