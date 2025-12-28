from DbManager import DbManager
from Device import Device

def main():
    # Initialize database manager
    db_manager = DbManager()
    
    # Create a device instance
    device = Device(name="Arduino Uno", baud=9600, port="COM5")
    
    device.read_data()
    
if __name__ == "__main__":
    main()