import constants
from processing_products import ProcessingProducts


class TestProductsList:

    def test_01_all_product_names(self):
        processing_products = ProcessingProducts()
        product_names = processing_products.get_products_names(constants.INPUT_DATA)
        expected_products = ["Pizza", "Sushi", "Burger", "Pad Thai"]
        for product in expected_products:
            assert product in product_names, (f"There is a difference between expected and actual product list. "
                                              f"Product '{product}' is missing from the list.")

    def test_02_product_prices(self):
        processing_products = ProcessingProducts()
        products = processing_products.get_products_with_price_more_than_threshold(constants.INPUT_DATA, 12.99)
        for product in products:
            assert product["price"] >= 12.99, (f"The product with a price of less than $12.99 on the list, "
                                               f"but expected not. "
                                               f"Product details {product}")