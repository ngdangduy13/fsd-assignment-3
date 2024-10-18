class Validator:
    def validate_email(self, email):
        return email.endswith('@university.com')

    def validate_password(self, password):
        return len(password) > 5 and password[0].isupper() and password[0].isalpha() and password[1:].isnumeric()
