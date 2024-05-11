from customtkinter import *
from app.database import Database

class CreateForm (CTkFrame):
    def __init__(self, master, commands, **kwargs):
        super().__init__(master, width=620, height=190, **kwargs)

        self.controller = commands

        titleLabel = CTkLabel(self, text="Name:")
        titleLabel.place(x=10, y=10)

        self.titleInput = CTkEntry(self, placeholder_text="Aa", width=600)
        self.titleInput.place(relx=.5, y=35, anchor="n")

        descriptionLabel = CTkLabel(self, text="Description")
        descriptionLabel.place(x=10, y=70)

        self.descriptionInput = CTkEntry(self, placeholder_text="Aa", width=600)
        self.descriptionInput.place(relx=.5, y=95, anchor="n")

        submitButton = CTkButton(self, text="SUBMIT", command=self.submit)
        submitButton.place(relx=.5, y=180, anchor="s")

    def submit(self):
        title = self.titleInput.get()
        description = self.descriptionInput.get()

        db = Database()
        db.query("INSERT INTO `categories`(name, description) VALUES (%s, %s)", (title, description))
        db.commit()

        self.controller.navigate('/categories')