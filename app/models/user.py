import sqlalchemy as sa
from sqlalchemy import orm

from app.database import Base
from app.mixins import AuditMixin, IDMixin

class User(Base, IDMixin, AuditMixin):
    name = sa.Column(String, nullable=False)

    subscription = orm.relationship('Subscription', back_populates='user')
