import string
import secrets
from PyInquirer import prompt

questions = [
    {
        "type": "list",
        "name": "tasks",
        "message": "What would you like to generate?",
        "choices": ["Password", "Token"],
    }
]

answers = prompt(questions)

# password generator that uses all case type, digits and special charactors
def password_generator(
    size=25, chars=string.ascii_letters + string.digits + string.punctuation
):
    return "".join(secrets.SystemRandom().choice(chars) for _ in range(size))


# token generator that takes a number as an argument and generates a token of that length
def token_generator(size):
    return secrets.token_hex(size)


if answers["tasks"] == "Password":
    print(password_generator(25))

if answers["tasks"] == "Token":
    size = input("how many bytes?: ")
    print(token_generator(int(size)))
