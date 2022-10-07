import sqlalchemy as sa
from sqlalchemy import orm

from app.database import Base
from app.mixins import AuditMixin, IDMixin

section_source_table = sa.Table(
    'section_source',
    metadata,
    sa.Column(
        'section_id',
        sa.ForeignKey('section.id'),
        primary_key=True,
    ),
    sa.Column(
        'source_id',
        sa.ForeignKey('source.id'),
        primary_key=True,
    ),
)


class Section(Base, IDMixin, AuditMixin):
    name = sa.Column(String, nullable=False)

    subscription = orm.relationship('Subscription', back_populates='section')
    source = orm.relationship(
        "Source", secondary=section_source_table, back_populates="section"
    )


class Source(Base, IDMixin, AuditMixin):
    name = sa.Column(String, nullable=False)

    article = orm.relationship('Article', back_populates='source')
    section = orm.relationship(
        "Section", secondary=section_source_table, back_populates="source"
    )
