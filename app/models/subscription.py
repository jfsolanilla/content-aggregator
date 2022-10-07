import sqlalchemy as sa
from sqlalchemy import orm

from app.models.user import User
from app.models.source import Source
from app.models.section import Section

class Subscription(Base, IDMixin, AuditMixin):
    user_id = sa.Column(
        sa.BigInteger,
        sa.ForeignKey(User.id),
        nullable=False,
        primary_key=True,
    )
    source_id = sa.Column(
        sa.BigInteger,
        sa.ForeignKey(Source.id),
        nullable=False,
        primary_key=True,
    )
    section_id = sa.Column(
        sa.BigInteger,
        sa.ForeignKey(Section.id),
        nullable=False,
        primary_key=True,
    )

    user = orm.relationship('User', back_populates='subscription')
    section = orm.relationship('Section', back_populates='subscription')