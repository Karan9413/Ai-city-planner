import operator

_SAFE_OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow,
}


def calculator_tool(query: str):
    try:
        parts = query.split()
        if len(parts) == 3:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
            if op in _SAFE_OPS:
                return str(_SAFE_OPS[op](a, b))
        return str(eval(query))
    except Exception:
        return "Invalid calculation"