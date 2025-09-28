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

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.category_count += 1

    @property
    def products(self) -> None:
        for item in self.__products:
            print("{}, {} руб. Остаток: {} шт.\n".format(item.name, item.price, item.quantity))
