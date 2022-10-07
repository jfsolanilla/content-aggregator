import sqlalchemy as sa
from sqlalchemy import orm

from app.models.source import Source

class Article(Base, IDMixin, AuditMixin):
    source_id = sa.Column(
        sa.BigInteger,
        sa.ForeignKey(Source.id),
        nullable=False,
        primary_key=True,
    )

    source = orm.relationship('Source', back_populates='article')