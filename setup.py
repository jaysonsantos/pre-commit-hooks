from setuptools import find_packages
from setuptools import setup


setup(
    name="jaysonsantos_pre_commit_hooks",
    description="My pre-commit hooks",
    url="https://github.com/jaysonsantos/pre-commit-hooks",
    version="0.1.0",
    author="Jayson Reis",
    author_email="santosdosreis@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages(),
    install_requires=["poetry", "pipenv", "virtualenv"],
    entry_points={
        "console_scripts": [
            "poetry-lock = jaysonsantos_pre_commit_hooks.poetry_lock:main",
            "pipenv-lock = jaysonsantos_pre_commit_hooks.pipenv_lock:main",
        ]
    },
)
