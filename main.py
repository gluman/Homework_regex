import re
# читаем адресную книгу в формате CSV в список contacts_list
# lastname,firstname,surname,organization,position,phone,email
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
pattern = r"([А-ЯЁа-яё]+) ?([А-ЯЁа-яё]+)? ?([А-ЯЁа-яё]+)?,([А-ЯЁа-яё]+)? ?([А-ЯЁа-яё]+)?,([А-ЯЁа-яё]+)?," \
          r"([А-ЯЁа-яё]*)?,([А-ЯЁа-яё \–\-\w]*)?,((\+?[\d ?]) ?\(?(\d{1,3})\)?\-? ?(\d{1,3})\-?(\d{1,2})\-?(\d{1," \
          r"2})([\(\)А-ЯЁа-яё \.\d]*)?)?,([\w\d\.]+\@[\w]+\.[\w]+)?,?"
n_contacts = []

n_contacts.append(contacts_list[0])
for contact_data in contacts_list[1:]:
    for contact in contact_data:
        subb = r"\1,\2\4,\3\5\6,\7,\8,+7(\11)\12-\13-\14\15,\16"
        n_data = re.sub(pattern, subb, contact)
        n_cont = n_data.split(',')
        add = True
        if len(n_contacts) > 1:
            for i in n_contacts[::-1]:
                if i[0] == n_cont[0] and i[1] == n_cont[1]:
                    if len(i[3]) <= 1:
                        i[3] = n_cont[3]
                    if len(i[4]) <= 1:
                        i[4] = n_cont[4]
                    if len(i[5]) <= 6:
                        i[5] = n_cont[5]
                    if len(i[6]) <= 1:
                        i[6] = n_cont[6]
                    add = False
        if add:
            n_contacts.append(n_cont)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(n_contacts)
