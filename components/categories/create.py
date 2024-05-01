from customtkinter import *

class CreateForm (CTkFrame):
    def __init__(self, master, commands, **kwargs):
        super().__init__(master, width=620, height=190, **kwargs)

        self.controller = commands

        titleLabel = CTkLabel(self, text="Name:")
        titleLabel.place(x=10, y=10)

        titleInput = CTkEntry(self, placeholder_text="Aa", width=600)
        titleInput.place(relx=.5, y=35, anchor="n")

        descriptionLabel = CTkLabel(self, text="Description")
        descriptionLabel.place(x=10, y=70)

        description = CTkEntry(self, placeholder_text="Aa", width=600)
        description.place(relx=.5, y=95, anchor="n")

        submitButton = CTkButton(self, text="SUBMIT")
        submitButton.place(relx=.5, y=180, anchor="s")


