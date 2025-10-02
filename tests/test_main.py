import pytest

from src.classes import Category, Product


@pytest.fixture
def test_products() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert print(str(product1)) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert print(str(product2)) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert print(str(product3)) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    assert print(product1 + product2) == 2580000.0
    assert print(product1 + product3) == 1334000.0
    assert print(product2 + product3) == 2114000.0


def test_categories() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1)) == "Смартфоны, количество продуктов: 144 шт."
