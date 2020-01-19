import mysql.connector
import sys
from mysql.connector import Error
import MySQLdb
 

class SQL():

    def __init__(self, host, user, pwd, database=None):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.cursor = None
        self.conn = None
        self.database = None

        if(database != None):
            self.database = database

    def connect(self):
        try:
            if(self.database != None):
                self.conn = mysql.connector.connect(host=self.host,                                                
                                                    user=self.user, 
                                                    passwd=self.pwd,
                                                    database=self.database,
                                                    port=3307,
                                                    auth_plugin='mysql_native_password',
                                                    charset = 'utf8')
            else:
                self.conn = mysql.connector.connect(host=self.host,                                                
                                                    user=self.user, 
                                                    passwd=self.pwd,
                                                    port=3307,
                                                    auth_plugin='mysql_native_password',
                                                    charset = 'utf8')

            self.cursor = self.conn.cursor(prepared=True)

        except Error as e:
            print("Error while connecting to MySQL", e)

    def disconnect(self):
        try:
            if (self.conn.is_connected()):
                self.cursor.close()
                self.conn.close()

        except Error as e:
            print("Error while disconnecting to MySQL", e)

    def create_db(self, db_name):
        try:
            if(self.database == None):
                self.connect()
                self.database = db_name

            self.cursor.execute("CREATE DATABASE " + db_name)

        except Error as e:
            print("Error while creating database", e)

    def create_table(self, table_name,**args):
        try:
            self.connect()
            self.cursor.execute("CREATE DATABASE " + db_name)

        except Error as e:
            log.appendText("Error while creating database " + table_name + str(e), (255,30,30))

    def insert(self, log, table_name, **args):
        try:
            self.connect()

            columns = args.keys()
            values = tuple(args.values())

            query = "INSERT IGNORE INTO " + table_name + " ("

            for column in columns:
                query += column + ","
            query = query[:-1]
            query += ")"
            query += " VALUES " + "("
            for value in values:
                query += "%s,"
            query = query[:-1]
            
            query += ")"

            self.cursor.execute(query.encode(sys.stdout.encoding), values)
            self.conn.commit()
            id_inserted = self.cursor.lastrowid

        except Error as e:
            log.appendText("Error while inserting data in table " + table_name + str(e), (255,30,30)) 
   
        finally:
            self.disconnect()
    
        return id_inserted
    
    def select(self, log, table_name):
        rows = None

        try:
            self.connect()
            self.cursor.execute("SELECT * FROM " + table_name)
            rows = self.cursor.fetchall()

        except Error as e:
            log.appendText("Error while retrieving database rows from table " + table_name + str(e), (255,30,30))

        finally:
            self.disconnect()

        return rows

    def select_one_attribute_where(self, log, table_name, attribute, condition):
        rows = None

        try:
            self.connect()
            query = f"SELECT {attribute} FROM {table_name} WHERE {condition[0]} = %s"
            query_condition = (condition[1],)
            self.cursor.execute(query, query_condition)
            rows = self.cursor.fetchall()

        except Error as e:
            log.appendText("Error while retrieving database rows from table " + table_name + str(e), (255,30,30))

        finally:
            self.disconnect()

        return rows

    def select_where(self, log, table_name, condition):
        rows = None

        try:
            self.connect()
            query = f"SELECT * FROM {table_name} WHERE {condition[0]} = %s"
            query_condition = (condition[1],)
            self.cursor.execute(query, query_condition)
            rows = self.cursor.fetchall()

        except Error as e:
            log.appendText("Error while retrieving database rows from table " + table_name + str(e), (255,30,30))

        finally:
            self.disconnect()

        return rows
    
    def execute_query(self, log, query, values):
        try:
            self.connect()
            self.cursor.execute(query, values)
            rows = self.cursor.fetchall()

        except Error as e:
            log.appendText("Error while executing query " + query + str(e), (255,30,30))

        finally:
            self.disconnect()

        return rows
