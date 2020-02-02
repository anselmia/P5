""" MySQL library to communicate with a MySql Server """

import sys

import mysql.connector
import MySQLdb
from mysql.connector import Error

import settings as CST


class SQL:
    """ Class to communicate with a MySql Server """

    def __init__(self, message):
        """ Initialization method """
        self.cursor = None
        self.conn = None
        self.message = message

        # Verify if DataBase exist on the server
        # Read and Run Mysql scrypt to create the database if it doesn't exist
        if not self.database_exist():
            sql_commands = self.replace_database_name_in_script(
                self.read_sql_scrypt("create_database.sql")
            )
            self.execute_sql_scrypts(sql_commands)

    def connect_to_database(self):
        """ Initializase the connector to connect to the database """
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
            self.message.mysql_error(e)

    def connect_to_server(self):
        """ Initializase the connector to connect to the server """
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
            self.message.mysql_error(e)

    def disconnect(self):
        """ Close the connexion to the database """
        try:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()

        except Error as e:
            self.message.mysql_error(e)

    def insert(self, table_name, **args):
        """
            Create and run a SQL Insert request.
            Arg : table_name
                  **args : a dict of columns : Values of data to be inserted
        """
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
            self.message.mysql_error(e)

        except Exception as e:
            self.message.mysql_error(e)

        finally:
            self.disconnect()

        return id_inserted

    def select(self, table_name):
        """
            Create and run a SQL Select request.
            Arg : table_name
        """
        rows = None

        try:
            self.connect_to_database()
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            self.message.mysql_error(e)

        finally:
            self.disconnect()

        return [tuple(self.to_unicode(col) for col in row) for row in rows]

    def select_one_attribute_where(self, table_name, attribute, condition):
        """
            Create and run a SQL Select attribute request whith a where clause.
            Arg : name of the table
                  attribute to retrieve
                  condition as a Tuple of column and value
            return the matching rows
        """
        rows = None

        try:
            self.connect_to_database()
            query = f"SELECT {attribute} FROM {table_name} WHERE {condition[0]} = %s"
            values = (condition[1],)
            self.cursor.execute(query, values)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            self.message.mysql_error(e)

        finally:
            self.disconnect()

        return rows

    def select_first_row_one_attribute_where(self, table_name, attribute, condition):
        """
            Create and run a SQL Select attribute request whith a where clause.
            Arg : name of the table
                  attribute to retrieve
                  condition as a Tuple of column and value

            return only the first found row
        """
        rows = None

        try:
            self.connect_to_database()
            query = f"SELECT {attribute} FROM {table_name} WHERE {condition[0]} = %s LIMIT 1"
            values = (condition[1],)
            self.cursor.execute(query, values)
            row = self.cursor.fetchone()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            self.message.mysql_error(e)

        finally:
            self.disconnect()

        return row

    def select_where(self, table_name, condition, operator="="):
        """
            Create and run a SQL Select request whith a where clause using
            a specified operator.
            Arg : name of the table
                  condition as a Tuple of column and value
                  operator of condition
        """
        rows = None

        try:
            self.connect_to_database()
            query = f"SELECT * FROM {table_name} WHERE {condition[0]} {operator} %s"
            query_condition = (condition[1],)
            self.cursor.execute(query, query_condition)
            rows = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            self.message.mysql_error(e)

        finally:
            self.disconnect()

        return rows

    def execute_query(self, query, values=None):
        """
            General method to execute a SQL query
            Query can be done using values or not
        """
        try:
            self.connect_to_database()
            if values is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, values)
            datas = self.cursor.fetchall()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            self.message.mysql_error(e)

        finally:
            self.disconnect()

        return datas

    def to_unicode(self, col):
        """ Method to decode bytearray """
        if isinstance(col, bytearray):
            return col.decode("utf-8")
        return col

    def read_sql_scrypt(self, sql_file_path):
        """
            Method to open and read a sql files at the specified path.
            It will return only the sql command with a ";" at the end
        """
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
        """
            Execute all the scrypt from a list
            arg : list of sql commands
        """
        self.connect_to_server()
        # Execute every command from the input file
        for num, command in enumerate(sql_commands):
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                self.cursor.execute(command)
            except Error as e:
                self.message.mysql_file_execute_command_skipped(str(e), num)

        self.disconnect()

    def database_exist(self):
        """ Methode to verify if the database exist on the server """
        command = f'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = "{CST.DATABASE_NAME}"'
        datas = []
        try:
            self.connect_to_server()
            self.cursor.execute(command)
            datas = self.cursor.fetchall()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            self.message.mysql_error(e)
        finally:
            self.disconnect()

        return len(datas) > 0

    def replace_database_name_in_script(self, sql_commands):
        """ Methode to replace the database name in the sql scrypt """
        sql_commands = [
            command.replace("databaseName", CST.DATABASE_NAME) for command in sql_commands
        ]

        return sql_commands
