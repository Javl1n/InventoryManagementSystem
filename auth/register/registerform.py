from customtkinter import *

class RegisterForm(CTkFrame):
    def __init__(self, master, commands, **kwargs):
        super().__init__(master, **kwargs)
        self.registerForm(self, commands)

    def registerForm(self, master, commands):
        registerTitle = CTkLabel(master = master, text="Register", font=('default', 32, 'bold'))
        registerTitle.grid(padx=20, pady=20, row= 0, columnspan= 2)

        username = CTkEntry(master = master, placeholder_text="username", width=200)
        username.grid(padx=20, pady=10, row= 1, columnspan= 2)

        password = CTkEntry(master = master, placeholder_text="password", width=200)
        password.grid(padx=20, pady=10, row= 2, columnspan= 2)

        submit = CTkButton(master = master, text="LOGIN", width=200, command=commands.register).grid(pady=20, row= 3, columnspan= 2)

        registrationDescription = CTkLabel(master = master,
                                           text="Already have an account?",
                                           fg_color='transparent').grid(pady=0, row= 4, column= 0)
        registrationButton = CTkButton(master = master,
                                       text="log in instead",
                                       fg_color='transparent',
                                       text_color='#87ceeb',
                                       hover=False,
                                       height=0,
                                       width=0,
                                       command=commands.login).grid(pady=5, row= 4, column= 1)