from customtkinter import *
from app.localstorage import LocalStorage


class NavigationFrame(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, height=720, **kwargs)

        session = LocalStorage()
        self.user = session.shelf['user'] if session.shelf['user'] is not None else None
        session.close()

        self.controller = controller
        self.render()

    def logout(self):
        session = LocalStorage()
        session.shelf['user'] = {
            'id': '',
            'name': ''
        }
        session.save()
        session.close()

        self.controller.navigate("/login")

    def render(self):

        CTkLabel(self, text=f"{self.user['name'].upper()}", font=('default', 24, 'bold')).place(y=40, relx=0.5, anchor='center')
        CTkButton(self, text="Items", command= lambda: self.controller.navigate("/items")).place(y=100, relx=0.5, anchor='center')
        CTkButton(self, text="Movements", command=lambda: self.controller.navigate("/movements")).place(y=160, relx=0.5, anchor='center')
        CTkButton(self, text="Suppliers", command=lambda: self.controller.navigate("/suppliers")).place(y=220, relx=0.5, anchor='center')
        CTkButton(self, text="Categories", command=lambda: self.controller.navigate("/categories")).place(y=280, relx=0.5, anchor='center')
        CTkButton(self, text="Log out", fg_color='red', command= self.logout).place(y=340, relx=0.5, anchor='center')
