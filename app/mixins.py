import sqlalchemy as sa

class IDMixin:
    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)

class AuditMixin:
    created_at = sa.Column(
        sa.Datetime(timezone=True),
        nullable=False,
        server_default=sa.func.current_timestamp(),
    )
    created_by = sa.Column(sa.String, nullable=False)

    updated_at = sa.Column(
        sa.Datetime(timezone=True),
        nullable=False,
        server_default=sa.func.current_timestamp(),
        onupdate=sa.func.current_timestamp(),
    )
    updated_by = sa.Column(
        sa.String,
        nullable=False,
    )

    deleted_at = sa.Column(
        sa.Datetime(timezone=True),
        nullable=True,
    )
    deleted_by = sa.Column(
        sa.String,
        nullable=True,
    )