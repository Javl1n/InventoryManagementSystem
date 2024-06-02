from customtkinter import *

from components import navigation, table
from app.database import Database
from app.localstorage import LocalStorage


class CategoryIndex(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        storage = LocalStorage()
        storage.shelf['category'] = None
        storage.save()
        storage.close()


        self.controller = controller

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        add_item = CTkButton(self, text="Add Category", command=lambda: self.controller.navigate('/categories/create')).place(y=35, x=1190, anchor="center")

        title = CTkLabel(self, text="CATEGORIES", font=("default", 32, "bold")).place(y=20, x=220)

        headers = {
            0: {
                'x': 25,
                'text' : "ID",
            },
            1: {
                'x': 120,
                'text' : 'Name'
            },
            2: {
                'x': 420,
                'text' : 'Description'
            },
            3: {
                'x': 850,
                'text' : ''
            },
        }


        database = Database()

        database.query("SELECT * FROM categories")

        categories = database.get()

        button = {
            'text': 'view more',
        }
        self.table = table.Table(self, controller=self, columns=headers, rows=categories, options=button).place(y=70, x=220)

    def show(self, categoryId):
        self.controller.navigate('/categories/show', {'category': categoryId})
