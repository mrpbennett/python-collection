import string
import secrets
from PyInquirer import prompt

questions = [
    {
        'type': 'list',
        'name': 'tasks',
        'message': 'What would you like to generate?',
        'choices': [
            'Password',
            'Hexadecimal',

        ]
    }
]

answers = prompt(questions)

# password generator that uses all case type, digits and special charactors 
def password_generator(size=25, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(secrets.SystemRandom().choice(chars) for _ in range(size))
    

# hexcode generator that takes a number as an argument and generates a token of that length
def hex_generator(size):
    return secrets.token_hex(size)


if answers['tasks'] == 'Password':
    print(password_generator(25))

if answers['tasks'] == 'Hexadecimal':
    print(hex_generator(25))