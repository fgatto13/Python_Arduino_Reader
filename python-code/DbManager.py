import os
import mysql.connector
import dotenv
import pandas as pd

class DbManager:
    def __init__(self):
        REQUIRED_VARS = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"]

        missing = [v for v in REQUIRED_VARS if not os.getenv(v)]
        if missing:
            raise RuntimeError(
                f"Missing environment variables: {', '.join(missing)}. "
                "Did you copy .env.template to .env?"
            )

        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.conn.cursor(dictionary=True)
    def fetch_all(self, params=None):
        self.cursor.execute("SELECT * FROM device", params or ())
        return self.cursor.fetchall()
    def fetch_one(self, params=None):
        self.cursor.execute("SELECT * FROM device WHERE device_id = %s", params or ())
        return self.cursor.fetchone()
    def insert_device(self, name, baud):
        try:
            self.cursor.execute(
                "INSERT INTO device (device_name, baud) VALUES (%s, %s)",
                (name, baud)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error inserting device: {err}")
            self.conn.rollback()
            return None
    def delete_device(self, device_id):
        try:
            self.cursor.execute(
                "UPDATE device SET is_deleted = TRUE WHERE device_id = %s",
                (device_id,)
            )
            self.conn.commit()
            return self.cursor.rowcount
        except mysql.connector.Error as err:
            print(f"Error deleting device: {err}")
            self.conn.rollback()
            return None
    def permanent_delete_device(self, device_id):
        try:
            self.cursor.execute(
                "DELETE FROM device WHERE device_id = %s",
                (device_id,)
            )
            self.conn.commit()
            return self.cursor.rowcount
        except mysql.connector.Error as err:
            print(f"Error permanently deleting device: {err}")
            self.conn.rollback()
            return None
    def close(self):
        self.cursor.close()
        self.conn.close()
    def print_env_variables(self):
        print("DB_HOST:", os.getenv("DB_HOST"))
        print("DB_USER:", os.getenv("DB_USER"))
        print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
        print("DB_NAME:", os.getenv("DB_NAME"))

if __name__ == "__main__":
    dotenv.load_dotenv()
    db_manager = DbManager()
    db_manager.print_env_variables()
    db_manager.insert_device("Test Device 1", 9600)
    db_manager.insert_device("Test Device 2", 9600)
    db_manager.insert_device("Test Device 3", 9600)
    db_manager.insert_device("Test Device 4", 9600)
    db_manager.insert_device("Test Device 5", 9600)
    df = pd.DataFrame(db_manager.fetch_all())
    print(df)
    db_manager.permanent_delete_device(1)
    db_manager.permanent_delete_device(2)
    db_manager.permanent_delete_device(3)
    db_manager.permanent_delete_device(4)
    db_manager.permanent_delete_device(5)
    db_manager.permanent_delete_device(6)
    db_manager.close()