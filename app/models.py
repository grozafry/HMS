from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import db

# db = SQLAlchemy()
# migrate = Migrate()
# db.init_app(app)
# migrate.init_app(app, db)

class Subscriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)

class RulesMaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    checker_func = db.Column(db.String(80), nullable=False)

class SubscriptionRules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.id'), nullable=False)
    rule_id = db.Column(db.Integer, db.ForeignKey('rules_master.id'), nullable=False)