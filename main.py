
from postgres_connection import PostgresConnection 

if __name__ == "__main__":
	psconn = PostgresConnection()
	psconn.create_table("test_table", {"name":"varchar(50)"})
	psconn.list_all_tables()
	psconn.list_all_columns_from_table("test_table")
	psconn.list_all_values_from_table("test_table")






