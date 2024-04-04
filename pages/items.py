from customtkinter import *
from components import navigation, table



class ItemPage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)
        title = CTkLabel(self, text="ITEM MANAGEMENT", font=("default", 32, "bold")).place(y=20, x=220)

        self.columns = {
            "ID" : {
                'x' : 25
            },
            'Name' : {
                'x' : 120
            },
            'Quantity' : {
                'x': 420
            },
            'Category' : {
                'x': 620
            },
            'Options' : {
                'x': 920
            },
        }

        self.table = table.Table(self, controller=self, columns = self.columns).place(y=70, x=220)
