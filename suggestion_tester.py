import sqlite3
import datetime
from suggestion_processor import process_suggestion

conn = sqlite3.connect('laundromat.db')

sug1 = ("wash carpet", str(datetime.datetime.now()), "Joe Schmoe")
process_suggestion(conn, sug1)
sug1 = ("wash carpet", str(datetime.datetime.now()), "Joe Schmoe")
process_suggestion(conn, sug1)
sug1 = ("wash cerpet", str(datetime.datetime.now()), "Joe Schmoe")
process_suggestion(conn, sug1)
sug1 = ("wash floor", str(datetime.datetime.now()), "Joe Schmoe")
process_suggestion(conn, sug1)

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
