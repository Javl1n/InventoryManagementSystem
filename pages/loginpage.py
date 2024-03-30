from customtkinter import *

from auth.login.loginform import LoginForm



class LoginPage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.navigation = controller

        self.frame = LoginForm(self, commands=self).place(relx=0.5, rely=0.5, anchor="center")

    def login(self):
        self.navigation.show_frame("ItemPage")


    def register(self):
        self.navigation.show_frame("RegisterPage")

