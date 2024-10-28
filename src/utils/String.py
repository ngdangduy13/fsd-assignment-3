class StringUtils:
    @staticmethod
    def to_cyan_string(str):
        return f"\033[96m{str}\033[0m"

    @staticmethod
    def to_red_string(str):
        return f"\033[91m{str}\033[0m"
