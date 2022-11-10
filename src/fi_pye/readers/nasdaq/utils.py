import pandas as pd


def _validate_limit(limit):
    """ """
    if limit is not None and not isinstance(limit, int):
        raise TypeError(f"invalid limit: {limit} with type: {type(limit)}. limit must be of type: int. ")

    return limit


def _validate_timeframe(value: str):
    """ """
    valid_values = ["month", "year"]
    if value not in valid_values:
        raise ValueError(f"Invalid timeframe: {value}. Valid timeframes include: {valid_values}. ")

    return value


def _validate_dates(start, end):
    """ """
    try:
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
    except (TypeError, ValueError):
        raise ValueError("Invalid date format.")

    if start > end:
        raise ValueError("start date must be earlier than end date.")

    return start, end
