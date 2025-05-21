from setuptools import setup, find_packages

setup(
    name="gx_plugin",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "great-expectations[fluent]",
        "python-dotenv",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "gx-init = gx_plugin.cli:run"
        ]
    }
)