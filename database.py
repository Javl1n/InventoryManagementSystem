from tkinter import messagebox

from mysql import connector
import sys

class Database():
    def __init__(self):
        self.connection = connector.connect(
            host = "localhost",
            port = "3307",
            user = "root",
            password = "frank050204",
            database = "inventory_management_system"
        )
        self.cursor = self.connection.cursor()

    def query(self, query, values):
        self.cursor.execute(query, values)

    def getOne(self):
        return self.cursor.fetchone()

    def get(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
