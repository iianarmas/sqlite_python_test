import testdb


# add one records
# testdb.add_one('Caroline', 'McGuiver', 30, 'carol@gmail.com')


# add multiple records
# new = [
# 		('Nick', 'Johnson', 34, 'nik@gmail.com'),
# 		('Randy', 'O\'neil', 32, 'rand@gmail.com'),
# 		('Anne', 'Nicholas', 29, 'anne@gmail.com')
# 	]

# testdb.add_many(new)


# in deleting, must pass a str instead of an int whenever a placeholder is used
# testdb.delete_one('6')

testdb.show_all()
