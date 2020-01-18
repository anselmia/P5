    def get(cls, api, database):
        """ Method retrieving stores in order to save them into database. """
        # Retrieve list of stores' name
        store_data = api.fetch_stores_data_api()

        for name in store_data[:20]:
            shop = cls(name=name)
            shop.save(database)