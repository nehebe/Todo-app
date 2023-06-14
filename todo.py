import sqlite3
import datetime
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator


conn = sqlite3.connect("todo.db")
c = conn.cursor()


# comment this out after you have the .db file
c.execute("""CREATE TABLE todo (
			thing_todo text,
			is_it_done text,
			time_it_was_made text
			)""")

question_1 = [
	{
		"type": "list",
		"message": "Select an action:",
		"choices": ["Read", "Write", Choice(value=None, name="Exit")],
		"default": None,
	},
]

result = prompt(questions=question_1)

if result[0] == "Write":
	todo = inquirer.text(message="What would you like to put in the todo list:", validate=EmptyInputValidator(),).execute()
	is_done = "False"
	time_made = datetime.date.today()
	c.execute("INSERT INTO todo VALUES (?, ?, ?)", (todo, is_done, time_made))
elif result[0] == "Read":
	c.execute("SELECT * FROM todo")
	print(c.fetchall())
else:
	exit()