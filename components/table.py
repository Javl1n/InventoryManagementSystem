from customtkinter import *

class Table(CTkFrame):
    def __init__(self, master, controller, columns, **kwargs):
        super().__init__(master, width=1040, height=630,  **kwargs)

        for key, value in columns.items():
            CTkLabel(self, text=key, font=('default', 12, 'bold')).place(x=value['x'], y=10)
