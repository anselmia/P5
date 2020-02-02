"""
    This library is uesd to communicate with the OpenFoodFact API
"""

import requests


class OpenFoodFactsApi:
    """ This library regroup methods to interogate the OpenFoodFact API """

    @staticmethod
    def fetch_categories_data_api(Message):
        """
            Method allowing the program to search categories' data online
            with the Open Food Facts API.
            Exceptions like HTTP, TimeOut, Connexion and other will be catched
            Return a list of category as dictionnary
        """
        category_names = []
        try:
            # Recover data from Open Food Facts URL API with request get.
            response = requests.get("https://fr.openfoodfacts.org/categories.json", timeout=3)
            # raise an exception if the request was unsuccessful
            response.raise_for_status()
            # Save the json data in a variable.
            json_data_file = response.json()
            # Get only the data needed: data besides the one in the "tags"
            # list are irrelevant here.
            # Input are filtered to avoid getting ":" in the name attribute or empty name
            category_names = [
                category.get("name")
                for category in json_data_file.get("tags")
                if (":" not in category.get("name") and len(category.get("name")) > 1)
            ]

        except requests.exceptions.HTTPError:
            Message.http_error()
        except requests.exceptions.ConnectionError:
            Message.connexion_error()
        except requests.exceptions.Timeout:
            Message.timeout()
        except requests.exceptions.RequestException:
            Message.other_api_exception()

        finally:
            return category_names

    @staticmethod
    def fetch_products_data_api(Message, category, filtered_tags):
        """
            Method allowing the program to search product' data online
            with the Open Food Facts API.
            Exceptions like HTTP, TimeOut, Connexion and other will be catched
            Return a list of products as dictionnary
            Arg : category of product and tags to filter in product tags
        """
        products = []
        # Properties to filter the product queries
        filters = {
            "action": "process",
            "tagtype_0": "categories",  # which subject is selected (categories)
            "tag_contains_0": "contains",  # contains or not
            "tag_0": category,  # parameters to choose
            "sort_by": "unique_scans_n",
            "countries": "France",
            "page_size": 1000,
            "page": 1,
            "json": 1,
        }

        try:
            # Recover data from Open Food Facts URL API with request get.
            response = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params=filters)
            # Save the json data in a variable.
            json_data_file = response.json()
            # Get only the data needed: data besides the one in the "products"
            data_products = json_data_file.get("products")

            # Create a list of product as dictionary from the dictionary of
            # products data_products
            # {key: product[key] for key in product.keys() & {i: None for i in filtered_tags}}
            # --> create a product dictionary filtering the keys using filtered_tags
            # all(item in list(product.keys()) for item in filtered_tags)
            # --> Filtered the product to match all keys present in filtered_tags
            products = [
                {key: product[key] for key in product.keys() & {i: None for i in filtered_tags}}
                for product in data_products
                if all(item in list(product.keys()) for item in filtered_tags)
            ]

        except requests.exceptions.HTTPError:
            Message.http_error()
        except requests.exceptions.ConnectionError:
            Message.connexion_error()
        except requests.exceptions.Timeout:
            Message.timeout()
        except requests.exceptions.RequestException:
            Message.other_api_exception()

        finally:
            return products
