from customtkinter import *
from app.database import Database

class CreateForm (CTkFrame):
    def __init__(self, master, commands, **kwargs):
        super().__init__(master, width=620, height=260, **kwargs)

        self.controller = commands

        titleLabel = CTkLabel(self, text="Title")
        titleLabel.place(x=10, y=10)

        self.titleInput = CTkEntry(self, placeholder_text="Aa", width=600)
        self.titleInput.place(relx=.5, y=35, anchor="n")

        descriptionLabel = CTkLabel(self, text="Description")
        descriptionLabel.place(x=10, y=70)

        self.description = CTkEntry(self, placeholder_text="Aa", width=600)
        self.description.place(relx=.5, y=95, anchor="n")

        categoryLabel = CTkLabel(self, text="Category")
        categoryLabel.place(x=10, y=130)

        self.category = CTkOptionMenu(self, values=self.categories(), width=600)
        self.category.place(relx=.5, y=155, anchor="n")

        submitButton = CTkButton(self, text="SUBMIT", command=self.submit)
        submitButton.place(relx=.5, y=240, anchor="s")

    def submit(self):
        name = self.titleInput.get()
        description = self.description.get()

        if name == '' or description == '':
            return

        database = Database()
        database.query("SELECT id FROM categories WHERE `name` = %s", (self.category.get(),))

        category = database.getOne()[0]

        database.query("INSERT INTO items(name, description, quantity, category_id) VALUES (%s, %s, %s, %s)", (name, description, 0, category))
        database.commit()

        self.controller.navigate('/items')


    def categories(self):
        database = Database()
        database.query("Select name FROM categories")
        categoriesData = database.get()
        categoriesArray = [];

        for category in categoriesData:
            categoriesArray.append(category[0])

        return categoriesArray


