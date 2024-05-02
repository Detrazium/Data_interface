from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import numpy as np
import random
import csv
import time

login_users = ['reneheg-avu90@mail.com',
			   'xixixuk-apo95@yahoo.com',
			   'xeci_fihaga20@gmail.com',
			   'baxoyi-digu85@hotmail.com',
			   'puci-jubeda40@hotmail.com',
			   'zakaj-amewe30@mail.com',
			   'kimone_yuda13@mail.com',
			   'zuyico_zedo94@hotmail.com',
			   'zole_boveji3@outlook.com',
			   'fasecax-onu18@hotmail.com']


users = {0: 'Гаврилов Фёдор Артёмович',
		 1: 'Васильева Ульяна Дмитриевна',
		 2: 'Федоров Артём Львович',
		 3: 'Куликова Ксения Павловна',
		 4: 'Соловьев Никита Максимович',
		 5: 'Родионова Мария Даниловна',
		 6: 'Абрамова Яна Алиевна',
		 7: 'Родионов Захар Сергеевич',
		 8: "Горюнова Лидия Михайловна",
		 9: 'Литвинова Полина Николаевна', }
status = '«Не в работе»'
class parse():
	def parse_random_named(self, url):
		def parsed(html):
			soup = BeautifulSoup(html)

			items = soup.find('textarea')
			return items.text
		options = Options()
		options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
		driver = webdriver.Chrome(options=options)
		driver.get(url)
		k = 0
		with open('items_name.txt', 'w', encoding='utf=8') as file:
			for i in range(1000):
				k+=1
				key = driver.find_elements(By.CLASS_NAME, 'is-fullwidth')[0]
				items = parsed(driver.page_source)
				file.write(items)
				print(k, '\n')
				time.sleep(2)
				key.click()

		print()
	def Created_client(self):
		def data_B():
			def years():
				thousands = random.randint(1, 2)

				dozensY = random.randint(0, 1)
				dozens = random.randint(1, 9)

				l = ''
				if thousands > 1:
					l += '20'
					if dozensY > 0: l += '0' + str(dozens)
					else: l += '10'

				else:
					l += '19'
					l += str(random.randint(60, 99))
				return l
			ondate = '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 30))
			data = []
			data.append(years() + ondate)
			return data

		with open('items_name.txt', 'r', encoding='utf=8') as file:
			f1 = file.readlines()
			key = 0
			itemir = len(f1) // 10
			item = []
			for name in f1:
				res = random.randint(0, 9)
				key += 1
				Id = str(key).zfill(8)
				contN = name.replace(',', '').split()
				if len(contN) == 3:
					data_born = data_B()
					INN = random.randint(100000000000,999999999999)
					csv_cont = [Id, *contN, data_born, INN, users[res], status]
					item.append(csv_cont)
		return item

	def Create_user(self):
		item = []
		for i, l in zip(login_users, users):
			fio = users[l]
			log = login_users[l]
			passw = random.randint(10000000, 99999999)
			client_csv = [fio, log, passw]
			item.append(client_csv)
		return item
def main():
	k = parse()
	item_user = k.Create_user()
	item_client = k.Created_client()
	return item_user, item_client



if __name__ == '__main__':
	main()


