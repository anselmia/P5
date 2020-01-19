import requests


class OpenFoodFactsApi:
    """ Retrieve different data from online API."""
    @staticmethod
    def fetch_stores_data_api():
        """
            Method allowing the program to search stores' data online
            with the Open Food Facts API.
        """
        # Recover data from Open Food Facts URL API with request get.
        response = requests.get(
                                "https://fr.openfoodfacts.org/categorie/"
                                "stores.json"
        )
        # Save the json data in a variable.
        json_data_file = response.json()
        # Get only the data needed: data besides the one in the "tags"
        # list are irrelevant here.
        data_tags = json_data_file.get('tags')
        # Select only the name of each store (no need for other data).
        store_data = [element.get('name', 'None') for element in data_tags]
        return store_data

    @staticmethod
    def fetch_categories_data_api(log):
        """
            Method allowing the program to search categories' data online
            with the Open Food Facts API.
        """
        category_names = []
        try:
            # Recover data from Open Food Facts URL API with request get.
            response = requests.get('https://fr.openfoodfacts.org/categories.json', timeout=3)
            response.raise_for_status()
            # Save the json data in a variable.
            json_data_file = response.json()
            #tags = {key: product[key] for key in product.keys() & {i : None for i in filtered_tags}}
            #categories = [ for product in data_products if all(item in list(product.keys()) for item in filtered_tags)]
            # Get only the data needed: data besides the one in the "tags"
            # list are irrelevant here.
            category_names = [category.get('name') for category in json_data_file.get('tags') if (':' not in category.get('name') and len(category.get('name')) > 1)]
        
        except requests.exceptions.HTTPError as errh:
            log.appendText("Http Error:" + str(errh), (255,30,30))
        except requests.exceptions.ConnectionError as errc:
            log.appendText("Error Connecting:" + str(errc), (255,30,30))
        except requests.exceptions.Timeout as errt:
            log.appendText("Timeout Error:" + errt, (255,30,30))
        except requests.exceptions.RequestException as err:
            log.appendText("OOps: Something Else" + err, (255,30,30))
        
        finally:
            return category_names

    @staticmethod
    def fetch_products_data_api(log, category, filtered_tags):
        """
            Method allowing the program to search products' data online
            with the Open Food Facts API.
        """
        # With the name of each category saved inside the database, do a
        # concatenation with the name of the category and the rest of the URL
        #url_categories = (
        #                f'''https://fr.openfoodfacts.org/categorie/{category}.json'''
        #)
        products = []
        payload = {
            'action': 'process',
            'tagtype_0': 'categories', #which subject is selected (categories)
            'tag_contains_0': 'contains', #contains or not
            'tag_0': category, #parameters to choose
            'sort_by': 'unique_scans_n',
            'countries': 'France',
            'page_size': 1000,
            'page': 1,
            'json': 1
            }
        
        try:
            response = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
        
            ## Recover data from Open Food Facts URL API with request get.
            #response = requests.get(url_categories)
            ## Save the json data in a variable.
            json_data_file = response.json()
            # Get only the data needed: data besides the one in the "products"
            # list are irrelevant here.
            data_products = json_data_file.get('products')     

            products = [{key: product[key] for key in product.keys() & {i : None for i in filtered_tags}} for product in data_products if all(item in list(product.keys()) for item in filtered_tags)]
        
        except requests.exceptions.HTTPError as errh:
            log.appendText("Http Error:" + str(errh), (255,30,30))
        except requests.exceptions.ConnectionError as errc:
            log.appendText("Error Connecting:" + str(errc), (255,30,30))
        except requests.exceptions.Timeout as errt:
            log.appendText("Timeout Error:" + errt, (255,30,30))
        except requests.exceptions.RequestException as err:
            log.appendText("OOps: Something Else" + err, (255,30,30))
        
        finally:
            return products
    
