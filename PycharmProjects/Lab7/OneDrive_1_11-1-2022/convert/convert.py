def float_default(string):
    try:
        return float(string)
    except ValueError:
        return string
