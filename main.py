class Car():

    """This is a simple car model"""

    def __init__(self, model, make, year, engine_volume, color_car, price_car):
        self.__make = make  # марка производителя
        self.__model = model  # модель
        self.year = year  # год випуска
        self.__engine_volume = engine_volume  # объем двигателя
        self.color_car = color_car  # цвет
        self.price_car = price_car  # цена

    def get_display_info(self):
        """
        Method of exiting car information
        :return:
        """
        print(self.__str__())

    def get_display_doc(self):
        """
        Documentation output method
        :return: documentation
        """
        return self.__doc__

    def get_display_dict(self):
        """
        Method returning dictionary.
        Internal dictionary of class attributes
        :return: dict
        """
        return self.__dict__

    def __add__(self, other):
        return f"Total amount of the cars: -- > {self.price_car + other.price_car}$"

    def __sub__(self, other):
        return f"The difference in the price of cars: --> {abs(self.price_car - other.price_car)}$"

    def __lt__(self, other):
        if self.price_car < other.price_car:
            print(f"The price --> {self.price_car}$ of the first car "
                  f"is less than the second --> {other.price_car} $ price car")

        if self.__engine_volume < other.__engine_volume:
            print(f"The engine size --> {self.__engine_volume}(L) of the first car "
                  f"is less than the engine size --> {other.__engine_volume}(L) of the second car")

        if self.year < other.year:
            print(f"The first car --> (release: {self.year}) "
                  f"came out earlier than the second car --> (release: {other.year})")

    def __eq__(self, other):
        if self.price_car == other.price_car:
            print(f"These two cars with the same price yeah --> {self.price_car}$ = {other.price_car}$")

        if self.__engine_volume == other.__engine_volume:
            print(f"The engine size --> {self.__engine_volume}(L) of the first car "
                  f"is equal to the engine size --> {other.__engine_volume}(L) of the second car")

        if self.year == other.year:
            print(f"The first car --> (release: {self.year}) c was released in the same year "
                  f"as the second car --> (release: {other.year})")

        if self.__model == other.__model:
            print('This cars with the same model range')

        if self.__make == other.__make:
            print('The machine manufacturer is the same')

        if self.color_car == other.color_car:
            print('Cars have the same color')

    def __gt__(self, other):
        if self.price_car > other.price_car:
            print(f"The price of first --> {self.price_car}$ car is more than the price "
                  f"of second --> {other.price_car}$ cars the price")

        if self.__engine_volume > other.__engine_volume:
            print(f"The engine volume --> {self.__engine_volume}(L) of the first car "
                  f"is greater than the engine volume --> {other.__engine_volume}(L) of the second car")

        if self.year > other.year:
            print(f"The first car --> (release: {self.year}) was made later "
                  f"than the second car --> (release: {other.year})")

    def __str__(self):
        """
        :return: car info
        """
        return f"Car info\n" \
               f"Make: {self.__make}\n" \
               f"Model: {self.__model}\n" \
               f"Year: {self.year}\n" \
               f"Color car: {self.color_car}\n" \
               f"Engine volume: {self.__engine_volume}\n" \
               f"Price car: {self.price_car}\n"

    @property
    def make(self):
        return self.__make

    @make.getter
    def make(self):
        return f"Manufacturer brand: {self.__make}"

    @make.setter
    def make(self, value):
        self.__make = value

    @property
    def model(self):
        return self.__model

    @model.getter
    def model(self):
        return f"Model car: {self.__model}"

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def engine_volume(self):
        return self.__engine_volume

    @engine_volume.getter
    def engine_volume(self):
        return f"Engine volume car: {self.__engine_volume} Liters"

    @engine_volume.setter
    def engine_volume(self, value):
        self.__engine_volume = value

    def get_yaer(self):
        return f"Year of car production: {self.year}"

    def set_yaer(self, value):
        self.year = value

    def get_price(self):
        return f"You can buy this {self.__make} {self.__model} for {self.price_car} $"

    def set_price(self, value):
        self.price_car = value

    def get_color(self):
        return f"The color {self.__make} {self.__model}: {self.color_car}"

    def set_color(self, value):
        self.color_car = value

    def get_make(self):
        return f"Method that returns the brand of the car --> {self.__make}"

    def get_model_car(self):
        return f"Method that returns the model of the car --> {self.__model}"

    def get_engine_volume_car(self):
        return f"Method that returns the volume of the engine --> {self.__engine_volume}"


car = Car(model='Raptor', make='Ford', year=2021, engine_volume=5.3, color_car='Red', price_car=45_000)
car2 = Car(model='Mustang Shelby GT500', make='Ford', year=1971, engine_volume=7, color_car='Silver', price_car=43_000)
car3 = Car(model='X5', make='BMV', year=2018, engine_volume=4.2, color_car='Silver', price_car=32_000)


print(car == car2)
# print(car - ca2)
# print(car.get_price())


