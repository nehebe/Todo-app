import os
import sqlite3
import datetime
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy.validator import EmptyInputValidator
from InquirerPy.validator import PathValidator
from InquirerPy.validator import NumberValidator

things = []

questions_1 = [
    {
        "type": "filepath",
        "message": "Enter file to upload:",
        "name": "location",
        "default": os.getcwd(),
        "validate": PathValidator(is_file=True, message="Input is not a file"),
        "only_files": True,
    },
]        

question_2 = [
	{
		"type": "list",
		"message": "Select an action:",
		"choices": ["Read", "Write", Choice(value=None, name="Exit")],
		"default": None,
	},
]

question_3 = [
	{
		"type": "rawlist",
		"choices": [],
		"message": "Press Ctrl+C to exit",
		"default": 1,
	},
	{
		"type": "rawlist",
		 "message": "Press Ctrl+C to exit",
		"choices": [
			Choice(name="Finished task", value="fin"),
			Choice(name="Delete task", value="del"),
			Separator(line=15 * "*"),
			Choice(name="Go back", value="bak"),
		],
		"validate": lambda result: len(result) > 0,
		"invalid_message": "Minimum 1 selection",
    },			
]

db_location = prompt(questions_1)
conn = sqlite3.connect(db_location["location"])
c = conn.cursor()


# comment this out after you have the .db file
# c.execute("""CREATE TABLE todo (
# 			thing_todo text,
# 			is_it_done text,
# 			time_it_was_made text
# 			)""")


result = prompt(questions=question_2)
action = result[0]

if result[0] == "Write":
	todo = inquirer.text(message="What would you like to put in the todo list:", validate=EmptyInputValidator(),).execute()
	is_done = "False"
	time_made = datetime.date.today()
	c.execute("INSERT INTO todo VALUES (?, ?, ?)", (todo, is_done, time_made))
elif result[0] == "Read":
	c.execute("SELECT * FROM todo")
	things = c.fetchall()
	question_3[0]["choices"] = things
	readlist = prompt(question_3)
else:
	exit()


conn.commit()
conn.close()