from setuptools import setup, find_packages # type: ignore

setup(
    name="PAG-WEB-STREAMLIT",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias
        'numpy>=1.0',
        'pandas'
    ],
)