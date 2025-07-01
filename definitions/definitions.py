
def parse_budget_categories(categories_input: str) -> list:
    """
    Parses a comma-separated string of budget categories into a list of category names.
    
    Args:
        categories_input (str): A string containing comma-separated budget category names.
        
    Returns:
        list: A list of category names as strings.
        
    Raises:
        TypeError: If categories_input is not a string.
    """
    if not isinstance(categories_input, str):
        raise TypeError("Input must be a string.")
    # If empty string, return list with one empty string
    if categories_input == "":
        return [""]
    # Split by comma and strip spaces; handle empty categories
    return [category.strip() for category in categories_input.split(',')]
