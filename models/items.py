from enum import unique
from sqlalchemy.orm import backref
from models import db


class ItemType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<ItemType {self.name}>"


class Characteristic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Characteristic {self.name}>"


class Check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characteristic_id = db.Column(db.Integer, db.ForeighKey("characteristic.id"), nullable=False)
    characteristic = db.relationship("Characteristic", backref=db.backref("checks", lazy=True))
    quantity = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"<Check {self.id}>"


class CheckGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_id = db.Column(db.Integer, db.ForeignKey("check.id"), nullable=False)
    check = db.relationship("Check", backref=db.backref("checkgroups", lazy=True))
    use_and = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return f"<CheckGroup {self.id}>"


class ItemEffect(db.Model):
    pass


class ItemEffectGroup(db.Model):
    pass


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    itemtype_id = db.Column(db.Integer, db.ForeignKey("itemtype.id"), nullable=False)
    itemtype = db.relationship("ItemType", backref=db.backref("items", lazy=True))

    check_group_id = None
    item_effect_group = None



    def __repr__(self):
        return f"<Item {self.name}>"

