import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class PostgresConnection:
	"""
	Connect python with postgres.

	This class can 
	create table in database,
	list tables in database,
	list all columns from a table,
	list all values from a table
	"""
	def __init__(self):
		self.t_host = "postgres"
		self.t_port = os.getenv("POSTGRES_PORT")
		self.t_dbname = os.getenv("POSTGRES_DB")
		self.t_user = os.getenv("POSTGRES_USER")
		self.t_password = os.getenv("POSTGRES_PASSWORD")
		self.db_conn = psycopg2.connect(host=self.t_host, port=self.t_port, dbname=self.t_dbname, user=self.t_user, password=self.t_password)
		self.db_conn.autocommit = True
		self.db_cursor = self.db_conn.cursor()
	
	def list_all_tables(self):

		"""
			Method to list all tables
		"""
		self.db_cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
		print(self.db_cursor.fetchall())

	def create_table(self, table_name:str, colums:dict) -> None:
		"""
			Method to list create a table
		"""
		s = f"""CREATE TABLE IF NOT EXISTS {table_name}"""
		s+="("
		for column_name in list(colums.keys()):
			s+= f"{column_name} {colums[column_name]},"
		s = s[:-1]
		s+= ")"
		self.db_cursor.execute(s)

	def list_all_columns_from_table(self, table_name):
		"""
			Method to list all columns from a table
		"""
		s = f"""SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}';"""
		self.db_cursor.execute(s)
		print(self.db_cursor.fetchall())


	def list_all_values_from_table(self, table_name):
		"""
			Method to list all values from a table
		"""
		s = f"""SELECT * FROM {table_name};"""
		self.db_cursor.execute(s)
		print(self.db_cursor.fetchall())