def slices(series, length):
    if not series:
        raise ValueError("series cannot be empty")

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    result = []

    for idx in range(len(series) - length + 1):
        result.append(series[idx:idx+length])

    return result
