from customtkinter import *
from database import Database
import shelve

class LoginForm(CTkFrame):
    def __init__(self, master, commands, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = commands

        self.render(self)

    def login(self):
        db = Database()

        username = self.username.get()
        password = self.password.get()

        db.query(
            "SELECT * FROM users WHERE `username` = %s AND `password` = %s",
            (username, password)
        )

        user = db.getOne()

        if user:
            self.controller.navigate('/items')

        else:
            self.message.configure(text="incorrect credentials", text_color='red')

    def render(self, master):
        loginTitle = CTkLabel(master = master, text="Log In", font=('default', 32, 'bold'))
        loginTitle.grid(padx=20, pady=20, row= 0, columnspan= 2)

        self.username = CTkEntry(master = master, placeholder_text="username", width=200)
        self.username.grid(padx=20, pady=10, row= 1, columnspan= 2)

        self.password = CTkEntry(master = master, placeholder_text="password", show="*", width=200)
        self.password.grid(padx=20, pady=10, row= 2, columnspan= 2)

        submit = CTkButton(master = master, text="LOGIN", width=200, command=self.login)
        submit.grid(pady=(20, 0), row= 3, columnspan= 2)

        self.message = CTkLabel(master=master, text="", font=('default', 12))
        self.message.grid(padx=20, row=4, columnspan=2)

        registrationDescription = CTkLabel(
            master = master,
            text="Don't have an account?",
            fg_color='transparent'
        )
        registrationDescription.grid(pady=0, row= 5, column= 0)


        registrationButton = CTkButton(
            master = master,
            text="register",
            fg_color='transparent',
            text_color='#87ceeb',
            hover=False,
            height=0,
            width=0,
            command=lambda: self.controller.navigate("/register")
        )
        registrationButton.grid(pady=5, row= 5, column= 1)