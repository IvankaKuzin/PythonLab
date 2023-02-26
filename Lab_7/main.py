from SearchValue import search_value
from SearchRange import search_range
from SearchLetter import search_first_letter
from SearchWord import search_word
k=input("Введіть елемент по якому буде здійснюватись пошук (значення, діапазон, перша літера, підрядок): ")
if k=='значення':
    v1=input('Введіть поле для пошуку значення: ')
    v2=input('Введіть значення поля для пошуку: ')
    search_value(v1, v2)
elif k=='діапазон':
    v1=input('Введіть поле для пошуку діапазону: ')
    v2=float(input('Введіть мінімальне значення: '))
    v3=float(input('Введіть максимальне значення: '))
    search_range(v1,v2,v3)
elif k=='перша літера':
    v1=input('Введіть поле для пошуку по першій літері: ')
    v2=input('Введіть літеру: ')
    search_first_letter(v1,v1)
elif k=='підрядок':
    v1=input('Введіть поле для пошуку підрядка: ')
    v2=input('Введіть рядок: ')
    search_word(v1,v2)
else:
    print("Пошук за даним елементом не виконується!")
