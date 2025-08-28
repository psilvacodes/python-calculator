# Python Calculator

A simple Python calculator package supporting basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division error handling)

## Installation

Clone the repository and create a virtual environment:

```bash
git clone git@github.com:YOUR_USERNAME/python-calculator.git
cd python-calculator
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```python
from calculator.operations import add, subtract, multiply, divide

print(add(2, 3))       # 5
print(subtract(5, 2))  # 3
print(multiply(3, 4))  # 12
print(divide(10, 2))   # 5
```

## Testing

```bash
pytest
```

All tests are located in the tests/ folder.

## Licence

This project is licensed under the MIT License. See the LICENSE file for 
details.
