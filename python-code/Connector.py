import mysql.connector
import os

class Connector():
    def __init__(self):
        self.envdata = os.getenv("../.env")
        self.mydb = mysql.connector.connect(
            host="",
            user="",
            pwd=""
        )
        self.cursor = self.mydb.cursor()