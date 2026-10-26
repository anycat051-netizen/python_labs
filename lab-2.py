import csv
import random

#задание 1
long_titles = 0
with open('books.csv', encoding='cp1251') as f:
    reader = csv.DictReader(f, delimiter=";")
    books = list(reader)
    for row in books:
        if len(row['Название']) > 30:
            long_titles += 1
print('Записей с названием длиннее 30 символов: ',long_titles)

#задание 2
def search_by_author(author):
    found_books = []
    for book in books:
        if author == book['Автор'] and get_year(book) >= 2018:
            found_books.append(book)
    return found_books
def get_year(book):
    date_with_time = book['Дата поступления']
    date = date_with_time.split(' ')[0]
    year = date.split('.')[2]
    return int(year)

author = input('Введите имя автора: ')
found = search_by_author(author)
if len(found) == 0:
    print('Ничего не найдено :(')
else:
    for book in found:
        print(book['Автор'] + ': ' + book['Название'] + ' - ' + str(get_year(book)))

#задание 3
def bibliography(books, n):
    filtered_books = [x for x in books if x.get('Автор', '').strip()]

    chosen_book = random.sample(filtered_books,n)
    for book in chosen_book:
        yield book['Автор'] + ': ' + book['Название'] + ' - ' + str(get_year(book))

with open('bibliography.txt', 'w', encoding='utf-8') as out:
    books20 =bibliography(books, 20)
    number = 1
    for line in books20:
        out.write(str(number) + '. ' + line + '\n')
        number += 1

#допзадание 1
tags = set()
for book in books:
    genres = book.get('Жанр книги', '')
    for t in genres.split('#'):
        tags.add(t)
for tag in sorted(tags):
    print(tag)

#допзадание 2
issued = {}
for book in books:
    title = book['Название']
    count_str = book['Кол-во выдач']
    count = int(count_str)
    if title in issued:
        issued[title] += count
    else:
        issued[title] = count
top = sorted(issued.items(), key=lambda x: x[1], reverse=True)
print('20 самых популярных книг:')
for i in range(20):
    print(i+1, '. ', top[i][0], ' - ', top[i][1])

#currency.xml
import xml.etree.ElementTree as ET
tree = ET.parse('currency.xml')
root = tree.getroot()
currency = {}
for valute in root.findall('Valute'):
    name = valute.find('Name').text
    char_code = valute.find('CharCode').text
    currency[name] = char_code

print('Курсы валют: ')
for name, char_code in currency.items():
    print(name, '-', char_code)