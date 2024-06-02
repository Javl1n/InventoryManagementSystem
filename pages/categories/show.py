from customtkinter import *

from components import navigation, table
from components.categories.edit import EditForm
from app.database import Database
from app.localstorage import LocalStorage


class CategoryShow(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.controller = controller

        storage = LocalStorage()


        if storage.shelf['category'] is None:
            return

        category = storage.shelf['category']

        storage.save()
        storage.close()
        database = Database()
        database.query("SELECT * FROM categories WHERE `id` = %s", (category,))

        category = database.getOne()

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        back = CTkButton(self, text="Go Back", command=lambda: self.controller.navigate('/categories')).place(y=35,
                                                                                                              x=1190,
                                                                                                              anchor="center")

        title = CTkLabel(self, text=category[1], font=("default", 32, "bold")).place(y=20, x=220)

        description = CTkLabel(self, text="Description: " + category[2], font=('default', 20)).place(y=60, x=220)

        EditForm(self, commands=controller, category=category).place(relx=.6, rely=.4, anchor='center')
