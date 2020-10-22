from Connection.DbConnection import DbConnection
import mysql.connector as mc

class UserDAO:
    def __init__(self):
        self.db = DbConnection()
        self.dbcursor = self.db.getCursor()

    def registerUser(self, username, password):
        try:
            query = "insert into credentials(username, password) values(%s,%s)"
            values = (username, password)
            self.dbcursor.execute(query, values)
            self.db.commit()
        except mc.Error as e:
            print(e.msg)

    def getUsers(self):
        try:
            query = "select * from credentials"
            self.dbcursor.execute(query)
            result = self.dbcursor.fetchall()
            return result
        except mc.Error as e:
            print(e.msg)

    def getUserByUsernameAndPassword(self, username, password):
        try:
            query = "select * from credentials where username=%s and password=%s"
            values = (username, password)
            self.dbcursor.execute(query, values)
            result = self.dbcursor.fetchall()
            if not result:
                return False 
            return True    
        except mc.Error as e:
            print(e.msg)

ud = UserDAO()
#ud.registerUser("jayu", "hello")
print(ud.getUserByUsernameAndPassword("jayu", "hello"))