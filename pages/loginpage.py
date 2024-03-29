from customtkinter import *

from auth.login.loginform import LoginForm
from pages import registerpage

class LoginPage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.navigation = controller

        self.frame = LoginForm(self, commands=self).place(relx=0.5, rely=0.5, anchor="center")

    def login(self):
        pass

    def register(self):
        self.navigation.show_frame(registerpage.RegisterPage)

