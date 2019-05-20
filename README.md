# 

Foobar is a Python library for dealing with word pluralization.

## Prerequisites

* [git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)  
* [Docker](https://docs.docker.com/install/linux/docker-ce/debian/#install-docker-ce)  
* [docker-compose](https://docs.docker.com/compose/install/)

## Run

```bash
git clone https://github.com/OmarEwedah/Flask-MYSQL.git
cd Flask-MYSQL/
docker-compose up -d --build
```

## Add Item in Database

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"item_name": "hamada","item_price": 200,"item_quantity": 10}' http://localhost:5000/shoppingBasket/AddItem

```

## Add cart to database
### From mysql command line

```mysql
# to connect to mysql

mysql -u root -p

# add example cart id

INSERT INTO shoppingBasket.shoppingCart (shoppingCart_id,item_price_total, item_quantity_total) VALUES (0,0,0);
```

## Add item to basket

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"item_id" : 1, "basket_id": 1, "item_quantity": 4}' http://localhost:5000/shoppingBasket/addItemToBasket
```
## Retrieve all items from basket

```bash
$ curl -X GET http://localhost:5000/shoppingBasket/1
```
