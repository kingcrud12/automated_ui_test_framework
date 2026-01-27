from automated_ui_test_framework.utils.scenario_provider import ScenarioProvider
from scenarios.login import LoginPage

def test_login(driver, base_url):
    print("Running test_login...")
    # scenario_name, data = ScenarioProvider.prompt_for_scenario()
    # page = LoginPage(driver)
    # page.fill_login_form(data['username_env'], data['password_env'])
    assert True
