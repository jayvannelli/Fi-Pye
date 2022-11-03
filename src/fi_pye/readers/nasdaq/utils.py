import pandas as pd


def _validate_treasury(treasury):
    valid_values = [
        "1mo", "2mo", "3mo", "6mo", "1yr", "3yr",
        "5yr", "7yr", "10yr", "20yr", "30yr"
    ]
    if treasury not in valid_values or not isinstance(treasury, str):
        raise ValueError(f"Invalid treasury: {treasury}. Valid treasury values include: {valid_values}. ")

    return valid_values.index(treasury) + 1


def _validate_limit(limit):
    """ """
    if limit is not None and not isinstance(limit, int):
        raise TypeError(f"invalid limit: {limit} with type: {type(limit)}. limit must be of type: int. ")

    return limit


def _validate_yield_duration(value: str) -> int:
    """ """
    valid_durations = ["5yr", "7yr", "10yr", "20yr", "30yr"]
    if value not in valid_durations:
        raise ValueError(f"Invalid duration: {value}. Valid durations include: {valid_durations}. ")

    return valid_durations.index(value) + 1

def _validate_tbill_duration(value: str, type: str) -> str:
    """ """
    valid_values = {
        "4wk": 1,
        "8wk": 3,
        "13wk": 5,
        "26wk": 7,
        "52wk": 9,
    }
    if value not in valid_values or not isinstance(value, str):
        raise ValueError(f"Invalid duration: {value}. Valid durations include: {valid_values}. ")

    if type == "discount-rate":
        val = valid_values[value]

    elif type == "coupon-rate":
        val = valid_values[value] + 1

    return val


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