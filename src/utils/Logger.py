from utils.String import StringUtils


class Logger:
    @staticmethod
    def log_green(message):
        print(f"\033[92m{message}\033[0m")

    @staticmethod
    def log_red(message):
        print(StringUtils.to_red_string(message))

    @staticmethod
    def log_yellow(message):
        print(f"\033[93m{message}\033[0m")

    @staticmethod
    def log_cyan(message):
        print(StringUtils.to_cyan_string(message))


