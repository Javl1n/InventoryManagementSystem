from customtkinter import *


class NavigationFrame(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, height=720, **kwargs)
        self.navigation = controller
        self.render()


    def render(self):
        CTkButton(self, text="Items", command= lambda: self.navigation.show_frame("ItemPage")).place(y=40, relx=0.5, anchor='center')
        CTkButton(self, text="Movements", command=lambda: self.navigation.show_frame("MovementPage")).place(y=100, relx=0.5, anchor='center')
        CTkButton(self, text="Suppliers", command=lambda: self.navigation.show_frame("SupplierPage")).place(y=160, relx=0.5, anchor='center')
        CTkButton(self, text="Categories", command=lambda: self.navigation.show_frame("CategoryPage")).place(y=220, relx=0.5, anchor='center')
        CTkButton(self, text="Log out", fg_color='red', command= lambda: self.navigation.show_frame("LoginPage")).place(y=280, relx=0.5, anchor='center')
