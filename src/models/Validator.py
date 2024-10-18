import re

class Validator:
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@university\.com$'
        return bool(re.match(pattern, email))

    def validate_password(self, password):
        pattern = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'
        return bool(re.match(pattern, password))
