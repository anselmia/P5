import sys

import mysql.connector
import MySQLdb
from mysql.connector import Error

import settings as CST
from models.text import Message


class SQL:
    def __init__(self, log):
        self.cursor = None
        self.conn = None
        self.log = log

        if not self.database_exist():
            sql_commands = self.replace_database_name_in_script(
                self.read_sql_scrypt("create_database.sql")
            )
            self.execute_sql_scrypts(sql_commands)

    def connect_to_database(self):
        try:
            self.conn = mysql.connector.connect(
                host=CST.DATABASE_HOST,
                user=CST.DATABASE_USER,
                passwd=CST.DATABASE_PWD,
                database=CST.DATABASE_NAME,
                port=CST.DATABASE_ACCESS_PORT,
                auth_plugin="mysql_native_password",
                charset="utf8",
            )

            self.cursor = self.conn.cursor(prepared=True)

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(self.log, e)

    def connect_to_server(self):
        try:
            self.conn = mysql.connector.connect(
                host=CST.DATABASE_HOST,
                user=CST.DATABASE_USER,
                passwd=CST.DATABASE_PWD,
                port=CST.DATABASE_ACCESS_PORT,
                auth_plugin="mysql_native_password",
            )

            self.cursor = self.conn.cursor(prepared=True)

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(self.log, e)

    def disconnect(self):
        try:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()

        except Error as e:
            Message.mysql_error(self.log, e)

    def insert(self, table_name, **args):
        id_inserted = 0
        try:
            self.connect_to_database()

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
            Message.mysql_error(self.log, e)

        except Exception as e:
            Message.mysql_error(self.log, e)

        finally:
            self.disconnect()

        return id_inserted

    def select(self, table_name):
        rows = None

        try:
            self.connect_to_database()
            self.cursor.execute("SELECT * FROM " + table_name)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(self.log, e)

        finally:
            self.disconnect()

        return [tuple(self.to_unicode(col) for col in row) for row in rows]

    def select_one_attribute_where(self, table_name, attribute, condition):
        rows = None

        try:
            self.connect_to_database()
            query = f"SELECT {attribute} FROM {table_name} WHERE {condition[0]} = %s"
            query_condition = (condition[1],)
            self.cursor.execute(query, query_condition)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(self.log, e)

        finally:
            self.disconnect()

        return rows

    def select_where(self, table_name, condition, operator="="):
        rows = None

        try:
            self.connect_to_database()
            query = f"SELECT * FROM {table_name} WHERE {condition[0]} {operator} %s"
            query_condition = (condition[1],)
            self.cursor.execute(query, query_condition)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(self.log, e)

        finally:
            self.disconnect()

        return rows

    def execute_query(self, query, values=None):
        try:
            self.connect_to_database()
            if values is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, values)
            datas = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(self.log, e)

        finally:
            self.disconnect()

        return datas

    def to_unicode(self, col):
        if isinstance(col, bytearray):
            return col.decode("utf-8")
        return col

    def read_sql_scrypt(self, sql_file_path):
        # Open and read the file as a single buffer
        with open(sql_file_path, "r", encoding="utf-8") as f:
            data = f.read().splitlines()
        stmt = ""
        sql_commands = []
        for line in data:
            if line:
                if line.startswith("--"):
                    continue
                stmt += line.strip() + " "
                if ";" in stmt:
                    sql_commands.append(stmt.strip())
                    stmt = ""

        return sql_commands

    def execute_sql_scrypts(self, sql_commands):
        self.connect_to_server()
        # Execute every command from the input file
        for num, command in enumerate(sql_commands):
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                self.cursor.execute(command)
            except Error as e:
                Message.mysql_file_execute_command_skipped(self.log, str(e), num)

        self.disconnect()

    def database_exist(self):
        command = f'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = "{CST.DATABASE_NAME}"'
        datas = []
        try:
            self.connect_to_server()
            self.cursor.execute(command)
            datas = self.cursor.fetchall()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            Message.mysql_error(self.log, e)
        finally:
            self.disconnect()

        return len(datas) > 0

    def replace_database_name_in_script(self, sql_commands):
        sql_commands = [
            command.replace("databaseName", CST.DATABASE_NAME) for command in sql_commands
        ]

        return sql_commands
