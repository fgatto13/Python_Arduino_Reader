from Connector import Connector
from Reader import Reader

def main():
    dbconnector = Connector()
    ino_data_reader = Reader("COM5", 9600)
    
if __name__ == "__main__":
    main()