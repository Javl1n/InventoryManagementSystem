from customtkinter import *

from navigation import *


class HomePage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.navigation = controller

        NavigationFrame(self, controller=controller).grid(row=0, column=0, sticky="nsew")
