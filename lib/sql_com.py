import sys

import mysql.connector
import MySQLdb
from mysql.connector import Error

from models.text import Message


class SQL:
    def __init__(self, host, user, pwd, database=None):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.cursor = None
        self.conn = None
        self.database = None

        if database is not None:
            self.database = database

    def connect(self, log):
        try:
            if self.database is not None:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    passwd=self.pwd,
                    database=self.database,
                    port=3307,
                    auth_plugin="mysql_native_password",
                    charset="utf8",
                )
            else:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    passwd=self.pwd,
                    port=3307,
                    auth_plugin="mysql_native_password",
                    charset="utf8",
                )

            self.cursor = self.conn.cursor(prepared=True)

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(log, e)

    def disconnect(self, log):
        try:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()

        except Error as e:
            Message.mysql_error(log, e)

    def create_db(self, log, db_name):
        try:
            if self.database is None:
                self.connect(log)
                self.database = db_name

            self.cursor.execute("CREATE DATABASE " + db_name)

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(log, e)

    def create_table(self, log, table_name, **args):
        try:
            self.connect(log)
            self.cursor.execute("CREATE DATABASE " + table_name)

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(log, e)

    def insert(self, log, table_name, **args):
        id_inserted = 0
        try:
            self.connect(log)

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

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(log, e)

        except Exception as e:
            Message.mysql_error(log, e)

        finally:
            self.disconnect(log)

        return id_inserted

    def select(self, log, table_name):
        rows = None

        try:
            self.connect(log)
            self.cursor.execute("SELECT * FROM " + table_name)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(log, e)

        finally:
            self.disconnect(log)

        return [tuple(self.to_unicode(col) for col in row) for row in rows]

    def select_one_attribute_where(self, log, table_name, attribute, condition):
        rows = None

        try:
            self.connect(log)
            query = f"SELECT {attribute} FROM {table_name} WHERE {condition[0]} = %s"
            query_condition = (condition[1],)
            self.cursor.execute(query, query_condition)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(log, e)

        finally:
            self.disconnect(log)

        return rows

    def select_where(self, log, table_name, condition):
        rows = None

        try:
            self.connect(log)
            query = f"SELECT * FROM {table_name} WHERE {condition[0]} = %s"
            query_condition = (condition[1],)
            self.cursor.execute(query, query_condition)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(log, e)

        finally:
            self.disconnect(log)

        return rows

    def execute_query(self, log, query, values):
        try:
            self.connect(log)
            self.cursor.execute(query, values)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(log, e)

        finally:
            self.disconnect(log)

        return rows

    def to_unicode(self, col):
        if isinstance(col, bytearray):
            return col.decode("utf-8")
        return col
