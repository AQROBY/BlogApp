import pytest
from website import create_app

@pytest.fixture(name="app")
def fixture_app():
    blogApp = create_app()
    yield blogApp

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()