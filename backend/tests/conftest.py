
import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app import models  # noqa: F401
from app.db.base import Base
from app.db.session import get_db
from app.core.config import settings
from app.main import app


TEST_DATABASE_NAME = "aurum_trading_test"


def get_test_engine():
    """Construye una conexión dirigida exclusivamente a la BD de pruebas."""

    from sqlalchemy.engine import make_url

    database_url = make_url(settings.DATABASE_URL)
    test_url = database_url.set(database=TEST_DATABASE_NAME)

    if test_url.database != TEST_DATABASE_NAME:
        raise RuntimeError("Unsafe test database configuration")

    return create_engine(test_url, pool_pre_ping=True)


@pytest.fixture(scope="session")
def engine():
    test_engine = get_test_engine()

    if test_engine.url.database != TEST_DATABASE_NAME:
        raise RuntimeError("Refusing to run tests on a non-test database")

    Base.metadata.create_all(bind=test_engine)

    yield test_engine

    # Conservamos el esquema de pruebas entre ejecuciones.
    # Los datos de cada prueba se revierten mediante rollback.
    test_engine.dispose()


@pytest.fixture
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()

    session = Session(
        bind=connection,
        join_transaction_mode="create_savepoint",
    )

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
