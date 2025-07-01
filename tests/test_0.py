import pytest
from definition_e11778c2797c45ed882ee08cf3021b25 import parse_budget_categories

@pytest.mark.parametrize("categories_input, expected", [
    # Typical case: multiple categories separated by commas
    ("Groceries, Rent, Utilities", ["Groceries", "Rent", "Utilities"]),
    # Single category, should return list with one item without spaces
    ("Travel", ["Travel"]),
    # Multiple categories with extra spaces
    (" Entertainment , Health , Travel  ", ["Entertainment", "Health", "Travel"]),
    # Empty string should return list with empty string or possibly handle as empty list
    ("", [""]),
    # String with only spaces, should probably return list with empty string
    ("   ", [""]),
    # Multiple commas with no categories between
    (",, ,", ["", "", " "]),
    # Categories with special characters
    ("Food & Drinks, Utilities@Home", ["Food & Drinks", "Utilities@Home"]),
    # Categories with numeric characters
    ("Category1,2,3", ["Category1", "2", "3"]),
    # Input is not a string (should handle or raise error)
    (123, TypeError),
    (None, TypeError),
    ([], TypeError),
])
def test_parse_budget_categories(categories_input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            parse_budget_categories(categories_input)
    else:
        result = parse_budget_categories(categories_input)
        assert result == expected
