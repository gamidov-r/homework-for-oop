class Product:
    """класс, описывающий продукты"""

    name: str
    description: str
    price: float
    quantity: float

    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """класс, описывающий категории"""

    name: str
    description: str
    products: list
    category_count: int
    product_count: int
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
