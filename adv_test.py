

class Publ:
    def __init__(self, name):
        self.name = name

    def publ_date(self):
        print('Today')

class Adv(Publ):
    def __init__(self, name, customer):
        Publ.__init__(self, name=name)
        self.customer = customer
    def custom_name(self):
        print(f"Cust is {self.customer}")


my_adv = Adv("ZZZ", "Goo")

my_adv.custom_name()
my_adv.publ_date()

