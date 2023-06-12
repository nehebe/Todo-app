import sqlite3
import datetime
import InquirerPy

conn = sqlite3.connect("todo.db")
c = conn.cursor()

# c.execute("""CREATE TABLE todo (
# 			thing_todo text,
# 			is_it_done text,
# 			time_it_was_made text
# 			)""")

screen = input("R for read, W for write: ")

if screen.lower() == "w":
	add = input("What would you like to add to the todo list?: ")
	is_done = "False"
	time_made = datetime.date.today()
	c.execute("INSERT INTO todo VALUES (?, ?, ?)", (add, is_done, time_made))
elif screen.lower() == "r":
	c.execute("SELECT * FROM todo")
	print(c.fetchall())


conn.commit()
conn.close()