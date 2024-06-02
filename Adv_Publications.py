from datetime import date



class Publications:
    def __init__(self, name):
        self.name = name

class Shop(Publications):
    def __init__(self, name, fuel):
        Publications.__init__(self, name=name)
        self.fuel = fuel


    def print_price(self, fuel):
        if fuel == 1:
            print("Gas cost 10")
        elif fuel == 2:
            print("Diesel cost 7")




class Advertazing(Publications):
    def __init__(self, name, adv_text):
        Publications.__init__(self, name=name)
        self.adv_text = adv_text

    def print_adv(self):
        print(f'your_adv {self.adv_text}')

class News(Publications):
    def __init__(self, name, city_name):
        Publications.__init__(self, name=name)
        self.city_name = city_name

    def print_news(self):
        today = date.today()
        print(f'In the city {self.city_name} smth happend today {today}')


inp = input("What do you want to do? input 1 if adv input 2 if news input 3 if shop")

if inp == '1':
    adv_text = input("type your adv")
    adv = Advertazing('Ad_name', adv_text)
    adv.print_adv()

elif inp == '2':
    city_name = input("type your city")
    news = News('name', city_name)
    news.print_news()

elif inp == '3':
    fuel = input("Input 1 if you want gas, input 2 if diesel")
    shop = Shop('name', fuel)
    shop.print_price(fuel)


