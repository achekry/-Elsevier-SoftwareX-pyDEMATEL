from setuptools import setup, find_packages

setup(
    name="pyDEMATEL",
    version="0.1.7",
    packages=find_packages(),
    install_requires=[
    'numpy>=1.22.0',
    'matplotlib>=3.4.3',
    'openpyxl>=3.0.9',
    ],
    author="Abderrahman Chekry, Jamal Bakkas, Mohamed Hanin, Elizabeth Caro Montero, Mirtha Silvana Garat de Marin and Imran Ashraf",
    author_email="a.chekry@uca.ac.ma",
    description="pyDematel a python-based tool implementing the Dematel and fuzzy Dematel methods for improved decision making",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/achekry/-Elsevier-SoftwareX-pyDEMATEL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pydematel=pyDEMATEL.DEMATELWindow:main',
        ],
    },
)
