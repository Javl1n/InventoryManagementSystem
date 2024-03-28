from customtkinter import *
from pages.loginpage import LoginPage
from pages.registerpage import RegisterPage
from home import HomePage

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Inventory Management System")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = CTkFrame(self, fg_color="transparent")
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, LoginPage, RegisterPage):
            frame = F(master=container, controller = self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(LoginPage)
        # self.login.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

