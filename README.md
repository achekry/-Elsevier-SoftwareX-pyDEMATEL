# pyDEMATELSolver

## Overview

The `pyDEMATELSolver` tool is designed to implement and facilitate the use of the DEMATEL and Fuzzy DEMATEL methods. The tool comprises three distinct classes: `DEMATELSolver`, `FuzzyDEMATELSolver`, and `DEMATELWindow`.

- **DEMATELSolver**: Implements the standard DEMATEL method.
- **FuzzyDEMATELSolver**: Implements the Fuzzy DEMATEL method.
- **DEMATELWindow**: Provides a graphical interface for users to interact with the tool .

This separation is designed to offer two ways of using the tool:

1. **Graphical Interface Mode**: Allows decision-makers to use the tool directly via its graphical interface provided by the `DEMATELWindow` class.
2. **Package Integration Mode**: Allows developers to directly integrate the `DEMATELSolver` or `FuzzyDEMATELSolver` classes into their own applications, without needing the graphical interface.

## Installation

To install the `pyDEMATELSolver` package, use the following command:

```sh
pip install pyDEMATEL_Package
