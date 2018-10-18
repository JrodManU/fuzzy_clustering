import sqlite3
import datetime
from suggestion_processor import process_suggestion

conn = sqlite3.connect('laundromat.db')

# the test file is just one string per line
file = open("test_data/shwe.txt", "r")
for line in file:
    #strip the line since we don't want trailing whitespace
    sug = (line.strip(), str(datetime.datetime.now()), "Joe Schmoe")
    process_suggestion(conn, sug)

c_suggestions = conn.cursor()
c_suggestions.execute("SELECT * FROM suggestions")
c_groups = conn.cursor()
c_groups.execute("SELECT * FROM suggestion_groups")

print("suggestions")
for row in c_suggestions:
    print(row)

print("suggestion_groups")
for row in c_groups:
    print(row)

conn.close()
