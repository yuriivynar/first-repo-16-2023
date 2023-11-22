class Tourist:
    def init(self, country: str, duration: int, price: int):
        self.country = country
        self.__duration = duration
        self.__price = price

    def print_all(self):
        self.getName()
        self.getDuration()
        self.getPrice()
        print(self.__str())
        print(self.repr())

    def getName(self):
        print(f'Country: {self.country}')

    def getDuration(self):
        print(f'Trip duration: {self.__duration} days')

    def getPrice(self):
        print(f'Price: {self.__price} €')

    def __str(self):
        return f'To {self.country}, {self.__duration} days, costs {self.__price} €'

    def __repr(self):
        return f'Tourist({self.country!r}, {self.__duration!r}, {self.__price!r})'

    def __del(self):
        print("Called destructor")

def main(inst1, inst2, inst3):
    for x in (inst1, inst2, inst3):
        x.print_all()

t1 = Tourist("England", 10, 1000)
t2 = Tourist("Germany", 5, 690)
t3 = Tourist("Poland", 7, 750)

main(t1, t2, t3)