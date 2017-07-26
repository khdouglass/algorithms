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

    # returns True or False
    return bracket_list == []

def is_valid(code):
    """Interview Cake solution."""

    openers_to_closers = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    openers = frozenset(openers_to_closers.keys())
    closers = frozenset(openers_to_closers.values())

    openers_stack = []

    for char in code:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()

                # if this closer doesn't correspond to the most recently
                # seen unclosed opener, short-circuit, returning false
                if not openers_to_closers[last_unclosed_opener] == char:
                    return False

    return openers_stack == []