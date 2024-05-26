# pyDEMATEL
## Overview

The `pyDEMATEL` tool is designed to implement and facilitate the use of the DEMATEL and Fuzzy DEMATEL methods. The tool comprises three distinct classes: `DEMATEL_Solver`, `Fuzzy_DEMATEL_Solver`, and `DEMATEL_Window`.

- **DEMATEL_Solver**: Implements the standard DEMATEL method.
- **Fuzzy_DEMATEL_Solver**: Implements the Fuzzy DEMATEL method.
- **DEMATEL_Window**: Provides a graphical interface for users to interact with the tool .

This separation is designed to offer two ways of using the tool:

1. **Graphical Interface Mode**: Allows decision-makers to use the tool directly via its graphical interface provided by the `DEMATEL_Window` class.
2. **Package Integration Mode**: Allows developers to directly integrate the `DEMATEL_Solver` or `Fuzzy_DEMATEL_Solver` classes into their own applications, without needing the graphical interface.

## Installation

To install the `pyDEMATEL` package, use the following command:

```sh
pip install pyDEMATEL
