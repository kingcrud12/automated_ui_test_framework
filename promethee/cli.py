import argparse
import os
import shutil
import webbrowser
import sys

def open_docs():
    """
    Opens the framework documentation in the default web browser.
    """
    try:
        # Try to locate the docs using pkg_resources (older but reliable) or file path relative to this file
        # Since we are in promethee/cli.py, docs are in promethee/docs/index.html
        
        # Method 1: Relative path from __file__
        current_dir = os.path.dirname(os.path.abspath(__file__))
        docs_path = os.path.join(current_dir, "docs", "index.html")
        
        if os.path.exists(docs_path):
            print(f"Opening documentation: {docs_path}")
            webbrowser.open(f"file://{docs_path}")
        else:
            print("Documentation file not found locally.")
            print("You can view it online on PyPI or GitHub.")
            
    except Exception as e:
        print(f"Failed to open documentation: {e}")

def init_project():
    """
    Initializes a new test project with the recommended structure.
    """
    base_dir = os.getcwd()
    print(f"Initializing new test project in: {base_dir}")

    # Define directories to create
    dirs = ["scenarios", "tests", "data", "utils"]
    for d in dirs:
        path = os.path.join(base_dir, d)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {d}")
    
    # Create __init__.py in scenarios and utils to make them packages
    for pkg in ["scenarios", "utils"]:
        init_path = os.path.join(base_dir, pkg, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, "w") as f:
                pass

    # Create utils/scenario_provider.py
    scenario_provider_path = os.path.join(base_dir, "utils", "scenario_provider.py")
    if not os.path.exists(scenario_provider_path):
        with open(scenario_provider_path, "w") as f:
            f.write("""import csv
import os

class ScenarioProvider:
    # Look for credentials in the data directory
    CREDENTIALS_FILE = os.path.join(os.getcwd(), 'data', 'credentials.csv')

    @staticmethod
    def get_data_for_scenario(scenario_name):
        if not os.path.exists(ScenarioProvider.CREDENTIALS_FILE):
             raise FileNotFoundError(f"Credentials file not found at {ScenarioProvider.CREDENTIALS_FILE}")

        with open(ScenarioProvider.CREDENTIALS_FILE, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['scenario'] == scenario_name:
                    user_env_key = f"TEST_USER_{scenario_name.upper().replace(' ', '_')}"
                    pass_env_key = f"TEST_PASS_{scenario_name.upper().replace(' ', '_')}"
                    os.environ[user_env_key] = row['email']
                    os.environ[pass_env_key] = row['password']
                    
                    return {
                        "username_env": user_env_key,
                        "password_env": pass_env_key
                    }
        
        raise ValueError(f"Scenario '{scenario_name}' not found in credentials.csv")

    @staticmethod
    def prompt_for_scenario(default_scenario="login"):
        # In automated environments (CI), you might want to switch this to read an env var
        print(f"Using default scenario: {default_scenario}")
        return default_scenario, ScenarioProvider.get_data_for_scenario(default_scenario)
""")
        print("Created utils/scenario_provider.py")

    # Create credentials.csv
    creds_path = os.path.join(base_dir, "data", "credentials.csv")
    if not os.path.exists(creds_path):
        with open(creds_path, "w") as f:
            f.write("scenario,email,password\\nlogin,test@example.com,secret123\\n")
        print("Created data/credentials.csv")

    # Create conftest.py
    conftest_path = os.path.join(base_dir, "conftest.py")
    if not os.path.exists(conftest_path):
        with open(conftest_path, "w") as f:
            f.write("""import pytest
from promethee.conftest import driver, base_url

# You can add local fixtures here
""")
        print("Created conftest.py")

    # Create sample scenario (login.py)
    login_scenario_path = os.path.join(base_dir, "scenarios", "login.py")
    if not os.path.exists(login_scenario_path):
        with open(login_scenario_path, "w") as f:
            f.write("""from promethee.base import Base
from selenium.webdriver.common.by import By
from selenium_ui_test_tool import fill_input, click_element, wait_for_element

class LoginPage(Base):
    def fill_login_form(self, username, password):
        print(f"Logging in with {username}...")
        # Example implementation
        # fill_input(self.driver, By.ID, "username", username)
        # fill_input(self.driver, By.ID, "password", password)
        # click_element(self.driver, By.ID, "login-btn")
""")
        print("Created scenarios/login.py")

    # Create generic sample test
    test_path = os.path.join(base_dir, "tests", "test_login.py")
    if not os.path.exists(test_path):
        with open(test_path, "w") as f:
            f.write("""from utils.scenario_provider import ScenarioProvider
from scenarios.login import LoginPage

def test_login(driver, base_url):
    print("Running test_login...")
    scenario_name, data = ScenarioProvider.prompt_for_scenario()
    
    page = LoginPage(driver)
    page.fill_login_form(data['username_env'], data['password_env'])
    
    assert True
""")
        print("Created tests/test_login.py")
    
    print("\nProject initialized successfully!")
    print("Run your tests with: pytest tests/")

def main():
    parser = argparse.ArgumentParser(description="Prométhée UI Test Framework CLI")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Initialize a new test project")
    docs_parser = subparsers.add_parser("docs", help="Open the documentation in browser")

    args = parser.parse_args()

    if args.command == "init":
        init_project()
    elif args.command == "docs":
        open_docs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
