import psycopg2
import parse_items_to_gen
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv
from PyQt5.QtWidgets import QApplication, QWidget

password = '89105071534'

linesClient = {'client_table': 'Id, SERIAL, PRIMARY KEY, Surname, Name, Middle_name, Date_of_birth, INN, FIO_responsible, STATUS'}
linesUser = {'User_Table': 'FIO, Login, Password,'}
class databasegen_core():
	def __init__(self):
		# self.createdatabase()
		# self.create_base_tables()
		self.cursor = self.get_connect()
		self.UserClient = parse_items_to_gen.main()
	def get_connect(self):
		connect = psycopg2.connect(database='postgress_intarface_db',
								   user='postgres',
								   password = password,
								   host='127.0.0.1',
								   port='')
		cursor = connect.cursor()
		return cursor
	def createdatabase(self):
		connect = psycopg2.connect(user='postgres',
								   password=password,
								   host = '127.0.0.1',
								   port='')
		connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		cursor = connect.cursor()
		cursor.execute('''CREATE DATABASE Postgress_intarface_db''')
		cursor.close()
	def create_base_tables(self):
		connect = psycopg2.connect(
			database='postgress_intarface_db',
			user='postgres',
			password=password,
			host='127.0.0.1',
			port='')

		cursor = connect.cursor()
		cursor.execute('''CREATE TABLE client_table
		(
		Id_accounts integer PRIMARY KEY NOT NULL,
		Surname TEXT NOT NULL,
		Name TEXT NOT NULL,
		Middle_name TEXT NOT NULL,
		Date_of_birth DATE NOT NULL,
		INN bigint NOT NULL,
		FIO_responsible text NOT NULL,
		STATUS text NOT NULL
		);
		
		CREATE TABLE User_Table
		(
		FIO text NOT NULL,
		Login text NOT NULL,
		Password integer NOT NULL
		)''')
		connect.commit()
		connect.close()
	def gen_CSV_client(self, client):
		key = ['Id', 'Surname', 'Name', 'Middle_name', 'Date_of_birth',
			   'INN', 'FIO_responsible', 'STATUS']
		with open('CSVs/csv_client.csv', 'w', encoding='utf=8') as csv_file:
			wrt_csv = csv.writer(csv_file)
			wrt_csv.writerow(key)
			for el in client:
				# print(el)
				wrt_csv.writerow([*el])
	def gen_CSV_user(self, user):
		key = ['FIO', 'Login', 'Password']
		with open('CSVs/csv_user.csv', 'w', encoding='utf=8') as csv_file:
			wrt_csv = csv.writer(csv_file)
			wrt_csv.writerow(key)
			for el in user:
				wrt_csv.writerow([*el])
	def CSVGEN_dis(self):
		# self.gen_CSV_user(self.UserClient[0])
		self.gen_CSV_client(self.UserClient[1])
	def CSV_insertDB(self):
		connect = psycopg2.connect(database = 'postgress_intarface_db',
								   user='postgres',
								   password=password,
								   host='127.0.0.1',
								   port='')

		cursor = connect.cursor()
		cursor.execute('''COPY client_table(Id_accounts, Surname, Name, Middle_name, Date_of_birth, INN, FIO_responsible, STATUS)
			   FROM 'C:\Datasets\csv_client.csv'
			   DELIMITER ','
			   CSV HEADER;
			   ''')

		cursor.execute('''COPY user_table(FIO,Login,Password)
		FROM 'C:\Datasets\csv_user.csv'
		DELIMITER ','
		CSV HEADER;''')
		connect.commit()
		connect.close()

def main():
	joing = databasegen_core()

if __name__ == '__main__':
	main()