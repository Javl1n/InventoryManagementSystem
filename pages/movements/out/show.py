from customtkinter import *

from components import navigation, table
from app.database import Database
from app.localstorage import LocalStorage


class MovementsOutShow(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.controller = controller

        storage = LocalStorage()

        if 'moveOut' not in storage.shelf.keys():
            return

        item = storage.shelf['moveOut']

        storage.save()
        storage.close()
        database = Database()
        database.query('''
            SELECT o.id, i.name, o.date, o.quantity, u.username FROM item_out o
            INNER JOIN items i ON o.item_id = i.id
            INNER JOIN users u ON o.user_id = u.id
            WHERE o.id = %s
        ''', (item, ))

        item = database.getOne()

        print(item)

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        back = CTkButton(self, text="Go Back", command=lambda: self.controller.navigate('/movements')).place(y=35, x=1190, anchor="center")

        level = 200

        title = CTkLabel(self, text="Move Out Details", font=("default", 40, "bold")).place(y=15 + level, relx=0.41)

        description = CTkLabel(self, text="Item: " + item[1], font=('default', 30)).place(y=60 + level, relx=0.41)
        category = CTkLabel(self, text="Date of Movement: " + str(item[2]), font=('default', 24)).place(y=100 + level, relx=0.41)
        quantity = CTkLabel(self, text="Quantity Moved: " + str(item[3]), font=('default', 24)).place(y=130 + level, relx=0.41)
        quantity = CTkLabel(self, text="Input By: " + str(item[4]), font=('default', 24)).place(y=160 + level, relx=0.41)


