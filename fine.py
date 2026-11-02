def calculate_fine(days):
    if not isinstance(days, int) or isinstance(days, bool):
        raise ValueError("Days must be an integer")

    if days < 0:
        raise ValueError("Days cannot be negative")

    if days <= 5:
        return days * 2
    else:
        return 10 + (days - 5) * 5