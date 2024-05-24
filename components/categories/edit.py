from customtkinter import *
from app.database import Database

class EditForm (CTkFrame):
    def __init__(self, master, commands, category, **kwargs):
        super().__init__(master, width=620, height=225, **kwargs)

        self.controller = commands

        self.category = category

        header = CTkLabel(self, text="Edit Category", font=('default', 24, 'bold'))
        header.place(relx=.5, y=10, anchor="n")

        titleLabel = CTkLabel(self, text="Name:")
        titleLabel.place(x=10, y=35)

        self.titleInput = CTkEntry(self, placeholder_text=self.category[1], width=600)
        self.titleInput.place(relx=.5, y=60, anchor="n")

        descriptionLabel = CTkLabel(self, text="Description")
        descriptionLabel.place(x=10, y=95)

        self.descriptionInput = CTkEntry(self, placeholder_text=self.category[2], width=600)
        self.descriptionInput.place(relx=.5, y=120, anchor="n")

        submitButton = CTkButton(self, text="SAVE", command=self.submit)
        submitButton.place(relx=.985, y=190, anchor="e")

        deleteButton = CTkButton(self, text="DELETE", fg_color="red", command=self.delete)
        deleteButton.place(relx=.015, y=190, anchor="w")

    def submit(self):
        title = self.titleInput.get()
        description = self.descriptionInput.get()

        if title == '' or description == '':
            if title == '':
                title = self.category[1]
            if description == '':
                description = self.category[2]

        db = Database()
        db.query("UPDATE `categories` SET name=%s, description=%s WHERE id=%s", (title, description, self.category[0]))
        db.commit()

        self.controller.navigate('/categories/show')

    def delete(self):
        db = Database()
        db.query("DELETE FROM categories WHERE id = %s", (self.category[0], ))
        db.commit()
        db.query('SELECT * FROM categories')
        categoryId = db.getOne()
        self.controller.navigate('/categories',{'category': categoryId})