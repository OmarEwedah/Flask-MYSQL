from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy import MetaData, create_engine, engine
from os import environ as env

metadata = MetaData()

# Database Configurations
app = Flask(__name__)
DATABASE = env.get("DATABASE")
PASSWORD = env.get("PASSWORD")
USER = env.get("USER")
HOSTNAME = env.get("HOSTNAME")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % (USER, PASSWORD, HOSTNAME, DATABASE)
db = SQLAlchemy(app)

# Database migration command line
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Items(db.Model):
    __tablename__ = 'Items'
    item_id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    item_name = db.Column(db.String(120), nullable=False)
    item_price = db.Column(db.DECIMAL)
    item_quantity = db.Column(db.Integer, nullable=False)


def __init__(self, item_name, item_price, item_quantity):
    # initialize columns
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity


def __repr__(self):
    return '<Item %r>' % self.item_name


class shoppingcart(db.Model):
    __tablename__ = 'shoppingCart'
    shoppingCart_id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    item_price_total = db.Column(db.DECIMAL)
    item_quantity_total = db.Column(db.Integer, nullable=False)

    def __init__(self, item_price_total, item_quantity_total):
        # initialize columns
        self.item_price_total = item_price_total
        self.item_quantity_total = item_quantity_total

    def __repr__(self):
        return '<shoppingCart %r>' % self.shoppingCart_id


class Shoppingcartitems(db.Model):
    __tablename__ = 'Shopping_cart_items'
    shopping_cartId = db.Column(db.Integer, db.ForeignKey('shoppingCart.shoppingCart_id'), nullable=False,
                                primary_key=True)
    shoppingCart = db.relationship("shoppingcart", backref=db.backref("shoppingCart", uselist=False))
    item_id = db.Column(db.Integer, db.ForeignKey('Items.item_id'), nullable=False, primary_key=True)
    Items = db.relationship("Items", backref=db.backref("Items", uselist=False))

    def __init__(self, shopping_cartId, item_id):
        # initialize columns
        self.shopping_cartId = shopping_cartId
        self.item_id = item_id

# connect to server
engine = create_engine('mysql://%s:%s@%s' % (USER, PASSWORD, HOSTNAME))

# create db if not exists
engine.execute("CREATE DATABASE IF NOT EXISTS %s " % (DATABASE))

db.create_all()
if __name__ == '__main__':
    manager.run()
