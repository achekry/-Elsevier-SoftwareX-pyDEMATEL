from setuptools import setup, find_packages

setup(
    name="pyDEMATEL",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],  # Liste des dépendances
    author="Abderrahman CHEKRY, Jamal Bakkas, Mohamed Hanine",
    author_email="a.chekry@uca.ac.ma",
    description="pyDematel a python-based tool implementing the Dematel and fuzzy Dematel methods for improved decision making",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/achekry/-Elsevier-SoftwareX-pyDEMATEL",  # Lien vers le repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",  # Utilisation d'un classifier valide
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
