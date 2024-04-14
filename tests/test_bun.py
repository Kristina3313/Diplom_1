import pytest
from praktikum.bun import Bun


class TestBun:
    # Получение названия булочки
    @pytest.mark.parametrize("name, price", [('Флюоресцентная булка R2-D3', 100), ('Краторная булка N-200i', 200)])
    def test_get_name_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Получение цены булочки
    @pytest.mark.parametrize("name, price", [('Флюоресцентная булка R2-D3', 100), ('Краторная булка N-200i', 200)])
    def test_get_price_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
