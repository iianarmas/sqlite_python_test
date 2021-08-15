import sqlite3

# Create table
# c.execute(''' CREATE TABLE person (
# 			first_name TEXT,
# 			last_name TEXT,
# 			age SMALLINT,
# 			email TEXT)
# 	''')


# Inserting values

# persons = [
# 		('John', 'Smith', 32, 'john@gmail.com'),
# 		('Jane', 'Doe', 28, 'jane@gmail.com'),
# 		('Luke', 'Brown', 31, 'luke@gmail.com'),
# 		('Corie', 'Chase', 29, 'chase@gmail.com'),
# 		('Michael', 'Prince', 27, 'mike@gmail.com')
# 		]

# c.executemany('INSERT INTO person VALUES(?,?,?,?)', persons)
# db.commit()


# Create a fxn for easier execution
# Query db and return all records
def show_all():
	# Create and connect to db
	db = sqlite3.connect('appdbase.db')

	c = db.cursor()
	
	# Select and print items in tablel
	c.execute('SELECT rowid, * FROM person')
	fetch = c.fetchall()

	for i in fetch:
		print(i)
	
	db.close()


# add new record to table
def add_one(first, last, age, email):
	# Create and connect to db
	db = sqlite3.connect('appdbase.db')

	c = db.cursor()

	c.execute('INSERT INTO person VALUES (?,?,?,?)', (first, last, age, email))

	db.commit()
	
	db.close()


# adding many records
def add_many(record):
	db = sqlite3.connect('appdbase.db')

	c = db.cursor()

	c.executemany('INSERT INTO person VALUES (?,?,?,?)', record)

	db.commit()
	
	db.close()



# delete record
def delete_one(id):
	# Create and connect to db
	db = sqlite3.connect('appdbase.db')

	c = db.cursor()

	c.execute('DELETE FROM person WHERE rowid = (?)', id)

	db.commit()
	
	db.close()

