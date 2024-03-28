from customtkinter import *

class HomePage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        label = CTkLabel(self, text="Welcome").pack()
