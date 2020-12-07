import sqlite3
import datetime
#Initializes connection with database and intializes tables in the database
dbconnect = sqlite3.connect("parkinglot.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();

plate_number = 'L1V3A6'
now = datetime.datetime.now()
entry_time = now.strftime("%H:%M:%S")


#creates a table that ensure there are no duplicate cars (plate numbers) being entered
cursor.execute('''
    CREATE TABLE IF NOT EXISTS CarDosier (
    PlateNumber TEXT,
    EntryTime TEXT,
    ExitTime TEXT,
    hasPaid INTEGER,
    Amount DOUBLE)''');
cursor.execute('''INSERT INTO CarDosier (PlateNumber, EntryTime, ExitTime, hasPaid, Amount) VALUES (?, ?, '0', 0, 0)''', (plate_number, entry_time));
dbconnect.commit();
cursor.execute('SELECT * FROM CarDosier');
for row in cursor:
        print(row['PlateNumber'],row['EntryTime'],row['ExitTime'], row['hasPaid'], row['Amount']);
dbconnect.close()