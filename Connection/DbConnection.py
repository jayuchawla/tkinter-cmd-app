import mysql.connector as mc

class DbConnection:

    def __init__(self):
        try:
            self.mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "root",
                database = "application",
                #auth_plugin='mysql_native_password'
            )

            self.cursor = self.mydb.cursor()
            print("Database connected!!")
        except mc.Error as e:
            print(e.msg)
            print("Database instantiation failed!!")

    def getCursor(self):
        return self.cursor

    def commit(self):
        self.mydb.commit()
        