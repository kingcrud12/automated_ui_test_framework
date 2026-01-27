# Automated UI Test Framework

*[English version below | Version française plus bas]*

---

# 🇬🇧 English Description

A robust, Page Object Model (POM) based framework for automated UI testing using Selenium and Pytest.

This framework is designed to help you write maintainable and scalable end-to-end tests with minimal boilerplate.

## Features

-   **Page Object Model (POM)**: Structured architecture separating page logic from test logic.
-   **Scaffolding CLI**: Quickly initialize a new project with best-practice directory structure using `automated-ui-framework init`.
-   **Built-in Utilities**: Ready-to-use helpers for Waiting, Clicking, Filling inputs (via `selenium-ui-test-tool`).
-   **Environment Management**: Easy handling of test data and credentials.
-   **Documentation**: Includes HTML documentation to help you get started.

## Installation

Install the package via pip:

```bash
pip install Auomated-ui-test-framework
```

## Getting Started

1.  **Create a new folder** for your test project:
    ```bash
    mkdir my_test_project
    cd my_test_project
    ```

2.  **Initialize the project structure**:
    ```bash
    automated-ui-framework init
    ```
    This will create:
    -   `scenarios/`: For your Page Objects.
    -   `tests/`: For your test scripts.
    -   `data/`: For credentials and test data.
    -   `utils/`: For local utilities.
    -   `conftest.py`: Pytest configuration.

3.  **Run the sample test**:
    ```bash
    pytest tests/
    ```

## Writing a Page Object

Inherit from the `Base` class provided by the framework:

```python
from automated_ui_test_framework.base import Base
from selenium.webdriver.common.by import By
# Uses selenium-ui-test-tool functions internally

class LoginPage(Base):
    def fill_form(self, username, password):
        self.fill_input(By.ID, "username", username)
        self.fill_input(By.ID, "password", password)
        self.click_element(By.ID, "submit-btn")
```

For more details, check the generated `docs/index.html` after installation.

---

# 🇫🇷 Description Française

Un framework robuste basé sur le modèle Page Object Model (POM) pour l'automatisation de tests UI avec Selenium et Pytest.

Ce framework est conçu pour vous aider à écrire des tests de bout en bout maintenables et évolutifs avec un minimum de code répétitif.

## Fonctionnalités

-   **Page Object Model (POM)** : Architecture structurée séparant la logique de la page de la logique de test.
-   **CLI d'initialisation** : Initialisez rapidement un nouveau projet avec une structure recommandée via `automated-ui-framework init`.
-   **Utilitaires intégrés** : Fonctions prêtes à l'emploi pour attendre, cliquer, remplir des champs (via `selenium-ui-test-tool`).
-   **Gestion d'environnement** : Gestion facile des données de test et des identifiants.
-   **Documentation** : Inclut une documentation HTML pour vous aider à démarrer.

## Installation

Installez le paquet via pip :

```bash
pip install Auomated-ui-test-framework
```

## Démarrage Rapide

1.  **Créez un nouveau dossier** pour votre projet de test :
    ```bash
    mkdir mon_projet_test
    cd mon_projet_test
    ```

2.  **Initialisez la structure du projet** :
    ```bash
    automated-ui-framework init
    ```
    Cela va créer :
    -   `scenarios/` : Pour vos Page Objects.
    -   `tests/` : Pour vos scripts de test.
    -   `data/` : Pour les identifiants et données de test.
    -   `utils/` : Pour les utilitaires locaux.
    -   `conftest.py` : Configuration Pytest.

3.  **Lancez le test d'exemple** :
    ```bash
    pytest tests/
    ```

## Écrire un Page Object

Héritez de la classe `Base` fournie par le framework :

```python
from automated_ui_test_framework.base import Base
from selenium.webdriver.common.by import By
# Utilise les fonctions selenium-ui-test-tool en interne

class LoginPage(Base):
    def fill_form(self, username, password):
        self.fill_input(By.ID, "username", username)
        self.fill_input(By.ID, "password", password)
        self.click_element(By.ID, "submit-btn")
```

Pour plus de détails, consultez le fichier `docs/index.html` généré après l'installation.
