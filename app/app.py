from customtkinter import *
from pages.auth.loginpage import LoginPage
from pages.auth.registerpage import RegisterPage
from pages.items.index import ItemsIndex
from pages.items.create import ItemsCreate
from pages.categories.index import CategoryIndex
from pages.categories.create import CategoryCreate
from pages.movements import MovementPage
from pages.suppliers.index import SupplierIndex
from pages.suppliers.create import SupplierCreate


class App(CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.resizable(False, False)
        self.title("Inventory Management System")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.container = CTkFrame(self, fg_color="transparent")
        self.container.pack(side = "top", fill = "both", expand = True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.session = ''
        frames = {
            '/items' : ItemsIndex,
            '/items/create' : ItemsCreate,
            '/login' : LoginPage,
            '/register' : RegisterPage,
            '/suppliers' : SupplierIndex,
            '/suppliers/create' : SupplierCreate,
            '/categories' : CategoryIndex,
            '/categories/create' : CategoryCreate,
            '/movements' : MovementPage
        }
        for key, value in frames.items():
            frame = value(master=self.container, controller = self)
            self.frames[key] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.navigate("/categories")

    def navigate(self, cont):
        frame = self.frames[cont]
        frame.destroy()
        frame.__init__(master=self.container, controller = self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


    # def setSession(self, user):
    #     self.session = user