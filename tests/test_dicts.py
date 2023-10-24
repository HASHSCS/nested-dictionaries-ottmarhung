import pytest
from solutions.dicts import *

# Tests for get_information
def test_get_information():
    assert get_information({'a': {'b': 1, 'c': 2}}, 'a', 'b') == 1
    assert get_information({'a': {'b': 1, 'c': 2}}, 'a', 'd') == None
    assert get_information({'a': {'b': 1, 'c': 2}}, 'x', 'b') == None

# Tests for add_information
def test_add_information():
    assert add_information({'a': {}}, 'a', 'b', 1) == {'a': {'b': 1}}
    assert add_information({'a': {'b': 1}}, 'a', 'b', 2) == {'a': {'b': 2}}
    assert add_information({'a': {'b': 1}}, 'x', 'y', 3) == {'a': {'b': 1}, 'x': {'y': 3}}

# Tests for remove_information
def test_remove_information():
    assert remove_information({'a': {'b': 1, 'c': 2}}, 'a', 'b') == {'a': {'c': 2}}
    assert remove_information({'a': {'b': 1, 'c': 2}}, 'a', 'd') == {'a': {'b': 1, 'c': 2}}
    assert remove_information({'a': {'b': 1, 'c': 2}}, 'x', 'b') == {'a': {'b': 1, 'c': 2}}

# Tests for get_nested_value
def test_get_nested_value():
    assert get_nested_value({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']) == 1
    assert get_nested_value({'a': {'b': {'c': 1}}}, ['a', 'b', 'd']) == None
    assert get_nested_value({'a': {'b': {'c': 1}}}, ['a', 'x']) == None

# Tests for set_nested_value
def test_set_nested_value():
    data = {'a': {'b': 1}}
    assert set_nested_value(data, ['a', 'b'], 2) == {'a': {'b': 2}}
    assert set_nested_value(data, ['a', 'c'], 3) == {'a': {'b': 2, 'c': 3}}
    assert set_nested_value(data, ['x', 'y'], 4) == {'a': {'b': 2, 'c': 3}, 'x': {'y': 4}}
