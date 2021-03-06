# Deploy Flask + MySQL with docker-compose

## shopping Basket
* use cases:
   * "as a customer, i want to add an item into the basket"
   * "as a customer, i want to view all my items in my basket"
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
$ curl -X POST -H "Content-Type: application/json" -d '{"item_name": "Short","item_price": 200,"item_quantity": 10}' http://localhost:5000/shoppingBasket/AddItem
```

## Add item to basket

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"item_id" : 1, "basket_id": 1, "item_quantity": 4}' http://localhost:5000/shoppingBasket/addItemToBasket
```
## Retrieve all items from basket

```bash
$ curl -X GET http://localhost:5000/shoppingBasket/1
```