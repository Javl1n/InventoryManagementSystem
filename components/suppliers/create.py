from customtkinter import *

from app.database import Database

class CreateForm (CTkFrame):
    def __init__(self, master, commands, **kwargs):
        super().__init__(master, width=620, height=260, **kwargs)

        self.controller = commands

        titleLabel = CTkLabel(self, text="Name:")
        titleLabel.place(x=10, y=10)

        self.titleInput = CTkEntry(self, placeholder_text="Aa", width=600)
        self.titleInput.place(relx=.5, y=35, anchor="n")

        addressLabel = CTkLabel(self, text="Address:")
        addressLabel.place(x=10, y=70)

        self.addressInput = CTkEntry(self, placeholder_text="Aa", width=600)
        self.addressInput.place(relx=.5, y=95, anchor="n")

        contactLabel = CTkLabel(self, text="Contact:")
        contactLabel.place(x=10, y=130)

        self.contactInput = CTkEntry(self, placeholder_text="+63", width=600)
        self.contactInput.place(relx=.5, y=155, anchor="n")

        submitButton = CTkButton(self, text="SUBMIT", command=self.submit)
        submitButton.place(relx=.5, y=240, anchor="s")

    def submit(self):
        name = self.titleInput.get()
        address = self.addressInput.get()
        contact = self.contactInput.get()

        if name == '' or address == '' or contact == '':
            return

        db = Database()
        db.query("INSERT INTO `suppliers`(name, address, contact) VALUES (%s, %s, %s)", (name, address, contact))
        db.commit()

        self.controller.navigate('/suppliers')

