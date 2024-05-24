from customtkinter import *
from components.movements.out import create
from components import navigation, table

class ItemsOutCreate(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)
        title = CTkLabel(self, text="ADD MOVEMENT: OUT", font=("default", 32, "bold")).place(y=35, x=220, anchor="w")

        add_item = CTkButton(self, text="Go back", command=lambda: self.controller.navigate('/movements')).place(y=35, x=1190, anchor="center")

        create.CreateForm(self, commands=controller).place(relx=.6, rely=.4, anchor='center')
