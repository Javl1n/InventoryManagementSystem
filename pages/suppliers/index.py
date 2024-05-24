from customtkinter import *

from components import navigation, table
from app.database import Database


class SuppliersIndex(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.controller = controller

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        title = CTkLabel(self, text="SUPPLIERS", font=("default", 32, "bold")).place(y=20, x=220)

        add_item = CTkButton(self, text="Add Supplier", command=lambda: self.controller.navigate('/suppliers/create')).place(y=35, x=1190, anchor="center")

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
                'text': 'Address'
            },
            3: {
                'x': 700,
                'text': 'Contact'
            },
            4: {
                'x': 850,
                'text': ''
            },
        }

        database = Database()

        database.query("SELECT * FROM suppliers")

        categories = database.get()

        button = {
            'text': 'view more',
        }

        self.table = table.Table(self, controller=self, columns=headers, rows=categories, options=button).place(y=70, x=220)

    def show(self, supplierId):
        self.controller.navigate('/suppliers/show', {'supplier': supplierId})