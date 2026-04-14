import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con= connector.connect(host='localhost', port='3306', user='root', password='root2021', database='pythontest',auth_plugin='mysql_native_password')

    
        query = 'CREATE TABLE IF NOT EXISTS user(userId int primary key, username varchar(200), phone varchar(12))'

        cur= self.con.cursor()
        cur.execute(query)
        print("Table created")

    def insertUser(self, userid, username, phone):
        query = "INSERT INTO user(userId, username, phone) VALUES('{}','{}','{}')".format(userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user inserted!")

    def fetchAll(self):
        query = "SELECT * FROM user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(f"UserId: {row[0]}")
            print(f"UserName: {row[1]}")
            print(f"UserPhone: {row[2]}")
            print()
        print("user fetched!")

    def fetchOne(self):
        userid = input("enter user id to fetch ")
        query = "SELECT * FROM user WHERE userId={}".format(userid)
        print()
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(f"UserId: {row[0]}")
            print(f"UserName: {row[1]}")
            print(f"UserPhone: {row[2]}")
            print()
        print("user fetched!")

    
    def deleteUser(self):
        userid = input("enter user id to delete ")
        query = "DELETE FROM user WHERE userId={}".format(userid)
        print()
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user {} deleted".format(userid))
        print()
        self.fetchAll()





helper = DBHelper()
# helper.insertUser(1481, 'Ram', '4577518')

helper.fetchAll()
# helper.fetchOne()
# helper.deleteUser()

