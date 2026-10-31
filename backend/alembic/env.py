
import sys
from pathlib import Path
from logging.config import fileConfig

from alembic import context

# Incorporar backend al sistema de importaciones Python
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_DIR))

# Configuración de Alembic
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Configuración de Aurum Trading
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app import models  # noqa: F401

# Metadatos de los modelos SQLAlchemy
target_metadata = Base.metadata


def run_migrations_offline():
    """Ejecutar migraciones sin establecer una conexión directa."""

    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Ejecutar migraciones mediante una conexión SQLAlchemy."""

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
