from customtkinter import *
from app.database import Database
from app.localstorage import LocalStorage

# MOVEMENT OUT
class CreateForm (CTkFrame):
    def __init__(self, master, commands, **kwargs):
        super().__init__(master, width=620, height=250, **kwargs)

        self.controller = commands

        itemLabel = CTkLabel(self, text="Item")
        itemLabel.place(x=10, y=10)

        self.itemInput = CTkOptionMenu(self, values=self.items(), width=600)
        self.itemInput.place(relx=.5, y=35, anchor="n")

        dateLabel = CTkLabel(self, text="Date")
        dateLabel.place(x=10, y=70)

        self.monthInput = CTkEntry(self, placeholder_text="Month (1-12)", width=195)
        self.monthInput.place(x=10, y=95)

        self.dayInput = CTkEntry(self, placeholder_text="Day (1-31)", width=195)
        self.dayInput.place(x=10+200, y=95)

        self.yearInput = CTkEntry(self, placeholder_text="Year", width=200)
        self.yearInput.place(x=10+400, y=95)

        ammountLabel = CTkLabel(self, text="Amount")
        ammountLabel.place(x=10, y=130)

        self.ammount = CTkEntry(self, placeholder_text="Aa", width=600)
        self.ammount.place(relx=.5, y=155, anchor="n")

        submitButton = CTkButton(self, text="SUBMIT", command=self.submit)
        submitButton.place(relx=.5, y=230, anchor="s")

    def submit(self):
        month = self.monthInput.get()
        day = self.dayInput.get()
        year = self.yearInput.get()
        ammount = self.ammount.get()


        if month == '' or day == '' or year == '' or ammount == '':
            return

        database = Database()
        database.query("SELECT id, quantity FROM items WHERE `name` = %s", (self.itemInput.get(),))

        item = database.getOne()
        itemId = item[0]
        originalQuantity = item[1]

        storage = LocalStorage()
        user = storage.shelf['user']['id']

        database.query("INSERT INTO item_out(item_id, date, quantity, user_id) VALUES (%s, %s, %s, %s)", (itemId, year + '-' + month + '-' + day, ammount, user))
        database.commit()

        database.query("UPDATE items SET quantity=%s WHERE id=%s", (
            int(originalQuantity) - int(ammount),
            itemId
        ))
        database.commit()

        self.controller.navigate('/movements')


    def suppliers(self):
        database = Database()
        database.query("Select name FROM suppliers")
        categoriesData = database.get()
        categoriesArray = [];

        for category in categoriesData:
            categoriesArray.append(category[0])

        return categoriesArray

    def items(self):
        database = Database()
        database.query("Select name FROM items")
        categoriesData = database.get()
        categoriesArray = [];

        for category in categoriesData:
            categoriesArray.append(category[0])

        return categoriesArray
