import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punctuation


class PasswordGenerator:
    @staticmethod
    def generate_password(pswd_length: int):
        letters = [ascii_uppercase, ascii_lowercase, digits, punctuation]
        pswd = ''

        if pswd_length == 4:
            for i in range(4):
                choice = random.choice(letters)
                letters.remove(choice)
                pswd += random.choice(choice)
            return pswd

        for i in range(pswd_length):
            luck = random.choice(letters)
            pswd += random.choice(luck)

        return pswd

    @staticmethod
    def validate_pswd(pswd: str):
        digit = False
        lowercase = False
        uppercase  = False
        symbols = False

        for p in pswd:
            if p in digits:
                digit = True
            elif p in ascii_lowercase:
                lowercase = True
            elif p in ascii_uppercase:
                uppercase = True
            elif p in punctuation:
                symbols = True

        if all((digit,lowercase,uppercase,symbols)):
            return True
        else:
            return False

    @classmethod
    def get_pswd(cls, pswd_len: int):
        if pswd_len < 4:
            return "Error: password length must be 4 or greater."

        pswd = cls.generate_password(pswd_len)
        is_strong_pswd = cls.validate_pswd(pswd)

        if is_strong_pswd:
            return pswd
        else:
            cls.get_pswd(pswd_len)

if __name__ == '__main__':
    pswd = PasswordGenerator.get_pswd(8)
    print(pswd)