# Created by nikitanovikov at 7/12/25

class Logger:

    @staticmethod
    def debug(message):
        print(f'\033[1;35m[DEBUG]:\033[0m {message}')

    @staticmethod
    def info(message):
        print(f'\033[1;34m[INFO]:\033[0m {message}')

    @staticmethod
    def error(message):
        print(f'\033[1;31m[ERROR]:\033[0m {message}')

    @staticmethod
    def warn(message):
        print(f'\033[1;33m[WARN]:\033[0m {message}')

    @staticmethod
    def success(message):
        print(f'\033[1;32m[SUCCESS]:\033[0m {message}')
