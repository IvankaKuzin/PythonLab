from Sort import sort1,sort2
from Filter import filter_val,filter_diap,filter_letter,filter_word
from Group import group
from ReadDataSet import read
from NewDataSet import new_dataset,mydataset_merge

var=input('Вкажіть функцію обробки даних (читання,фільтрування,сортування,групування): ')
if var=='читання':
    read()
if var=='фільтрування':
    count = input('Виконати фільтрування за значенням, діапазоном, першою буквою чи підрядком? ')
    if count=='значенням':
        colum=input('Введіть назву стовпця: ')
        var=int(input('Введіть значення: '))
        filter_val(colum,var)
    if count=='діапазоном':
        colum = input('Введіть назву стовпця: ')
        var1 = int(input('Введіть мінімальне значення: '))
        var2 = int(input('Введіть максимальне значення: '))
        filter_diap(colum,var1,var2)
    if count=='першою буквою':
        colum = input('Введіть назву стовпця: ')
        var = input('Введіть першу букву: ')
        filter_letter(colum,var)
    if count=='підрядком':
        colum = input('Введіть назву стовпця: ')
        var = input('Введіть підрядок: ')
        filter_word(colum,var)
if var=='сортування':
    count=int(input('Виконати сортування за одним чи двома стовпцями? '))
    if count==1:
        col=input('Введіть назву стовпця: ')
        reg=int(input('Виберіть режим сортування (0-спадання, 1-зростання): '))
        sort1(col,reg)
    if count==2:
        col1=input('Введіть назву першого стовпця: ')
        col2 = input('Введіть назву другого стовпця: ')
        reg=int(input('Виберіть режим сортування (0-спадання, 1-зростання): '))
        sort2(col1,col2,reg)
if var=='групування':
    col=input('Введіть назву стовпця: ')
    reg=input('Введіть значення, яке хочете отримати із групованого стовпця \n (мінімальне, максимальне середнє чи відхилення): ')
    group(col,reg)
    abc=input('Потрібно утворити новий файл з групою? ')
    if abc=='так':
        a1=input('Чи потрібно додати нові дані до вхідних? ')
        if a1=='так':
            new_dataset()
            mydataset_merge()

































