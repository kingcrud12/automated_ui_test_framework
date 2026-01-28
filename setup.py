from setuptools import setup, find_packages

setup(
    name="promethee-selenium",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "selenium-ui-test-tool",
        "pytest",
        "selenium"
    ],
    entry_points={
        "console_scripts": [
            "promethee=promethee.cli:main",
        ],
    },
    author="Yann Dipita",
    description="Prométhée: A POM-based automated UI test framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    package_data={
        "promethee": ["docs/*"],
    }
)
