import mysql.connector


class DataBaseConnection:
    config = {
        'user': 'root',
        'password': 'root',
        'database': 'scrapper',
    }

    def __init__(self):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursorDB = self.cnx.cursor(buffered=True)
        self.cursorSelectDB = self.cnx.cursor(buffered=True)
        self.cursorLinks = self.cnx.cursor(buffered=True)

    def insertData(self, title, price, stockStatus, shop):
        # update value in database
        update_old_data = ("UPDATE scrapped_values SET product_price = %s, product_stock_status = %s WHERE product_name = %s AND product_shop = %s")
        # insert new value in database
        insert_new_data = (
            "INSERT INTO scrapped_values (product_name, product_price, product_stock_status, product_shop)"
            "VALUES (%s, %s, %s, %s)")
        # check if their is a product with current name and shop in database. If such product already exist update it, else insert
        query = ("SELECT * FROM scrapped_values WHERE product_name = %s AND product_shop = %s")

        self.cursorSelectDB.execute(query, (title, shop))
        isAlreadyExist = False
        for product_name in self.cursorSelectDB:
            isAlreadyExist = True
        if isAlreadyExist:
            self.cursorDB.execute(update_old_data, (price, stockStatus, title, shop))
        else:
            self.cursorDB.execute(insert_new_data, (title, price, stockStatus, shop))
        self.cnx.commit()

    def insertUrl(self, url):
        insert_new_link = ("INSERT INTO scrapper_links (link)"
                           "VALUES (%s)")
        self.cursorLinks.execute(insert_new_link, (url,))
        self.cnx.commit()

    def getUrls(self):
        result = []
        query = ("SELECT * FROM scrapper_links")
        self.cursorLinks.execute(query)
        for (id, link) in self.cursorLinks:
            result.append(link)
        self.cnx.commit()
        return result

    def insertErrorLink(self, url):
        insert_new_link = ("INSERT INTO scrapper_errors (link) VALUES (%s)")
        self.cursorLinks.execute(insert_new_link, (url,))
        self.cnx.commit()
