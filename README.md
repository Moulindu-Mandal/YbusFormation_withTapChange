# Ybus Matrix Formation with Tap-Changing Transformers

This repository contains a Python (or MATLAB/C) program designed to build the Ybus (admittance) matrix for a power system, given the system's line data. The program is flexible and scalable to handle systems of arbitrary size and includes provisions for regulating transformer tap settings.

## Features
- **n-Dimensional System Support**: The program is generic and can accommodate any number of buses (`n`) as specified by the user.
- **Input Flexibility**: Line data can be provided via an Excel or CSV file. The program prompts the user to input the file path and automatically parses the data to generate the Ybus matrix.
- **Transformer Tap Accommodation**: The program supports transformer tap ratios, which are incorporated into the Ybus matrix calculations.
- **Non-Zero Entry Count**: After generating the Ybus matrix, the program outputs the total number of non-zero and zero entries for quick analysis.

## How to Use
1. **Define System Size**: When prompted, input the size (`n`) of the power system (number of buses).
2. **Input Line Data**: Provide the file path to the system line data in Excel or CSV format. Ensure that the data includes the necessary parameters such as resistance, reactance, line charging susceptance, and transformer details (if applicable).
3. **Tap Settings**: If regulating transformers are part of the system, the program will include the tap settings in the Ybus calculations.
4. **Matrix Output**: The program will display the Ybus matrix and provide the total count of non-zero and zero entries.

### Input File Format
The input file should contain the following columns:
- Bus i
- Bus j
- Resistance (R)
- Reactance (X)
- Susceptance (B)
- Transformer Tap Ratio (if applicable)

### Example
An example input file and the corresponding output Ybus matrix are included in the repository for reference.

## Dependencies
- Python 3.x (if using Python version)
- Libraries: `numpy`, `pandas`
- For Excel file input, ensure `openpyxl` is installed:  
  ```bash
  pip install openpyxl
##Output
- Ybus matrix as a matrix format
- Total non-zero and zero entries in the matrix
##License
This project is licensed under the MIT License.
