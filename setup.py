# setup.py
# created by cubicles

from setuptools import setup, find_packages

setup(
        name='ventechow',
        version='0.1',
        packages=find_packages(),
        install_requires=[
            'pandas',
            'joblib',
            ],
    )


