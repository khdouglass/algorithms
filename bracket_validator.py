def bracket_validator(equation):
    """Validate whether an equation's brackets are balanced."""

    bracket_dict = {'(': ')', '{': '}', '[': ']'}
    bracket_list = []

    for char in equation:
        if char in bracket_dict:
            bracket_list.append(char)
        if char == bracket_dict[bracket_list[-1]]:
            if len(bracket_list) > 0:
                bracket_list.pop()
            else:
                return False
    if len(bracket_list) == 0:
        return True
    else: 
        return False