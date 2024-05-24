from customtkinter import *

from components import navigation, table
from app.database import Database
from app.localstorage import LocalStorage


class MovementsInShow(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.controller = controller

        storage = LocalStorage()

        if 'moveIn' not in storage.shelf.keys():
            return

        item = storage.shelf['moveIn']

        storage.save()
        storage.close()
        database = Database()
        database.query('''
            SELECT o.id, i.name, s.name, o.date, o.quantity, o.expiration_date, u.username FROM item_in o
            INNER JOIN items i ON o.item_id = i.id
            INNER JOIN users u ON o.user_id = u.id
            INNER JOIN suppliers s ON o.supplier_id = s.id
            WHERE o.id = %s
        ''', (item, ))

        item = database.getOne()

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        back = CTkButton(self, text="Go Back", command=lambda: self.controller.navigate('/movements')).place(y=35, x=1190, anchor="center")

        level = 180

        CTkLabel(self, text="Move In Details", font=("default", 40, "bold")).place(y=15 + level, relx=0.41)

        CTkLabel(self, text="Item: " + item[1], font=('default', 30)).place(y=60 + level, relx=0.41)
        CTkLabel(self, text="Supplier: " + str(item[2]), font=('default', 24)).place(y=100 + level, relx=0.41)
        CTkLabel(self, text="Date of Movement: " + str(item[3]), font=('default', 24)).place(y=130 + level, relx=0.41)
        CTkLabel(self, text="Expiration Date: " + str(item[5]), font=('default', 24)).place(y=160 + level, relx=0.41)
        CTkLabel(self, text="Quantity Moved: " + str(item[4]), font=('default', 24)).place(y=190 + level, relx=0.41)
        CTkLabel(self, text="Input By: " + str(item[6]), font=('default', 24)).place(y=220 + level, relx=0.41)


