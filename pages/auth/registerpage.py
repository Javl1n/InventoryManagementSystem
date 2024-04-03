from customtkinter import *

from auth.register.registerform import RegisterForm


class RegisterPage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.frame = RegisterForm(self, navigation=controller).place(relx=0.5, rely=0.5, anchor="center")