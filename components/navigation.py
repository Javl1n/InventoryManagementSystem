from customtkinter import *


class NavigationFrame(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, height=720, **kwargs)
        self.controller = controller
        self.render()

    def logout(self):
        self.controller.setSession("")
        self.controller.navigate("/logout")

    def render(self):
        CTkButton(self, text="Items", command= lambda: self.controller.navigate("/items")).place(y=40, relx=0.5, anchor='center')
        CTkButton(self, text="Movements", command=lambda: self.controller.navigate("/movements")).place(y=100, relx=0.5, anchor='center')
        CTkButton(self, text="Suppliers", command=lambda: self.controller.navigate("/suppliers")).place(y=160, relx=0.5, anchor='center')
        CTkButton(self, text="Categories", command=lambda: self.controller.navigate("/categories")).place(y=220, relx=0.5, anchor='center')
        CTkButton(self, text="Log out", fg_color='red', command= self.logout).place(y=280, relx=0.5, anchor='center')
