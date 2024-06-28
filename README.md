# pyDEMATEL

[![License: BSD](https://img.shields.io/badge/License-BSD-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)


## Table of Contents
- [Overview](#overview)
- [License](#license)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Authors](#authors)
- [Contact](#contact)


## Overview

The `pyDEMATEL` tool is designed to implement and facilitate the use of the DEMATEL and Fuzzy DEMATEL methods. The tool comprises three distinct classes: `DEMATELSolver`, `FuzzyDEMATELSolver`, and `DEMATELWindow`.

- **DEMATELSolver**: Implements the standard DEMATEL method.
- **FuzzyDEMATELSolver**: Implements the Fuzzy DEMATEL method.
- **DEMATELWindow**: Provides a graphical interface for users to interact with the tool.

This separation is designed to offer two ways of using the tool:

1. **Graphical Interface Mode**: Allows decision-makers to use the tool directly via its graphical interface provided by the `DEMATELWindow` class.
2. **Package Integration Mode**: Allows developers to directly integrate the `DEMATELSolver` or `FuzzyDEMATELSolver` classes into their own applications, without needing the graphical interface.

## License
This project is licensed under the BSD License - see the LICENSE file for details.

## Features

- **Feature 1**: Data Acquisition Methods: Acquires numbers and names of experts and factors and gathers evaluation matrix values from each expert.
- **Feature 2**: Matrix Generation Steps: Computes the "direct-influence matrix Z", generates the "normalized direct-influence matrix X", creates the "total-influence matrix T" and produces an "influential Relation Map IRM".
- **Feature 3**: Output Presentation Methods: Presents outputs in various formats, including graphical representations and provides options to generate Excel documents.
- **Feature 4**: Integration and Flexibility: Designed for integration into Python-based programs and Implements the DEMATEL method comprehensively, ensuring accuracy and completeness.

## Installation

### Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

### Steps to Install
To install the `pyDEMATEL` package, use the following command:

```sh
pip install pyDEMATEL
```

## Usage
To start using `pyDEMATEL`, follow these steps:
- **Step 1**:  Enter the number of experts and the number of factors.
- **Step 2**:  Provide the names of experts and factors.
- **Step 3**:  Enter the evaluation matrix for each expert.
- **Step 4**:  Generate the results.

### Example
**Here is an example of how to use the graphical interface of the software**:
Use the following command to execute the graphical interface of the `pyDEMATEL` software.

```sh
pydematel
```

**Here is an example demonstrating how to use the FuzzyDEMATELSolver package, which implements the FuzzyDEMATEL method**:
```sh
from pyDEMATEL.FuzzyDEMATELSolver import FuzzyDEMATELSolver
import numpy as np
```
Inputs:
```sh
expert = "Alami"
factors = [ "A1 ", 
            "A2 ", 
            "A3 ", 
            "A4 ", 
            "A5 ", 
           "A6 ", 
            "A7 ", 
           "A8",
           "A9",
           "A10",           
           "A11", 
            "A12 ", 
            "A13 ", 
            "A14 ", 
            "A15 ", 
           "A16 ", 
            "A17 ", 
           "A18"] 
```
           
Linguistic evaluation matrix of marine experts’ consensus: source  https://www.sciencedirect.com/science/article/pii/S0950423015300498

```sh
valeurs=[
[(0, 0, 0.25),(0, 0, 0.25),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0, 0.25),(0, 0.25, 0.5),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0, 0.25),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0.25, 0.5),(0.5, 0.75, 1)],
[(0.5, 0.75, 1),(0, 0, 0.25),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0, 0.25),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0.75, 1, 1),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0.25, 0.5),(0.5, 0.75, 1)],
[(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.5, 0.75, 1),(0, 0, 0.25),(0.25, 0.5, 0.75),(0.25, 0.5, 0.75)],
[(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0, 0.25),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0.75, 1, 1),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0.75, 1, 1),(0.5, 0.75, 1),(0, 0.25, 0.5),(0.5, 0.75, 1),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5)],
[(0, 0.25, 0.5),(0, 0.25, 0.5),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0, 0.25),(0.5, 0.75, 1),(0.5, 0.75, 1),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0.75, 1, 1),(0.5, 0.75, 1),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0.5, 0.75, 1)],
[(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0.75, 1, 1)],
[(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.25, 0.5, 0.75)],
[(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0, 0.25),(0, 0, 0.25),(0.5, 0.75, 1),(0.5, 0.75, 1),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0, 0.25)],
[(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0, 0.25),(0.5, 0.75, 1),(0, 0, 0.25),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0.25, 0.5, 0.75),(0, 0, 0.25)],
[(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0.5, 0.75, 1),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.75, 1, 1),(0, 0, 0.25),(0, 0.25, 0.5),(0.5, 0.75, 1),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.5, 0.75, 1)],
[(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0.75, 1, 1),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0, 0, 0.25),(0, 0.25, 0.5),(0.5, 0.75, 1),(0, 0, 0.25),(0.75, 1, 1),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0.5, 0.75, 1)],
[(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0.75, 1, 1),(0.5, 0.75, 1),(0, 0, 0.25),(0, 0.25, 0.5),(0.75, 1, 1),(0, 0, 0.25),(0, 0.25, 0.5),(0.5, 0.75, 1),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0, 0.25),(0, 0.25, 0.5),(0.5, 0.75, 1),(0, 0, 0.25),(0, 0, 0.25),(0.5, 0.75, 1)],
[(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0.75, 1, 1),(0.25, 0.5, 0.75),(0.75, 1, 1),(0, 0.25, 0.5),(0.5, 0.75, 1),(0, 0, 0.25),(0, 0, 0.25),(0, 0.25, 0.5),(0.5, 0.75, 1),(0.5, 0.75, 1),(0, 0, 0.25),(0.5, 0.75, 1),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5)],
[(0, 0.25, 0.5),(0, 0.25, 0.5),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0, 0.25),(0, 0, 0.25),(0, 0, 0.25),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0, 0.25),(0, 0, 0.25),(0, 0, 0.25),(0.5, 0.75, 1)],
[(0.25, 0.5, 0.75),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0.75, 1, 1),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0.5, 0.75, 1),(0.5, 0.75, 1),(0, 0, 0.25),(0.75, 1, 1),(0.25, 0.5, 0.75),(0.5, 0.75, 1)],
[(0, 0.25, 0.5),(0.75, 1, 1),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.25, 0.5, 0.75),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0.5, 0.75, 1),(0.75, 1, 1)],
[(0, 0, 0.25),(0.5, 0.75, 1),(0.75, 1, 1),(0.5, 0.75, 1),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0.25, 0.5),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0, 0, 0.25),(0.25, 0.5, 0.75)],
[(0, 0.25, 0.5),(0.5, 0.75, 1),(0.75, 1, 1),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0.25, 0.5),(0, 0, 0.25),(0, 0, 0.25),(0, 0.25, 0.5),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0.25, 0.5, 0.75),(0, 0.25, 0.5),(0, 0, 0.25),(0.25, 0.5, 0.75),(0.5, 0.75, 1),(0, 0.25, 0.5),(0, 0, 0.25)]
]           

matrices = np.array([np.array(valeurs, dtype=object)])
```
Creating an instance of FuzzyDEMATELSolver:
```sh
solver = FuzzyDEMATELSolver()
solver.setMatrix(matrices)
print(solver.getMatrix())
solver.addExpert(expert)
solver.setFactors(factors)

solver.setNumberOfExperts(1)
solver.setNumberOfFactors(18)

print(solver.getExperts())
print(solver.getFactors())
```
Executing the steps of the FuzzyDEMATEL method:
```sh
solver.step1()
print(solver.getFuzzyDirectInfluenceMatrix())
solver.step2()
print(solver.getFuzzyNormalizedDirectInfluenceMatrix())
solver.step3()
print(solver.getFuzzyTotalInfluenceMatrix())
solver.step4()
print(solver.getRalation())
print(solver.getProminence())
```
Generating the graph:
```sh
solver.drawCurve()
```
**Note** : To use the DEMATELSolver package, which implements the DEMATEL method, follow the same steps as in the previous example.
## Authors
- Abderrahman Chekry
- Jamal Bakkas
- Mohamed Hanine
- Elizabeth Caro Montero
- Mirtha Silvana Garat de Marin
- Imran Ashraf

## Contact
If you have any questions or suggestions, feel free to contact us at a.chekry@uca.ac.ma.
