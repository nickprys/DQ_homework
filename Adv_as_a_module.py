
# Import date from datetime module
from datetime import date


# Define 'Publication' class with a name
class Publications:
    def __init__(self, name):
        self.name = name


# Create a subclass of 'Publication' called 'Shop'
class Shop(Publications):
    # Extend Publication's init method to include 'fuel'
    def __init__(self, name, fuel):
        # Call the parent class's init method
        super().__init__(name=name)
        # Add new attribute 'fuel'
        self.fuel = fuel

    # Method for printing price based on 'fuel' attribute
    def print_price(self):
        # Determine price based on fuel type and print it
        # Also appends result to 'newsfeed.txt'
        if self.fuel == 1:
            output = "Gas cost 10"
        elif self.fuel == 2:
            output = "Diesel cost 7"

        print(output)
        # Append result to file
        with open('newsfeed.txt', 'a') as f:
            f.write(output + '\n')


# 'Advertazing' subclass of 'Publications'
class Advertazing(Publications):
    # As before, extends init method to include 'adv_text' attribute
    def __init__(self, name, adv_text):
        super().__init__(name=name)
        self.adv_text = adv_text

    # Method to print ad message and append it to 'newsfeed.txt'
    def print_adv(self):
        output = f'your_adv {self.adv_text}'
        print(output)
        with open('newsfeed.txt', 'a') as f:
            f.write(output + '\n')


# 'News' subclass of 'Publications'
class News(Publications):
    # Extensions include 'city_name'
    def __init__(self, name, city_name):
        super().__init__(name=name)
        self.city_name = city_name

    # Print today's news for a city and write it to 'newsfeed.txt'
    def print_news(self):
        today = date.today()
        output = f'In the city {self.city_name} smth happend today {today}'
        print(output)
        with open('newsfeed.txt', 'a') as f:
            f.write(output + '\n')


if __name__ == '__main__':
    # Main logic: acts based on user's choice
    inp = input("What do you want to do? input 1 if adv input 2 if news input 3 if shop")

    # Advertising
    if inp == '1':
        adv_text = input("type your adv")
        adv = Advertazing('Ad_name', adv_text)
        adv.print_adv()

    # News
    elif inp == '2':
        city_name = input("type your city")
        news = News('name', city_name)
        news.print_news()

    # Shop
    elif inp == '3':
        fuel = int(input("Input 1 if you want gas, input 2 if diesel"))
        shop = Shop('name', fuel)
        shop.print_price()

