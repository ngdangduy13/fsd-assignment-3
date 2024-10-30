from models.Database import Database

class Admin:
    # Initializes the Admin class with id, email, password, and name attributes.
    def __init__(self, id, email, password, name):
        self.id = id  # Unique identifier for the admin.
        self.email = email  # Email address of the admin.
        self.password = password  # Password for admin authentication.
        self.name = name  # Name of the admin.

    # Provides a string representation of the Admin object, showing email and name.
    def __str__(self):
        return f"Email: {self.email}, Name: {self.name}"
