from DbManager import DbManager
from Device import Device
from dotenv import load_dotenv
from simple_term_menu import TerminalMenu # https://github.com/IngoMeyer441/simple-term-menu
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
        # Create a terminal menu for user to select a port
        options = [port.device for port in ports]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        assert isinstance(menu_entry_index, int)
        print(f"You have selected {options[menu_entry_index]}")
        # after the port gets selected, we create a device instance with the selected port
        device = Device(device_id=1, name='INO_TEST', baud=9600, port=options[menu_entry_index])
        print(f'Reading data from device on port {device.port}...')
        data = device.read_data()
        if not data:
            print('No data read from device.')
    else:
        print('No ports found')

if __name__ == "__main__":
    main()