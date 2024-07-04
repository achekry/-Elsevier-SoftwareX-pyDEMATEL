# pyDEMATEL

[![License: BSD](https://img.shields.io/badge/License-BSD-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

![Graphical interface of pyDEMATEL](https://raw.githubusercontent.com/achekry/-Elsevier-SoftwareX-pyDEMATEL/main/img/fig2.png)

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
This project is licensed under the BSD License - see the [LICENSE](LICENSE.md) file for details.

## Features

- **Feature 1**: Data Acquisition Methods: Acquires numbers and names of experts and factors and gathers evaluation matrix values from each expert.
- **Feature 2**: Matrix Generation Steps: Computes the "direct-influence matrix Z", generates the "normalized direct-influence matrix X", creates the "total-influence matrix T" and produces an "influential Relation Map IRM".
- **Feature 3**: Output Presentation Methods: Presents outputs in various formats, including graphical representations and provides options to generate Excel documents.
- **Feature 4**: Integration and Flexibility: Designed for integration into Python-based programs and Implements the DEMATEL method comprehensively, ensuring accuracy and completeness.

## Installation

### Prerequisites
Before you begin, ensure that `Python` and `pip` are installed and updated on your system.

### Steps to Install
To install the `pyDEMATEL` package, use the following command:

```sh
pip install pyDEMATEL
```
The following libraries are installed automatically with `pyDEMATEL`:
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

## Usage
Use the following command to execute the graphical interface of the `pyDEMATEL` software:

```sh
pydematel
```
 The steps to follow are : :
- **Step 1**:  Enter the number of experts and the number of factors.
- **Step 2**:  Provide the names of experts and factors.
- **Step 3**:  Choose the solving method: either DEMATEL or FuzzyDEMATEL
- **Step 4**:  Enter the evaluation matrix for each expert.
- **Step 5**:  Generate the results.

### Example

**Here is an example demonstrating how to use the FuzzyDEMATELSolver package, which implements the FuzzyDEMATEL method**:
```sh
from pyDEMATEL.FuzzyDEMATELSolver import FuzzyDEMATELSolver
import numpy as np

# Inputs: experts and factors
expert = "bob"
factors =  ["A1", 
            "A2", 
            "A3", 
            "A4", 
            "A5", 
            "A6", 
            "A7", 
            "A8",
            "A9",
            "A10",           
            "A11", 
            "A12", 
            "A13", 
            "A14", 
            "A15", 
            "A16", 
            "A17", 
            "A18"] 
    
# Linguistic evaluation matrix of marine experts’ consensus in other words evaluation matrix for each expert (source  https://www.sciencedirect.com/science/article/pii/S0950423015300498)
evaluationMatrix=[
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

matrices = np.array([np.array(evaluationMatrix, dtype=object)])

# Creating an instance of FuzzyDEMATELSolver
solver = FuzzyDEMATELSolver()
solver.setMatrix(matrices)
print('********* expert s individual direct influence matrices *********')
print(solver.getMatrix())
solver.addExpert(expert)
solver.setFactors(factors)
solver.setNumberOfExperts(1)
solver.setNumberOfFactors(18)
print('********* List of experts *********')
print(solver.getExperts())
print('********* List of Factors *********')
print(solver.getFactors())

# Executing the steps of the FuzzyDEMATEL method
solver.step1()
print('********* Direct Influence Fuzzy Matrix *********')
print(solver.getFuzzyDirectInfluenceMatrix())
solver.step2()
print('********* Normalized Direct Influence Fuzzy Matrix *********')
print(solver.getFuzzyNormalizedDirectInfluenceMatrix())
solver.step3()
print('********* Total Influence Fuzzy Matrix *********')
print(solver.getFuzzyTotalInfluenceMatrix())
solver.step4()
print('********* Relation *********')
print(solver.getRalation())
print('********* Prominence *********')
print(solver.getProminence())

# Generating the graph
solver.drawCurve()

# Generating excel file
solver.savexl(input("Please enter the destination path for the Excel file:"))

```

**Here is an example demonstrating how to use the DEMATELSolver package, which implements the Classical DEMATEL method**:
```sh
from pyDEMATEL.DEMATELSolver import DEMATELSolver
import numpy as np

# Inputs: experts and factors
expert = "bob"
factors = [ "A1", 
            "A2", 
            "A3", 
            "A4", 
            "A5", 
            "A6", 
            "A7", 
            "A8"]
    
# Average matrix in other words evaluation matrix for each expert (source  https://imisc.figshare.com/articles/journal_contribution/paper-codal-etal_pdf/7325816/3)
matrices= [np.array([[0.00, 1.11, 1.01, 1.41, 1.66, 0.50, 1.60, 2.00],                   
                      [1.43, 0.00, 2.22, 2.00, 2.40, 1.20, 1.66, 1.33], 
                      [0.82, 1.00, 0.00, 2.05, 2.44, 1.65, 2.65, 1.88], 
                      [1.92, 0.80, 1.82, 0.00, 2.75, 3.50, 3.33, 3.10], 
                      [2.20, 3.11, 1.25, 0.75, 0.00, 2.25, 2.66, 1.75], 
                      [1.01, 1.31, 1.45, 1.20, 1.44, 0.00, 0.75, 3.00], 
                      [3.50, 3.20, 2.95, 3.33, 2.88, 1.85, 0.00, 1.40], 
                      [0.50, 1.25, 1.40, 3.66, 1.00, 2.00, 3.33, 0.00]])]


# Creating an instance of DEMATELSolver
solver = DEMATELSolver()
solver.setMatrix(matrices)
print('********* expert s individual direct influence matrices *********')
print(solver.getMatrix())
solver.addExpert(expert)
solver.setFactors(factors)
solver.setNumberOfExperts(1)
solver.setNumberOfFactors(8)
print('********* List of experts *********')
print(solver.getExperts())
print('********* List of Factors *********')
print(solver.getFactors())

# Executing the steps of the DEMATEL method
solver.step1()
print('********* Direct Influence Matrix *********')
print(solver.getDirectInfluenceMatrix())
solver.step2()
print('********* Normalized Direct Influence Matrix *********')
print(solver.getNormalizedDirectInfluenceMatrix())
solver.step3()
print('********* Total Influence Matrix *********')
print(solver.getTotalInfluenceMatrix())
solver.step4()
print('********* Relation *********')
print(solver.getRalation())
print('********* Prominence *********')
print(solver.getProminence())

# Generating the graph
solver.drawCurve()

# Generating excel file
solver.savexl(input("Please enter the destination path for the Excel file:"))

```


## Authors
- Abderrahman Chekry<sup>1</sup>
- Jamal Bakkas<sup>1</sup>
- Mohamed Hanine<sup>2</sup>
- Elizabeth Caro Montero<sup>3,4,5</sup>
- Mirtha Silvana Garat de Marin<sup>3,7,8</sup>
- Imran Ashraf<sup>8</sup>
<br/><sup>1</sup>LAPSSII Laboratory, Graduate School of Technology, Cadi Ayyad University, Safi, Morocco.
<br/><sup>2</sup>LTI Laboratory, ENSA, Chouaib Doukkali University, El Jadida, Morocco.
<br/><sup>3</sup>Universidad Europea del Atlantico. Isabel Torres 21, 39011 Santander, Spain.
<br/><sup>4</sup>Universidad Internacional Iberoamericana Campeche 24560, Mexico.
<br/><sup>5</sup>Universidad de La Romana. La Romana, Republica Dominicana.
<br/><sup>6</sup>Universidad Internacional Iberoamericana Arecibo, Puerto Rico 00613, USA.
<br/><sup>7</sup>Universidade Internacional do Cuanza. Cuito, Bie, Angola.
<br/><sup>8</sup>Department of Information and Communication Engineering, Yeungnam University, Gyeongsan 38541, South Korea.

## Contact
If you have any questions or suggestions, feel free to contact us at a.chekry@uca.ac.ma.
