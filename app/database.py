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

    def query(self, query, values = None):
        if values is not None:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query, )

    def getOne(self):
        return self.cursor.fetchone()

    def get(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
