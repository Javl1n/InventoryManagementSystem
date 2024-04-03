from customtkinter import *

from components import navigation


class SupplierPage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.navigation = controller

        navigation.NavigationFrame(self, controller=controller).grid(row=0, column=0, rowspan=200, sticky="nsew")

        title = CTkLabel(self, text="SUPPLIERS", font=("default", 32, "bold")).grid(row=0, column=1, padx=20, pady=20)