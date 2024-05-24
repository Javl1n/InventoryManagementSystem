from customtkinter import *
from app.localstorage import LocalStorage

from pages.auth.loginpage import LoginPage
from pages.auth.registerpage import RegisterPage
from pages.items.index import ItemsIndex
from pages.items.show import ItemsShow
from pages.items.create import ItemsCreate
from pages.categories.index import CategoryIndex
from pages.categories.show import CategoryShow
from pages.categories.create import CategoryCreate
from pages.movements.index import MovementPage
from pages.movements.moveIn.create import ItemsInCreate
from pages.movements.moveIn.show import MovementsInShow
from pages.movements.out.create import ItemsOutCreate
from pages.movements.out.show import MovementsOutShow
from pages.suppliers.index import SuppliersIndex
from pages.suppliers.show import SuppliersShow
from pages.suppliers.create import SuppliersCreate


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
            '/items/show': ItemsShow,
            '/items/create' : ItemsCreate,
            '/login' : LoginPage,
            '/register' : RegisterPage,
            '/suppliers' : SuppliersIndex,
            '/suppliers/show' : SuppliersShow,
            '/suppliers/create' : SuppliersCreate,
            '/categories' : CategoryIndex,
            '/categories/show' : CategoryShow,
            '/categories/create' : CategoryCreate,
            '/movements' : MovementPage,
            '/movements/in/create' : ItemsInCreate,
            '/movements/in' : MovementsInShow,
            '/movements/out/create' : ItemsOutCreate,
            '/movements/out' : MovementsOutShow,
        }
        for key, value in frames.items():
            frame = value(master=self.container, controller = self)
            self.frames[key] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.navigate("/login")

    def navigate(self, cont, params = None):
        frame = self.frames[cont]

        requests = LocalStorage()
        if params is not None:
            for key, value in params.items():
                requests.shelf[key] = value
            requests.save()
            requests.close()

        frame.destroy()
        frame.__init__(master=self.container, controller = self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()