import pytest

from src.classes import Category, Product


def test_raise_product():
    with pytest.raises(ValueError):
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_raise_category():
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert 0 == category_empty.middle_price()