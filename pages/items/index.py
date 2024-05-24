from customtkinter import *
from components import navigation, table
from app.localstorage import LocalStorage
from app.database import Database


class ItemsIndex(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        session = LocalStorage()

        self.user = session.shelf["user"]

        session.close()

        title = CTkLabel(self, text="ITEM MANAGEMENT", font=("default", 32, "bold")).place(y=35, x=220, anchor="w")

        add_item = CTkButton(self, text="Add Item", command=lambda: self.controller.navigate('/items/create')).place(y=35, x=1190, anchor="center")

        headers = {
            0: {
                'x': 25,
                'text': "ID",
            },
            1: {
                'x': 120,
                'text': 'Name'
            },
            2: {
                'x': 320,
                'text': 'Description'
            },
            3: {
                'x': 700,
                'text': 'Quantity'
            },
            4: {
                'x': 850,
                'text': ''
            },
        }

        database = Database()

        database.query("SELECT * FROM items")

        items = database.get()

        button = {
            'text': 'view more',
        }
        self.table = table.Table(self, controller=self, columns=headers, rows=items, options=button).place(y=70, x=220)

    def show(self, itemId):
        self.controller.navigate('/items/show', {'item': itemId})
