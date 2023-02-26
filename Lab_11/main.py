class Movie:
    def __init__(self,name,director,lenght,number_actor):
        self.name=name
        self.director=director
        self.lenght=lenght
        self.number_actor=number_actor

    def Price(self):
        price=self.lenght*20+self.number_actor*30
        if self.director=='Стівен Спілберг' or self.director=='Джеймс Кемерон':
            price=price*2
        print("Вартість фільму",price,"$")

    def __str__(self):
        return f"Назва:{self.name}, Режисер:{self.director}," \
               f" Тривалість:{self.lenght}, Кількість акторів:{self.number_actor}"

class Cartoon(Movie):
    pass
    def Price(self):
        price=self.lenght*25+self.number_actor*10
        print("Вартість мультфільму", price, "$")

m1=Movie('Звільнення','Антуан Фукуа',132,32)
m2=Movie('Титанік','Джеймс Кемерон',194,11)
m3=Cartoon('Tom and Jerry','Тім Сторі',101,2)
print(m1,m1.Price(),'\n')
print(m2,m2.Price(),'\n')
print(m3,m3.Price(),'\n')
