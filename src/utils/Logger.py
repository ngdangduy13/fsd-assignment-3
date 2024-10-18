class Logger:
    @staticmethod
    def success(message):
        print(f"\033[92m{message}\033[0m")

    @staticmethod
    def error(message):
        print(f"\033[91m{message}\033[0m")
