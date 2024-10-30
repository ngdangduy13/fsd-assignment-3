import re

class Validator:
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@university\.com$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_password(password):
        pattern = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'
        return bool(re.match(pattern, password))
