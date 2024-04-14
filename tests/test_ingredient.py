from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestIngredient:
    # Получение цены добавленного ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 100),
        (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 150),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 200),
        (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 250),])
    def test_get_price_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    # Получение имени добавленного ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 100),
        (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 150),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 200),
        (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 250),])
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    # Получение типа добавленного ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 100),
        (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 150),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 200),
        (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 250),])
    def test_get_type_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
