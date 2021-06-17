import json


class Car:
    """This is a simple car model"""

    def __init__(self, model=None, make=None, year=None, engine_volume=None, color_car=None, price_car=None):
        self.make = make  # марка производителя
        self.model = model  # модель
        self.year = year  # год випуска
        self.engine_volume = engine_volume  # объем двигателя
        self.color_car = color_car  # цвет
        self.price_car = price_car  # цена

    @staticmethod
    def format_data(instance):
        """
        function that performs formatting and serialization of data
        :param instance: instance class Car
        :return: data string
        """
        result = {}
        for key in instance.__dict__:
            result[key] = instance.__dict__[key]
        return json.dumps(result)

    @staticmethod
    def from_dict_to_instance(dictionary, cls):
        """
        function that performs formatting dict --> instance
        :param dictionary: value dict
        :param cls: class Car
        :return: object Car
        """
        obj = cls()
        obj.make = dictionary['make']
        obj.model = dictionary['model']
        obj.year = dictionary['year']
        obj.engine_volume = dictionary['engine_volume']
        obj.color_car = dictionary['color_car']
        obj.price_car = dictionary['price_car']
        return obj

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

        if self.engine_volume < other.engine_volume:
            print(f"The engine size --> {self.engine_volume}(L) of the first car "
                  f"is less than the engine size --> {other.engine_volume}(L) of the second car")

        if self.year < other.year:
            print(f"The first car --> (release: {self.year}) "
                  f"came out earlier than the second car --> (release: {other.year})")

    def __eq__(self, other):
        if self.price_car == other.price_car:
            print(f"These two cars with the same price yeah --> {self.price_car}$ = {other.price_car}$")

        if self.engine_volume == other.engine_volume:
            print(f"The engine size --> {self.engine_volume}(L) of the first car "
                  f"is equal to the engine size --> {other.engine_volume}(L) of the second car")

        if self.year == other.year:
            print(f"The first car --> (release: {self.year}) c was released in the same year "
                  f"as the second car --> (release: {other.year})")

        if self.model == other.model:
            print('This cars with the same model range')

        if self.make == other.make:
            print('The machine manufacturer is the same')

        if self.color_car == other.color_car:
            print('Cars have the same color')

    def __gt__(self, other):
        if self.price_car > other.price_car:
            print(f"The price of first --> {self.price_car}$ car is more than the price "
                  f"of second --> {other.price_car}$ cars the price")

        if self.engine_volume > other.engine_volume:
            print(f"The engine volume --> {self.engine_volume}(L) of the first car "
                  f"is greater than the engine volume --> {other.engine_volume}(L) of the second car")

        if self.year > other.year:
            print(f"The first car --> (release: {self.year}) was made later "
                  f"than the second car --> (release: {other.year})")

    def __str__(self):
        """
        :return: car info
        """
        return f"Car info\n" \
               f"Make: {self.make}\n" \
               f"Model: {self.model}\n" \
               f"Year: {self.year}\n" \
               f"Color car: {self.color_car}\n" \
               f"Engine volume: {self.engine_volume}\n" \
               f"Price car: {self.price_car}\n"

    def get_yaer(self):
        return f"Year of car production: {self.year}"

    def set_yaer(self, value):
        self.year = value

    def get_price(self):
        return f"You can buy this {self.make} {self.model} for {self.price_car} $"

    def set_price(self, value):
        self.price_car = value

    def get_color(self):
        return f"The color {self.make} {self.model}: {self.color_car}"

    def set_color(self, value):
        self.color_car = value

    def get_make(self):
        return f"Method that returns the brand of the car --> Brand:{self.make}"

    def get_model_car(self):
        return f"Method that returns the model of the car --> Model:{self.model}"

    def get_engine_volume_car(self):
        return f"Method that returns the volume of the engine --> Volume_engine: {self.engine_volume}(L)"


car = Car(model='Raptor', make='Ford', year=2021, engine_volume=5.3, color_car='Red', price_car=45_000)

print(Car.format_data(car))
desirialized = json.loads(Car.format_data(car))
print(Car.from_dict_to_instance(desirialized, Car))

