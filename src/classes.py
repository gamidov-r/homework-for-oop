import sys


class Product:
    """класс, описывающий продукты"""

    name: str
    description: str
    # price: float
    quantity: float

    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: str):
        if isinstance(other, Product):
            return self.quantity * self.price + other.quantity * other.price
        else:
            return TypeError

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        # zero is positive price ? I think zero is undefined price as negative
        # additional solution №4
        if price == self.__price:
            pass
        elif self.__price > price > 0:
            if input("submit new price? ") == "y":
                # if "y" == "y":
                self.__price = price
        elif price > self.__price:
            self.__price = price

        else:
            # output to console is print or stdout ?
            # print("Цена не должна быть нулевая или отрицательная")
            sys.stdout.write("Цена не должна быть нулевая или отрицательная\n")



    @classmethod
    def new_product(cls, product: dict) -> "Product":
        return cls(product["name"], product["description"], product["price"], product["quantity"])



class Category:
    """класс, описывающий категории"""

    name: str
    description: str
    __products: list
    category_count: int
    product_count: int
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        # return "ok"
        return f"{self.name}, количество продуктов: {str(self.product_count)} шт."

    def add_product(self, product) -> None:
        if isinstance(product, Product):
            if product.name not in self.__products:
                self.__products.append(product)
                Category.category_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> None:
        result = ""
        for item in self.__products:
            result += "{}, {} руб. Остаток: {} шт.\n".format(item.name, item.price, item.quantity)
        return result


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        # if isinstance(other, Smartphone):
        if issubclass(type(other), Smartphone):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError




class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if isinstance(other, LawnGrass):
        # if issubclass(type(other), Smartphone):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError

