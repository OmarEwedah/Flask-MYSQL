import logging


def check_item_exist(connection, item_id):
    sql = "SELECT * FROM shoppingBasket.Items WHERE item_id = %s"
    try:
        retrieved = connection.execute(sql, item_id)
        item = []
        for row in retrieved:
            item = row
        if item is None:
            return False
        else:
            return item

    except RuntimeError:
        raise
    except Exception as e:
        logging.exception(e)


def check_cart_exist(connection, cart_id):
    sql = "SELECT * FROM shoppingBasket.shoppingCart WHERE shoppingCart_id = %s"
    try:
        retrieved = connection.execute(sql, cart_id)
        cart = []
        for row in retrieved:
            cart = row
        cart_id = [row[0] for row in cart]
        if cart is None:
            print "here"
            connection.execute("INSERT INTO shoppingBasket.shoppingCart (item_price_total, item_quantity_total) VALUES (0, 0)")
        else:
            return cart
    except RuntimeError:
        raise
    except Exception as e:
        logging.exception(e)


def change_item_quantity(connection, item_id, quantity):
    result = check_item_exist(connection, item_id)
    retrieved_quantity= []
    if quantity <= result[3]:
        newQuantity = result[3] - quantity
        update_sql = "UPDATE  shoppingBasket.Items SET item_quantity=%s WHERE  item_id =%s;"
        connection.execute(update_sql, (newQuantity, item_id))
        return True
    else:
        return False


# def update_cart_price_quantity(connection, item_id, basket_id, quantity):
#     Item_sql = connection.execute("SELECT * FROM shoppingBasket.Items WHERE item_id = %s", item_id)
#     cart_sql = connection.execute("SELECT * FROM shoppingBasket.shoppingCart WHERE shoppingCart_id = %s", basket_id)

#     Item = []
#     cart = []
#     print cart
#     for row in Item_sql:
#         Item = row
#     for row in cart_sql:
#         cart = row
#     if cart is []:
#         connection.execute("INSERT INTO shoppingBasket.shoppingCart (shoppingCart_id, item_price_total, item_quantity_total) VALUES (%s,0, 0)", basket_id)
#         cart = (basket_id, 0, 0)
#     Item_price = Item[2]
#     Old_cart_total_price = int(cart[1])
#     Old_cart_quantity = int(cart[2])
#     newTotalPrice = Old_cart_total_price + Item_price * quantity
#     newTotalQuantity = Old_cart_quantity + quantity
#     update_sql = "UPDATE shoppingBasket.shoppingCart SET item_price_total= %s, item_quantity_total= %s  WHERE  shoppingCart_id =%s;"
#     try:
#         connection.execute(update_sql, (newTotalPrice, newTotalQuantity, basket_id))
#         return True

#     except RuntimeError:
#         raise
#     except Exception as e:
#         logging.exception(e)

def update_cart_price_quantity(connection, item_id, basket_id, quantity):
    Item_sql = connection.execute("SELECT * FROM shoppingBasket.Items WHERE item_id = %s", item_id)
    cart_sql = connection.execute("SELECT * FROM shoppingBasket.shoppingCart WHERE shoppingCart_id = %s", basket_id)
    Item = []
    cart = []
    for row in Item_sql:
        Item = row
    for row in cart_sql:
        cart = row
    Item_price = Item[2]
    Old_cart_total_price = int(cart[1])
    Old_cart_quantity = int(cart[2])
    newTotalPrice = Old_cart_total_price + Item_price * quantity
    newTotalQuantity = Old_cart_quantity + quantity
    update_sql = "UPDATE shoppingBasket.shoppingCart SET item_price_total= %s, item_quantity_total= %s  WHERE  shoppingCart_id =%s;"
    try:
        connection.execute(update_sql, (newTotalPrice, newTotalQuantity, basket_id))
        return True

    except RuntimeError:
        raise
    except Exception as e:
        logging.exception(e)


def add_item_to_basket(connection, item_id, basket_id):
    sql = "INSERT IGNORE INTO shoppingBasket.Shopping_cart_items (shopping_CartId, item_id) VALUES (%s, %s);"
    try:
        connection.execute(sql, (basket_id, item_id))
        return True

    except RuntimeError:
        raise
    except Exception as e:
        logging.exception(e)


def retrieve_total_price_from_basket(connection, basket_id):
    sql = "SELECT * FROM shoppingBasket.shoppingCart WHERE shoppingCart_id = %s"
    cart = []
    try:
        result = connection.execute(sql, basket_id)
        for row in result:
            cart = row
        return cart
    except RuntimeError:
        raise
    except Exception as e:
        logging.exception(e)


def retrieve_all_items_from_basket(connection, basket_id):
    Items = []
    sql = "SELECT * FROM shoppingBasket.Shopping_cart_items WHERE shopping_cartId = %s"
    try:
        rows = connection.execute(sql, basket_id)
        for row in rows:
            item_id = row[1]
            result = connection.execute("SELECT * FROM shoppingBasket.Items WHERE item_id = %s", item_id)
            for item in result:
                Items.append(dict(item))
        return Items
    except RuntimeError:
        raise
    except Exception as e:
        logging.exception(e)