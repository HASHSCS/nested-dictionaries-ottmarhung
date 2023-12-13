[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12538694&assignment_repo_type=AssignmentRepo)
# Python Nested Dictionaries Assignment

In this assignment, you will delve deeper into Python dictionaries, focusing on nested dictionaries.

## Instructions

- Clone this repository to your local machine.
- Navigate to the `solutions` directory and open the `dicts.py` file.
- Complete the functions provided as per the specifications.
- Push your code to GitHub to see the results of the tests.

## Requirements

- Python 3.8+
- `pytest` for running tests locally

To install the dependencies:

```bash
pip install -r requirements.txt
```

To run the tests locally:

```bash
pytest
```

## Grading

Your assignment will be graded automatically every time you push. Check the GitHub Actions tab to see the results.

## Exercises

### Basic Operations on Nested Dictionaries:

1. **Retrieve Information**:
   - `get_information(data, outer_key, inner_key)`: retrieves the associated value from a nested dictionary given the outer and inner keys.

2. **Add Information**:
   - `add_information(data, outer_key, inner_key, value)`: adds or modifies information in the nested dictionary using the given outer and inner keys.

3. **Remove Information**:
   - `remove_information(data, outer_key, inner_key)`: removes the associated key-value pair from a nested dictionary given the outer and inner keys.

### Advanced Operations on Nested Dictionaries:

4. **Retrieve Nested Value**:
   - `get_nested_value(data, key_chain)`: retrieves the value of a given key chain from a nested dictionary.

5. **Set Nested Value**:
   - `set_nested_value(data, key_chain, value)`: modifies the nested dictionary to set a value at a specific key chain.

Your task is to implement these functions in `solutions/dicts.py` and ensure they pass all tests in `tests/test_dicts.py`.

Good luck and happy coding!