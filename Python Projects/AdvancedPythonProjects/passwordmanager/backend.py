import sqlite3 

class PasswordMangerBC:
    def __init__(self):
        connection = sqlite3.connect("passwordmanagerdb.db")
        cursor = connection.cursor()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Passwords(
                       Id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Website Text,
                       Email Text,
                       Password Text
                        )
                       """)
        connection.commit()
        connection.close()
        print("Password Database Created")

    def save_data(sale, website, email, password):
        connection = sqlite3.connect("passwordmanagerdb.db")
        cursor = connection.cursor()
        cursor.execute("""
                INSERT INTO Passwords(Website, Email, Password)
                       values(?,?,?)
                       """,(website, email, password))
        

        connection.commit()
        connection.close()
        print("Values inserted!")



        