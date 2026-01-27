from setuptools import setup, find_packages

setup(
    name="Auomated_ui_test_framework",
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "selenium-ui-test-tool",
        "pytest",
        "selenium"
    ],
    entry_points={
        "console_scripts": [
            "automated-ui-framework=automated_ui_test_framework.cli:main",
        ],
    },
    author="Hugo Testas",
    description="A POM-based automated UI test framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    package_data={
        "automated_ui_test_framework": ["docs/*"],
    }
)
