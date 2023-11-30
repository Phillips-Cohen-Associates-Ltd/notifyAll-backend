import secrets
import string

class Utils():
    @staticmethod
    def generate_random_code():
        characters = string.ascii_letters + string.digits
        code = ''.join(secrets.choice(characters) for _ in range(6))
        return code
