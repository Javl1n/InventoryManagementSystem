from customtkinter import *

from components import navigation, table
from components.suppliers.edit import EditForm
from app.database import Database
from app.localstorage import LocalStorage


class SuppliersShow(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.controller = controller

        storage = LocalStorage()

        if storage.shelf['supplier'] is None:
            return

        supplier = storage.shelf['supplier']

        storage.save()
        storage.close()
        database = Database()
        database.query('''
            SELECT * FROM suppliers 
            WHERE id = %s
        ''', (supplier, ))

        supplier = database.getOne()


        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        back = CTkButton(self, text="Go Back", command=lambda: self.controller.navigate('/items')).place(y=35, x=1190, anchor="center")

        name = CTkLabel(self, text=supplier[1], font=("default", 32, "bold")).place(y=20, x=220)

        address = CTkLabel(self, text="Address: " + supplier[2], font=('default', 24)).place(y=65, x=220)
        contact = CTkLabel(self, text="Contact Number: " + str(supplier[3])).place(y=95, x=220)
        EditForm(self, commands=controller, supplier=supplier).place(relx=.6, rely=.5, anchor='center')


