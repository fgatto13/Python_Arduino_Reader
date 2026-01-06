from DbManager import DbManager
from Device import Device
from dotenv import load_dotenv

def main():
    load_dotenv()
    # Initialize database manager
    db_manager = DbManager()
    db_manager.print_env_variables()
    db_manager.close()

if __name__ == "__main__":
    main()