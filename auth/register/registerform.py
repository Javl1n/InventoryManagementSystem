from customtkinter import *
from database import Database

class RegisterForm(CTkFrame):
    def __init__(self, master, navigation, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = navigation


        self.render(self)

    def register(self):
        db = Database()

        username = self.username.get()
        password = self.password.get()
        contact = self.contacts.get()

        db.query("INSERT INTO users (username, password, contact) VALUES (%s, %s, %s)", (username, password, contact))
        db.commit()

        self.controller.navigate('/login')

    def render(self, master):
        registerTitle = CTkLabel(master = master, text="Register", font=('default', 32, 'bold'))
        registerTitle.grid(padx=20, pady=20, row= 0, columnspan= 2)

        self.username = CTkEntry(master = master, placeholder_text="username", width=200)
        self.username.grid(padx=20, pady=10, row= 1, columnspan= 2)

        self.password = CTkEntry(master = master, placeholder_text="password", show="*", width=200)
        self.password.grid(padx=20, pady=10, row= 2, columnspan= 2)

        self.contacts = CTkEntry(master=master, placeholder_text="contact", width=200)
        self.contacts.grid(padx=20, pady=10, row=3, columnspan=2)

        submit = CTkButton(master = master, text="REGISTER", width=200, command=self.register).grid(pady=20, row= 4, columnspan= 2)

        registrationDescription = CTkLabel(master = master,
                                           text="Already have an account?",
                                           fg_color='transparent').grid(pady=0, row= 5, column= 0)

        registrationButton = CTkButton(
            master = master,
            text="log in instead",
            fg_color='transparent',
            text_color='#87ceeb',
            hover=False,
            height=0,
            width=0,
            command=lambda: self.controller.navigate('/login')
        ).grid(pady=5, row= 5, column= 1)


