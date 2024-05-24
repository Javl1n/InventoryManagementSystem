from customtkinter import *

from components import navigation, table
from components.items.edit import EditForm
from app.database import Database
from app.localstorage import LocalStorage


class ItemsShow(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.controller = controller

        storage = LocalStorage()

        if storage.shelf['item'] is None:
            return

        item = storage.shelf['item']

        storage.save()
        storage.close()
        database = Database()
        database.query('''
            SELECT * FROM items 
            INNER JOIN categories ON items.category_id = categories.id
            WHERE items.id = %s
        ''', (item, ))

        item = database.getOne()


        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        back = CTkButton(self, text="Go Back", command=lambda: self.controller.navigate('/items')).place(y=35, x=1190, anchor="center")

        title = CTkLabel(self, text=item[1], font=("default", 32, "bold")).place(y=20, x=220)

        description = CTkLabel(self, text="Description: " + item[2], font=('default', 24)).place(y=65, x=220)
        category = CTkLabel(self, text="Category: " + str(item[6])).place(y=95, x=220)
        quantity = CTkLabel(self, text="Current Stocks: " + str(item[3])).place(y=120, x=220)
        EditForm(self, commands=controller, item=item).place(relx=.6, rely=.5, anchor='center')


