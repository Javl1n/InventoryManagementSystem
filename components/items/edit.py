from customtkinter import *
from app.database import Database

class EditForm (CTkFrame):
    def __init__(self, master, commands, item, **kwargs):
        super().__init__(master, width=620, height=275, **kwargs)

        self.controller = commands
        self.item = item


        header = CTkLabel(self, text="Edit Item", font=('default', 24, 'bold'))
        header.place(relx=.5, y=10, anchor="n")

        titleLabel = CTkLabel(self, text="Name: ")
        titleLabel.place(x=10, y=35)

        self.titleInput = CTkEntry(self, placeholder_text=self.item[1], width=600)
        self.titleInput.place(relx=.5, y=60, anchor="n")

        descriptionLabel = CTkLabel(self, text="Description")
        descriptionLabel.place(x=10, y=95)

        self.descriptionInput = CTkEntry(self, placeholder_text=self.item[2], width=600)
        self.descriptionInput.place(relx=.5, y=120, anchor="n")

        categoryLabel = CTkLabel(self, text="Category")
        categoryLabel.place(x=10, y=150)
        categoryVariable = StringVar(value=self.item[6])
        self.category = CTkOptionMenu(self, values=self.categories(), width=600, variable=categoryVariable)
        self.category.place(relx=.5, y=175, anchor="n")

        submitButton = CTkButton(self, text="SAVE", command=self.submit)
        submitButton.place(relx=.985, y=240, anchor="e")

        deleteButton = CTkButton(self, text="DELETE", fg_color="red", command=self.delete)
        deleteButton.place(relx=.015, y=240, anchor="w")

    def submit(self):
        title = self.titleInput.get()
        description = self.descriptionInput.get()

        if title == '' or description == '':
            if title == '':
                title = self.item[1]
            if description == '':
                description = self.item[2]

        db = Database()
        db.query("SELECT id FROM categories WHERE `name` = %s", (self.category.get(),))

        category = db.getOne()[0]
        db.query("UPDATE `items` SET name=%s, description=%s, category_id=%s WHERE id=%s", (title, description, category, self.item[0]))
        db.commit()

        self.controller.navigate('/items/show')

    def delete(self):
        db = Database()
        db.query("DELETE FROM items WHERE id = %s", (self.item[0],))
        db.commit()
        db.query('SELECT * FROM items')
        itemId = db.getOne()
        self.controller.navigate('/items',{'item': itemId})

    def categories(self):
        database = Database()
        database.query("Select name FROM categories")
        categoriesData = database.get()
        categoriesArray = [];

        for category in categoriesData:
            categoriesArray.append(category[0])

        return categoriesArray
