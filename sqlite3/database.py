import sqlite3
# import datetime

# Connect to the database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# # Create a table
c.execute("""CREATE TABLE IF NOT EXISTS customers (
              first_name text,
              last_name text,
              email_address text
          )""")


# Inserting the single data into the table
# c.execute("INSERT INTO customers VALUES (  'Umesh', 'Yadav', 'umeshyadav@gmail.com')")

# Inserting the many data into the table

# manyData = [
#     ('Isha', 'Pulkit', 'ishapulkit@gmail.com'),
#     ('Harsh', 'Om', 'harshom@gmail.com'),
#     ('Prakash', 'Rao', 'prakashrao@gmail.com'),
#     ('Watson', 'Dan', 'watsondan@gmail.com')
# ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", manyData)

# print("Data is inserted successfully...")


# Fetch the all data from the table

# This is by for loop
# detail = c.execute(
#     "SELECT first_name, last_name, email_address FROM customers")

# for row in detail:
#     print("First Name = ", row[0])
#     print("Last Name = ", row[1])
#     print("Email Address", row[2], "\n")

# This is by fetchall() prebuild function
details = c.execute("SELECT * FROM customers")
# print(details.fetchone())  # This will only fetch the value at 1st
# print(details.fetchmany(2))  # This command will print the data upto 2 values

items = details.fetchall()  # This will fetch all the data present into the table
for item in items:
    print(
        f"First name: {item[0]}\nLast name: {item[1]}\nEmail address: {item[2]}\n ")

# Commit our command
conn.commit()

# Close our connection
conn.close()


# NULL - It does exists or not
# INTEGER - It has whole numbers
# REAL - It has decimal numbers
# TEXT - This are strings and char.
# BLOB - Images, MP3, MP4 etc.
