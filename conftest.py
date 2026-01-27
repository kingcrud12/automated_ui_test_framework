import pytest
from selenium_ui_test_tool import create_driver

@pytest.fixture(scope="function")
def driver():
    """
    Fixture locale pour tests/login.
    Nécessaire car l'exécution depuis ce dossier ne remonte pas toujours à la racine.
    """
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return ""
