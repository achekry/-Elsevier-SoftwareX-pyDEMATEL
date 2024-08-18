from setuptools import setup, find_packages
import sys

# Check for tkinter availability
try:
    import tkinter as tk
except ImportError:
    print("Warning: tkinter is not available. This package requires tkinter, which is included with Python but might not be installed in some environments.")
    if sys.platform.startswith('linux'):
        print("On Linux, you may need to install tkinter separately using your package manager.")
        print("For Debian/Ubuntu: sudo apt-get install python3-tk")
        print("For Fedora: sudo dnf install python3-tk")
    sys.exit(1)  # Optionally exit setup if tkinter is critical

# Define the setup configuration

setup(
    name="pyDEMATEL",
    version="0.2.2",
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
