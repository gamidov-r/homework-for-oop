import pytest

from src.main import Category, Product


@pytest.fixture
def test_products() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description.startswith("256GB")
    assert product1.price == 18000.0
    assert product1.quantity == 5


def test_categories() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert category1.name == "Смартфоны"
    assert category1.description.startswith("Смартфоны, ")
    assert category1.category_count == 1
    assert category1.product_count == 3
