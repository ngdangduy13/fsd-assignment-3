
from models.Database import Database


class Admin:
    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = password
        self.name = name

    def __str__(self):
        return f"Email: {self.email}, Name: {self.name}"
