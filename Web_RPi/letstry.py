import datetime
import sqlite3

dbconnect = sqlite3.connect("parkinglot.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();

cursor.execute('''
    CREATE TABLE IF NOT EXISTS CarDosier (
    PlateNumber TEXT UNIQUE,
    EntryTime TEXT,
    ExitTime TEXT,
    hasPaid INTEGER,
    Amount DOUBLE)''');

def compare_time(time):
    #Gets the current time to compare to excluding microseconds
    current = datetime.datetime.now().replace(microsecond=0)
    
    #Splits the date and time apart and then further seperates to match the python datetime function
    d1, t1 = time.split(' ')[0], time.split(' ')[1]
    d2 = d1.split('-')
    t2 = t1.split(':')
    
    #Compiles all the splits to match the correct datetime format (e.x. datetime.datetime(year, month, day, hour, minute, second)
    full = datetime.datetime(int(d2[0]), int(d2[1]), int(d2[2]), int(t2[0]), int(t2[1]), int(t2[2]))
    
    #returns the difference in seconds
    difference = (current-full).seconds
    return difference

#calculates the amount that a customer owes for their parking space, the inserted value is alwasys a car's entry time
#The price will change to $20 if the calculated amount is more than $20 like a regular parking lot
def calculate_amount(time):
    
    #sends the entry time to the compare_time function to calculate the seconds a car has been parked
    spent_time = compare_time(time)
    
    #applies the second based rate
    amount = round(spent_time*(0.05*(1/60)),2)
    if amount >= 20:
        amount = 20
    return amount

def update_amount():
    cursor.execute("""SELECT * from CarDosier""")
    records = cursor.fetchall()
    for row in records:
        update_sum = calculate_amount(row['EntryTime'])
        ID = row['PlateNumber']
        cursor.execute('''UPDATE CarDosier Set Amount = ? Where PlateNumber = ?''', (update_sum, ID));
        dbconnect.commit();
        print(update_sum)
    
if __name__ == '__main__':
    update_amount()