class ProcessingProducts:

    def get_products_names(self, response_json) -> list[str]:
        return [product["name"] for product in response_json["products"]]

    def get_products_with_price_more_than_threshold(self, response_json, threshold) -> list[dict]:
        return [product for product in response_json["products"] if product["price"] >= threshold]
