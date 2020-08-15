from PyInquirer import prompt
from simple_chalk import chalk, green, red
import functions as func

questions = [
    {
        "type": "list",
        "name": "tasks",
        "message": "What would you like to do?",
        "choices": [
            "Remove .png files from your desktop",
            "Delete files from a directory",
            "Delete whole directories and their contents",
        ],
    }
]

answers = prompt(questions)

if answers["tasks"] == "Remove .png files from your desktop":
    func.clear_desktop_of_pngs()
    print(chalk.green(".png files have now been removed."))

