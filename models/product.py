class Product():
    
    def __init__():

    @classmethod
    def get(cls, api, database):
            """ Method retrieving products in order to save them into database."""
            # Retrieve categories' data from database
            categories = Category.select())

            for category in categories:
                # Call method to search products in api and send category
                products = api.fetch_products_data_api(category)
                # For each products' data retrieve only needed ones per product
                for product in products:
                    prod_name = data_product.get('product_name', 'None')
                    prod_ingredients = data_product.get('ingredients_text_fr')
                    prod_url = data_product.get('url')
                    prod_nutriscore = data_product.get('nutrition_grade_fr')

                    prod_categories = data_product.get('categories')
                    prod_stores = data_product.get('stores')

                    product = cls(
                                    name=prod_name, description=prod_ingredients,
                                    url=prod_url, nutrition_grade=prod_nutriscore
                    )
                    product.save(database)

                    # Retrieve the last product inserted in database
                    last_id_product = database.mycursor.lastrowid
                    # Retrieve the last category inserted in database
                    last_id_cat = category.id

                    product.link_prod_cat(database, prod_categories,
                                          last_id_product, last_id_cat)
                    product.link_prod_shop(database, prod_stores, last_id_product)
            # database.add_column_to_product()