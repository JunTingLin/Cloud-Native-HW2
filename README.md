# Cloud-Native-HW2
This is assignment 2 for Cloud-Native

## Overview

This repository contains a simple Python project that demonstrates basic arithmetic functionality. The main focus is on the addition function provided in `main.py`, and unit tests are implemented using pytest in the `tests` directory.

## Project Structure

- **main.py**: Contains the core logic including the `add` function.
- **tests/test_main.py**: Contains pytest unit tests to verify the functionality of the `add` function.
- **.github/workflows/ci.yml**: GitHub Actions configuration file that automatically runs tests on pushes and pull requests.
- **.github/ISSUE_TEMPLATE/**: Contains issue templates (e.g., `task.yml` ) for managing tasks.

## How to Run the Project

### 1. Running the Application
To run the main application, execute the following command:
```bash
python main.py
```
This will run the main.py file, which demonstrates the addition function by adding two numbers and printing the result.


### 2. Running Unit Tests
Ensure that you have pytest installed. If not, install it using:
```bash
pip install pytest
```
Then, run the tests by executing:
```bash
pytest tests/test_main.py
```
This command will run all unit tests to verify that the add function works as expected.
