from customtkinter import *
from pages import home
from pages import loginpage


class NavigationFrame(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.navigation = controller
        self.render()


    def render(self):
        CTkButton(self, text="Home", command= lambda: self.navigation.show_frame(home.HomePage)).grid(row=0, column=0, pady=20, padx=20)
        CTkButton(self, text="Log out", fg_color='red', command= lambda: self.navigation.show_frame(loginpage.LoginPage)).grid(row=1, column=0)
