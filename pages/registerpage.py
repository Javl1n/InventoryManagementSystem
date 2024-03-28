from customtkinter import *

from auth.register.registerform import RegisterForm
from pages import loginpage


class RegisterPage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.navigation = controller

        self.frame = RegisterForm(self, commands=self).place(relx=0.5, rely=0.5, anchor="center")

    def register(self):
        pass

    def login(self):
        self.navigation.show_frame(loginpage.LoginPage)