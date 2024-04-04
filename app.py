from customtkinter import *
from pages.auth.loginpage import LoginPage
from pages.auth.registerpage import RegisterPage
from pages.items import ItemPage
from pages.categories import CategoryPage
from pages.movements import MovementPage
from pages.suppliers import SupplierPage


class App(CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.resizable(False, False)
        self.title("Inventory Management System")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = CTkFrame(self, fg_color="transparent")
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.session = ''
        frames = {
            '/items' : ItemPage,
            '/login' : LoginPage,
            '/register' : RegisterPage,
            '/suppliers' : SupplierPage,
            '/categories' : CategoryPage,
            '/movements' : MovementPage
        }
        for key, value in frames.items():
            frame = value(master=container, controller = self)
            self.frames[key] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.navigate("/login")

    def navigate(self, cont):
        # if not self.session:
        #     frame = self.frames["/login"]
        # else:
        frame = self.frames[cont]
        frame.tkraise()

    # def setSession(self, user):
    #     self.session = user