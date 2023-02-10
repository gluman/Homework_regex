import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
# lastname,firstname,surname,organization,position,phone,email
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
pattern = r"([А-ЯЁа-яё]+) ?([А-ЯЁа-яё]+)? ?([А-ЯЁа-яё]+)?,([А-ЯЁа-яё]+)? ?([А-ЯЁа-яё]+)?,([А-ЯЁа-яё]+)?,([А-ЯЁа-яё]*)?,([А-ЯЁа-яё \–\-\w]*)?,((\+?[\d ?]) ?(\(?\d{1,3}\)?)\-? ?(\d{1,3})\-?(\d{1,2})\-?(\d{1,2})([\(\)А-ЯЁа-яё \.\d]*)?)?,([\w\d\.]+\@[\w]+\.[\w]+)?,?'?\r?"
# ваш код
n_contacts = []
n_cont = {}
for contact_data in contacts_list[1:]:
  for contact in contact_data[0].split(','):
    n_cont['lastname']=

    print(contact)

#

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)